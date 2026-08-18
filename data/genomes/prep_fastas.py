import os

# 1. Read FASTA
seqs = {}
with open("combined_vir.fasta") as f:
    curr = ""
    for line in f:
        if line.startswith(">"):
            # Only take the first word of the header as the ID
            curr = line.strip()[1:].split()[0]
            seqs[curr] = ""
        else:
            seqs[curr] += line.strip()

# 2. Read Clusters
clusters = []
with open("vir_clusters.txt") as f:
    for line in f:
        c = line.strip().split()
        if len(c) >= 3:
            clusters.append(c)

# Sort by size so Subfamily_1 is the largest
clusters.sort(key=len, reverse=True)

# 3. Write individual FASTAs
os.makedirs("alignments", exist_ok=True)
count_written = 0
for i, c in enumerate(clusters):
    with open(f"alignments/Subfamily_{i+1}_unaligned.fasta", "w") as out:
        for prot in c:
            if prot in seqs:
                out.write(f">{prot}\n{seqs[prot]}\n")
                count_written += 1

print(f"Generated {len(clusters)} unaligned FASTA files containing {count_written} total sequences.")
