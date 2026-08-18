suppressPackageStartupMessages({
  library(ggtree)
  library(ape)
  library(treeio)
  library(ggplot2)
  library(dplyr)
})

meta <- read.delim("phylo_q1/tip_metadata.tsv", sep="\t", header=TRUE, stringsAsFactors=FALSE)
meta$logsize <- log10(meta$size + 1)
# Rename so the first column matches what ggtree expects ("label")
names(meta)[1] <- "label"
meta$display <- paste0(meta$fs_name, " (n=", meta$size, ")")

plot_one_tree <- function(treefile, title, outpdf) {
  tr <- read.tree(treefile)
  p <- ggtree(tr) %<+% meta +
    geom_tiplab(aes(label=display, color=dominant_genome), size=2.6, hjust=0, offset=0.05) +
    geom_tippoint(aes(size=logsize, color=dominant_genome)) +
    scale_color_manual(values=c(
      universal="black", PvP01="#E41A1C", PvW1="#377EB8", PvPAM="#4DAF4A", none="gray70"
    )) +
    scale_size_continuous(range=c(0.5, 4), name="log10(size)") +
    ggtitle(title) +
    theme_tree() +
    xlim(0, NA) +
    theme(plot.margin = margin(5,80,5,5))
  ggsave(outpdf, p, width=12, height=16)
  cat("Wrote", outpdf, "\n")
}

plot_one_tree("phylo_q1/trees/q1_aa.treefile",   "Q1: AA tree (VT+F+G4)",          "phylo_q1/q1_aa_tree.pdf")
plot_one_tree("phylo_q1/trees/q1_3di.treefile",  "Q1: 3Di tree (Garg & Hochberg)", "phylo_q1/q1_3di_tree.pdf")
plot_one_tree("phylo_q1/trees/q1_part.treefile", "Q1: Partitioned AA + 3Di tree",  "phylo_q1/q1_part_tree.pdf")
