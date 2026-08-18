suppressPackageStartupMessages({
  library(ggtree)
  library(ape)
  library(treeio)
  library(ggplot2)
  library(phangorn)
})

meta <- read.delim("phylo_q2/tip_metadata.tsv", sep="\t", header=TRUE, stringsAsFactors=FALSE)

# Helper: compute consistency index of "genome" as a trait
# Equivalent question: how many parsimony changes (state transitions) does the tree need?
# If genomes were truly random, ~ceiling(338/3) transitions; perfect monophyly = 2 transitions.
phylo_genome_stats <- function(treefile, label) {
  tr <- read.tree(treefile)
  d <- meta[match(tr$tip.label, meta$label), ]
  genome_vec <- d$genome
  names(genome_vec) <- tr$tip.label
  # Use phangorn parsimony
  ph <- phyDat(matrix(genome_vec, ncol=1, dimnames=list(tr$tip.label, "g")), type="USER", levels=c("PvP01","PvW1","PvPAM"))
  p_score <- parsimony(tr, ph)
  
  # Compare to random: shuffle the labels 1000 times and re-score
  set.seed(42)
  rand <- replicate(1000, {
    perm_vec <- sample(genome_vec)
    names(perm_vec) <- tr$tip.label
    ph_rand <- phyDat(matrix(perm_vec, ncol=1, dimnames=list(tr$tip.label, "g")), type="USER", levels=c("PvP01","PvW1","PvPAM"))
    parsimony(tr, ph_rand)
  })
  min_possible <- 2   # 3 states minus 1 (perfect monophyly = 2 transitions)
  max_observed_rand <- max(rand)
  median_rand <- median(rand)
  p_val_more_clustered <- mean(rand <= p_score)
  
  # Count single-genome clades (monophyletic groups)
  # For each internal node, check if all descendants belong to same genome
  n_tips <- length(tr$tip.label)
  # Use ape's getMRCA + extract.clade
  internal_nodes <- (n_tips+1):(n_tips + tr$Nnode)
  is_single_genome <- sapply(internal_nodes, function(nd) {
    desc_tips <- tr$tip.label[unlist(phangorn::Descendants(tr, nd, "tips"))]
    desc_genomes <- unique(meta$genome[match(desc_tips, meta$label)])
    length(desc_genomes) == 1 && length(desc_tips) >= 2
  })
  single_g_nodes <- sum(is_single_genome)
  
  cat(sprintf(
    "\n=== %s ===\n  Parsimony score (genome trait): %d\n  Minimum possible (perfect monophyly): %d\n  Median random shuffle: %.1f\n  Max random shuffle: %d\n  P-value (more clustered than random): %.4f\n  Internal nodes with all-single-genome descendants: %d / %d\n",
    label, p_score, min_possible, median_rand, max_observed_rand,
    p_val_more_clustered, single_g_nodes, length(internal_nodes)
  ))
  return(p_score)
}

# Run for all three Q2 trees
ps_aa  <- phylo_genome_stats("phylo_q2/trees/q2_aa.treefile",   "Q2 AA tree (VT+F+R6)")
ps_3di <- phylo_genome_stats("phylo_q2/trees/q2_3di.treefile",  "Q2 3Di tree")
ps_pt  <- phylo_genome_stats("phylo_q2/trees/q2_part.treefile", "Q2 Partitioned AA+3Di")

# Visualization: trees with tips colored by genome
plot_q2 <- function(treefile, title, outpdf) {
  tr <- read.tree(treefile)
  p <- ggtree(tr, layout="circular", size=0.2) %<+% meta +
    geom_tippoint(aes(color=genome), size=0.6) +
    scale_color_manual(values=c(PvP01="#E41A1C", PvW1="#377EB8", PvPAM="#4DAF4A")) +
    ggtitle(title) +
    theme_tree() +
    theme(legend.position="bottom")
  ggsave(outpdf, p, width=8, height=8)
  cat("Wrote", outpdf, "\n")
}
plot_q2("phylo_q2/trees/q2_aa.treefile",   "Q2: FS_001 AA tree (n=338)",            "phylo_q2/q2_aa_tree.pdf")
plot_q2("phylo_q2/trees/q2_3di.treefile",  "Q2: FS_001 3Di tree (n=338)",           "phylo_q2/q2_3di_tree.pdf")
plot_q2("phylo_q2/trees/q2_part.treefile", "Q2: FS_001 Partitioned AA+3Di (n=338)", "phylo_q2/q2_part_tree.pdf")
