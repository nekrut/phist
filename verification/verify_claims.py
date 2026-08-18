"""
Claim verification agent for pvivax_PIR_characterization.pdf
"""
import re, sys, os
from pathlib import Path
from collections import Counter, defaultdict
import pandas as pd

ROOT = Path("/Users/anton/.loom/analyses/phist2")
ALN = ROOT / "data/genomes/alignments"
RESULTS = []
def check(label, expected, observed, tol=None, expected_str=None, observed_str=None):
    if expected is None or observed is None:
        status = "NO-DATA"; match = False
    elif isinstance(expected, (int, float)) and isinstance(observed, (int, float)):
        if tol is None: tol = 0
        match = abs(observed - expected) <= tol
        status = "PASS" if match else "FAIL"
    else:
        match = expected == observed
        status = "PASS" if match else "FAIL"
    RESULTS.append({"label": label, "expected": str(expected),
                    "observed": str(observed), "status": status})

def hdr(t): pass  # no-op for the simplified version

# ---- PIR census ----
for g, path, exp in [("PvP01","data/genomes/PvP01_vir_hmm.fasta", 931),
                     ("PvW1", "data/genomes/PvW1_vir_hmm.fasta", 748),
                     ("PvPAM","data/genomes/PvPAM_vir_hmm.fasta", 985)]:
    n = sum(1 for line in (ROOT/path).read_text().splitlines() if line.startswith(">"))
    check(f"{g} VIR HMM hits", exp, n)
check("Total VIR HMM hits across 3 genomes", 2664,
      sum(sum(1 for line in (ROOT/p).read_text().splitlines() if line.startswith(">"))
          for p in ["data/genomes/PvP01_vir_hmm.fasta","data/genomes/PvW1_vir_hmm.fasta","data/genomes/PvPAM_vir_hmm.fasta"]))

for g, path, exp in [("PvP01","data/genomes/PvP01_proteins.fasta", 6523),
                     ("PvW1", "data/genomes/PvW1_proteins.fasta", 6075),
                     ("PvPAM","data/genomes/PvPAM_proteins.fasta", 6462)]:
    n = sum(1 for line in (ROOT/path).read_text().splitlines() if line.startswith(">"))
    check(f"{g} total annotated proteins", exp, n)

coords = pd.read_csv(ALN/"spatial/vir_coords.tsv", sep="\t")
for g, exp in [("PvP01",130), ("PvW1",17), ("PvPAM",26)]:
    check(f"{g} contigs bearing >=1 VIR", exp, int(coords[coords["genome"]==g]["chrom"].nunique()))
chrom_size = coords.groupby(["genome","chrom"])["end"].max().reset_index()
for g, exp_mb in [("PvP01",3.2), ("PvW1",3.7), ("PvPAM",3.3)]:
    largest = chrom_size[chrom_size["genome"]==g]["end"].max() / 1e6
    check(f"{g} largest contig (Mb)", exp_mb, round(largest,1), tol=0.1)

main_coords = pd.read_csv(ALN/"spatial/vir_coords_main.tsv", sep="\t")
for g, exp in [("PvP01",347), ("PvW1",634), ("PvPAM",735)]:
    check(f"{g} VIRs on main chromosomes", exp, int((main_coords["genome"]==g).sum()))
for g, exp_mb in [("PvP01",23.5), ("PvW1",27.7), ("PvPAM",27.4)]:
    total = main_coords[main_coords["genome"]==g].groupby("chrom")["end"].max().sum()/1e6
    check(f"{g} main-chromosome length sum (Mb)", exp_mb, round(total,1), tol=0.1)

# ---- Structural classes ----
fs = pd.read_csv(ALN/"foldseek_clusters_summary.tsv", sep="\t")
check("Number of Foldseek clusters", 73, len(fs))
f1 = fs[fs["FS_cluster"]=="FS_001"].iloc[0]
for k, exp in [("size",1197),("PvP01",400),("PvW1",349),("PvPAM",448)]:
    check(f"FS_001 {k}", exp, int(f1[k]))
total_c = fs["size"].sum()
check("Total VIRs in clusters", 2592, int(total_c))
check("FS_001 fraction of total (%)", 46.2, round(f1["size"]/total_c*100,1), tol=0.1)
top10 = fs.sort_values("size", ascending=False).head(10)
check("Top 10 size sum", 2453, int(top10["size"].sum()))
check("Top 10 fraction (%)", 94.6, round(top10["size"].sum()/total_c*100,1), tol=0.1)
for i, exp_size in [(1,1197),(2,385),(3,248),(4,143),(5,136),(6,96),(7,85),(8,74),(9,53),(10,36)]:
    check(f"FS_{i:03d} size", exp_size, int(top10.iloc[i-1]["size"]))
universal = fs[(fs["PvP01"]>0)&(fs["PvW1"]>0)&(fs["PvPAM"]>0)]
check("Universal clusters", 21, len(universal))
check("Members in universal (%)", 97.3, round(universal["size"].sum()/total_c*100,1), tol=0.1)
mcl = [c for c in (ALN/"../vir_clusters.txt").read_text().splitlines() if len(c.split())>=3]
check("MCL clusters", 146, len(mcl))
fs001_members = set()
rep_members = defaultdict(list)
with open(ALN/"foldseek_work/vir_struct_cluster_cluster.tsv") as f:
    for line in f:
        r,m = line.rstrip().split("\t"); rep_members[r].append(m)
fs001_members = set(rep_members["PVP01_0007630.1-p1"])
mcl_in_fs001 = sum(1 for c in mcl if any(m in fs001_members for m in c.split()))
check("MCL subfamilies collapsing into FS_001", 89, mcl_in_fs001)

# ---- Spatial ----
main = main_coords.copy()
chrom_len = main.groupby(["genome","chrom"])["end"].max().reset_index().rename(columns={"end":"chrom_len"})
main = main.merge(chrom_len, on=["genome","chrom"])
main["dist_to_end"] = main[["start","chrom_len"]].apply(lambda r: min(r["start"], r["chrom_len"]-r["start"]), axis=1)
main["rel_end"] = main["dist_to_end"]/main["chrom_len"]
check("Main-chrom VIRs in outer 10% (%)", 64.5, round((main["rel_end"]<0.10).mean()*100,1), tol=0.5)
for g, exp in [("PvP01",80),("PvW1",64),("PvPAM",57)]:
    f = (main[main["genome"]==g]["rel_end"]<0.10).mean()*100
    check(f"{g} VIRs in outer 10% (%)", exp, round(f), tol=2)
tandem = pd.read_csv(ALN/"spatial/tandem_test_main.tsv", sep="\t")
check("Tandem tests significant", 2, int((tandem["p_tandem"]<0.05).sum()))
check("Total tandem tests", 32, len(tandem))
synteny = pd.read_csv(ALN/"spatial/synteny_features.tsv", sep="\t")
from scipy import stats
pivot = synteny.pivot(index="FS_cluster", columns="genome", values="n_chroms").dropna()
for c1,c2,exp in [("PvP01","PvW1",0.909),("PvP01","PvPAM",0.914),("PvW1","PvPAM",0.915)]:
    rho,_ = stats.spearmanr(pivot[c1],pivot[c2])
    check(f"Spearman ρ n_chroms ({c1} vs {c2})", exp, round(rho,3), tol=0.005)
fs001_main = main[main["FS_cluster"]=="FS_001"]
for g, exp in [("PvP01",137),("PvW1",284),("PvPAM",320)]:
    check(f"FS_001 main-chrom members ({g})", exp, int((fs001_main["genome"]==g).sum()))
for g in ["PvP01","PvW1","PvPAM"]:
    check(f"FS_001 chromosomes occupied ({g})", 14, int(fs001_main[fs001_main["genome"]==g]["chrom"].nunique()))

# ---- Orthology ----
rbh = pd.read_csv(ALN/"ortho/fs001_rbh.tsv", sep="\t")
check("FS_001 RBH pairs", 194, len(rbh))
hk = pd.read_csv(ALN/"ortho/housekeeping_rbh.tsv", sep="\t")
check("Housekeeping RBH pairs", 5120, len(hk))
check("FS_001 RBH median identity (%)", 74.5, round(rbh["pident"].median(),1), tol=0.1)
check("Housekeeping RBH median identity (%)", 99.8, round(hk["pident"].median(),1), tol=0.1)
syn = pd.read_csv(ALN/"ortho/synteny_scores.tsv", sep="\t")
sd = syn["synteny_score"].value_counts().sort_index()
check("Synteny score 0", 139, int(sd.get(0,0)))
check("Synteny score >=3", 11, int(sd.get(3,0)+sd.get(4,0)))
combined = pd.read_csv(ALN/"ortho/orthologs_combined.tsv", sep="\t")
cc = combined["confidence"].value_counts()
for k,exp in [("high",11),("medium",26),("low",157)]:
    check(f"{k}-confidence orthologs", exp, int(cc.get(k,0)))
hi = combined[combined["confidence"]=="high"]
check("High-confidence median identity (%)", 87, int(round(hi["pident"].median())), tol=2)

# ---- Within-class diversity ----
n_q2 = sum(1 for line in (ALN/"phylo_q2/fs001_subcluster_rep_seq.fasta").read_text().splitlines() if line.startswith(">"))
check("Q2 sub-representatives", 338, n_q2)
genome_of = dict(line.rstrip().split("\t") for line in (ALN/"../id_map.txt").read_text().splitlines() if line.strip())
reps = [line[1:].split()[0] for line in (ALN/"phylo_q2/fs001_subcluster_rep_seq.fasta").read_text().splitlines() if line.startswith(">")]
gc = Counter(genome_of.get(r,"?") for r in reps)
for g, exp in [("PvP01",118),("PvW1",110),("PvPAM",110)]:
    check(f"Q2 sub-reps {g}", exp, gc.get(g,0))
m = re.search(r"Best-fit model according to BIC: ([^\s]+)", (ALN/"phylo_q2/trees/q2_aa.iqtree").read_text())
check("Q2 ModelFinder selected", "VT+F+R6", m.group(1) if m else None)

# ---- Pseudogenes (new) ----
for g, gff, exp in [("PvP01","data/genomes/gff/PvivaxP01.gff",185),
                    ("PvW1","data/genomes/gff/PvivaxPvW1.gff",0),
                    ("PvPAM","data/genomes/gff/PvivaxPAM.gff",322)]:
    n = sum(1 for line in (ROOT/gff).read_text().splitlines()
            if not line.startswith("#") and len(line.split("\t"))>=3 and line.split("\t")[2]=="pseudogene")
    check(f"{g} total pseudogenes in GFF", exp, n)
for g, tbl, exp in [("PvP01","data/pseudogenes/PvP01_pseudo_PF05795.tbl",75),
                    ("PvPAM","data/pseudogenes/PvPAM_pseudo_PF05795.tbl",70)]:
    unique = set()
    with open(ROOT/tbl) as fh:
        for line in fh:
            if line.startswith("#"): continue
            sid = re.sub(r"_frame[+-][0-9]$", "", line.split()[0])
            unique.add(sid)
    check(f"{g} VIR-family pseudogenes by PF05795", exp, len(unique))

# ---- Print report ----
print(f"# Verification Report — pvivax_PIR_characterization.pdf\n")
print(f"Total claims checked: **{len(RESULTS)}**")
n_pass = sum(1 for r in RESULTS if r["status"]=="PASS")
n_fail = sum(1 for r in RESULTS if r["status"]=="FAIL")
print(f"- PASS: **{n_pass}** ({100*n_pass/len(RESULTS):.0f}%)")
print(f"- FAIL: **{n_fail}**")
print("\n| Status | Claim | Expected | Observed |")
print("| --- | --- | --- | --- |")
for r in RESULTS:
    print(f"| {r['status']} | {r['label']} | {r['expected']} | {r['observed']} |")
if n_fail > 0:
    print(f"\n## Failed checks\n")
    for r in RESULTS:
        if r["status"]=="FAIL":
            print(f"- **{r['label']}**: expected {r['expected']}, observed {r['observed']}")
