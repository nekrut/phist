"""Extract top 10 Foldseek cluster sequences into FASTA files for MAFFT alignment."""
import os
from collections import defaultdict

ALIGN_DIR = "data/genomes/alignments"

# 1. Load all VIR sequences
seqs = {}
with open(f"{ALIGN_DIR}/all_vir_combined.fasta") as f:
    sid = None
    for line in f:
        if line.startswith(">"):
            sid = line[1:].split()[0]
            seqs[sid] = []
        else:
            seqs[sid].append(line.strip())
seqs = {k: "".join(v) for k, v in seqs.items()}

# 2. Load Foldseek clusters and sort by size
members_of = defaultdict(list)
with open(f"{ALIGN_DIR}/foldseek_work/vir_struct_cluster_cluster.tsv") as f:
    for line in f:
        rep, mem = line.rstrip().split("\t")
        members_of[rep].append(mem)
reps_sorted = sorted(members_of.keys(), key=lambda r: len(members_of[r]), reverse=True)

# 3. Write top 10 FASTA files
os.makedirs(f"{ALIGN_DIR}/fs_clusters", exist_ok=True)
for i, rep in enumerate(reps_sorted[:10], 1):
    out = f"{ALIGN_DIR}/fs_clusters/FS_{i:03d}_unaligned.fasta"
    with open(out, "w") as f:
        for m in members_of[rep]:
            if m in seqs:
                f.write(f">{m}\n{seqs[m]}\n")
    print(f"FS_{i:03d}: {len(members_of[rep])} members → {out}")
