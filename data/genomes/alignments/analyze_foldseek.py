"""
Compare Foldseek (structural) clusters vs MCL (sequence) clusters,
and tabulate per-genome distribution.
"""
import pandas as pd
from collections import defaultdict

ALIGN_DIR = "data/genomes/alignments"
GENOME_DIR = "data/genomes"

# ---- 1. Load Foldseek cluster assignments (rep -> member) ----
foldseek_cluster_of = {}  # member_id -> foldseek_rep
with open(f"{ALIGN_DIR}/foldseek_work/vir_struct_cluster_cluster.tsv") as f:
    for line in f:
        rep, member = line.rstrip().split("\t")
        foldseek_cluster_of[member] = rep

# Foldseek IDs use only the first token of the FASTA header,
# so they match the MCL IDs directly.

# ---- 2. Load MCL cluster assignments ----
mcl_clusters_sorted = []
with open(f"{GENOME_DIR}/vir_clusters.txt") as f:
    for line in f:
        proteins = line.strip().split()
        if len(proteins) >= 3:
            mcl_clusters_sorted.append(proteins)
# Sort by size so Subfamily_1 is the largest (matches Plan A naming)
mcl_clusters_sorted.sort(key=len, reverse=True)
mcl_cluster_of = {}  # member_id -> "Subfamily_N"
for i, c in enumerate(mcl_clusters_sorted, 1):
    for p in c:
        mcl_cluster_of[p] = f"MCL_{i:03d}"

# ---- 3. Load id -> genome mapping ----
genome_of = {}
with open(f"{GENOME_DIR}/id_map.txt") as f:
    for line in f:
        pid, genome = line.rstrip().split("\t")
        genome_of[pid] = genome

# ---- 4. Build per-Foldseek-cluster table ----
# Re-name Foldseek clusters as FS_001..FS_073 ordered by size
fs_members = defaultdict(list)
for member, rep in foldseek_cluster_of.items():
    fs_members[rep].append(member)
fs_reps_sorted = sorted(fs_members.keys(), key=lambda r: len(fs_members[r]), reverse=True)
fs_name_of_rep = {r: f"FS_{i+1:03d}" for i, r in enumerate(fs_reps_sorted)}

rows = []
for rep in fs_reps_sorted:
    name = fs_name_of_rep[rep]
    members = fs_members[rep]
    genome_counts = {"PvP01": 0, "PvW1": 0, "PvPAM": 0}
    mcl_within = defaultdict(int)
    for m in members:
        g = genome_of.get(m, "?")
        if g in genome_counts:
            genome_counts[g] += 1
        mcl_within[mcl_cluster_of.get(m, "unclustered")] += 1
    rows.append({
        "FS_cluster": name,
        "rep_id": rep,
        "size": len(members),
        "PvP01": genome_counts["PvP01"],
        "PvW1": genome_counts["PvW1"],
        "PvPAM": genome_counts["PvPAM"],
        "n_MCL_subfamilies_merged": len(mcl_within),
        "MCL_breakdown": ",".join(f"{k}:{v}" for k,v in sorted(mcl_within.items(), key=lambda x: -x[1]))
    })

df = pd.DataFrame(rows)
df.to_csv(f"{ALIGN_DIR}/foldseek_clusters_summary.tsv", sep="\t", index=False)

# ---- 5. Per-genome distribution summary ----
shared_all = df[(df["PvP01"]>0)&(df["PvW1"]>0)&(df["PvPAM"]>0)]
shared_p01_pvw1 = df[(df["PvP01"]>0)&(df["PvW1"]>0)&(df["PvPAM"]==0)]
shared_p01_pvpam = df[(df["PvP01"]>0)&(df["PvW1"]==0)&(df["PvPAM"]>0)]
shared_pvw1_pvpam = df[(df["PvP01"]==0)&(df["PvW1"]>0)&(df["PvPAM"]>0)]
unique_p01 = df[(df["PvP01"]>0)&(df["PvW1"]==0)&(df["PvPAM"]==0)]
unique_w1 = df[(df["PvW1"]>0)&(df["PvP01"]==0)&(df["PvPAM"]==0)]
unique_pam = df[(df["PvPAM"]>0)&(df["PvP01"]==0)&(df["PvW1"]==0)]

print("=" * 70)
print("FOLDSEEK STRUCTURAL CLUSTERING RESULTS")
print("=" * 70)
print(f"Total VIR proteins:          {df['size'].sum()}")
print(f"Total structural clusters:   {len(df)}")
print(f"Largest cluster:             {df['size'].iloc[0]} members")
print(f"Smallest cluster:            {df['size'].iloc[-1]} members")
print()
print("--- Distribution across genomes ---")
print(f"Universally shared (all 3):       {len(shared_all)}")
print(f"PvP01 + PvW1 only (Asia):         {len(shared_p01_pvw1)}")
print(f"PvP01 + PvPAM only:               {len(shared_p01_pvpam)}")
print(f"PvW1 + PvPAM only:                {len(shared_pvw1_pvpam)}")
print(f"Unique to PvP01 (Indonesia):      {len(unique_p01)}")
print(f"Unique to PvW1 (Thailand):        {len(unique_w1)}")
print(f"Unique to PvPAM (Peru):           {len(unique_pam)}")
print()
print("--- Top 10 largest structural clusters ---")
print(df.head(10).drop(columns=["MCL_breakdown","rep_id"]).to_string(index=False))
print()

# ---- 6. Quantify merging: how many MCL subfamilies got merged into each FS cluster? ----
merge_dist = df["n_MCL_subfamilies_merged"].value_counts().sort_index()
print("--- How many MCL subfamilies merged per FS cluster ---")
print(merge_dist.to_string())
print()
n_merged_fs = (df["n_MCL_subfamilies_merged"] > 1).sum()
print(f"FS clusters that merge >=2 MCL subfamilies: {n_merged_fs} / {len(df)}")
print()

# ---- 7. Generate notebook table ----
import io
buf = io.StringIO()
buf.write("| Distribution | FS Cluster Count |\n")
buf.write("| --- | --- |\n")
buf.write(f"| Universally shared (all 3 genomes) | {len(shared_all)} |\n")
buf.write(f"| Shared by PvP01 + PvPAM | {len(shared_p01_pvpam)} |\n")
buf.write(f"| Shared by PvW1 + PvPAM | {len(shared_pvw1_pvpam)} |\n")
buf.write(f"| Shared by PvP01 + PvW1 (Asia only) | {len(shared_p01_pvw1)} |\n")
buf.write(f"| Unique to PvP01 (Indonesia) | {len(unique_p01)} |\n")
buf.write(f"| Unique to PvW1 (Thailand) | {len(unique_w1)} |\n")
buf.write(f"| Unique to PvPAM (Peru) | {len(unique_pam)} |\n")
with open(f"{ALIGN_DIR}/foldseek_distribution_table.md","w") as f:
    f.write(buf.getvalue())

# ---- 8. Top 10 table for notebook ----
buf = io.StringIO()
buf.write("| FS Cluster | Members | PvP01 | PvW1 | PvPAM | # MCL subfamilies merged |\n")
buf.write("| --- | --- | --- | --- | --- | --- |\n")
for _, r in df.head(10).iterrows():
    buf.write(f"| **{r['FS_cluster']}** | {r['size']} | {r['PvP01']} | {r['PvW1']} | {r['PvPAM']} | {r['n_MCL_subfamilies_merged']} |\n")
with open(f"{ALIGN_DIR}/foldseek_top10_table.md","w") as f:
    f.write(buf.getvalue())

print("Outputs written:")
print(f"  - {ALIGN_DIR}/foldseek_clusters_summary.tsv")
print(f"  - {ALIGN_DIR}/foldseek_distribution_table.md")
print(f"  - {ALIGN_DIR}/foldseek_top10_table.md")

# ---- 9. Member-weighted distribution ----
def members_in(subset):
    return subset["size"].sum() if len(subset) else 0

print()
print("--- Member-weighted distribution (count proteins, not clusters) ---")
total = df["size"].sum()
print(f"Total VIR proteins: {total}")
print(f"In universally-shared clusters:    {members_in(shared_all):>5} ({100*members_in(shared_all)/total:.1f}%)")
print(f"In PvP01+PvPAM-only clusters:      {members_in(shared_p01_pvpam):>5} ({100*members_in(shared_p01_pvpam)/total:.1f}%)")
print(f"In PvW1+PvPAM-only clusters:       {members_in(shared_pvw1_pvpam):>5} ({100*members_in(shared_pvw1_pvpam)/total:.1f}%)")
print(f"In PvP01+PvW1-only clusters:       {members_in(shared_p01_pvw1):>5} ({100*members_in(shared_p01_pvw1)/total:.1f}%)")
print(f"In PvP01-unique clusters:          {members_in(unique_p01):>5} ({100*members_in(unique_p01)/total:.1f}%)")
print(f"In PvW1-unique clusters:           {members_in(unique_w1):>5} ({100*members_in(unique_w1)/total:.1f}%)")
print(f"In PvPAM-unique clusters:          {members_in(unique_pam):>5} ({100*members_in(unique_pam)/total:.1f}%)")
