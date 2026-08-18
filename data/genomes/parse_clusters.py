import pandas as pd
from collections import Counter

# Load mapping
genome_map = {}
with open("id_map.txt") as f:
    for line in f:
        pid, genome = line.strip().split('\t')
        genome_map[pid] = genome

clusters = []
with open("vir_clusters.txt") as f:
    for i, line in enumerate(f):
        proteins = line.strip().split()
        if len(proteins) < 3: # Ignore singletons/tiny fragments
            continue
            
        counts = {'Cluster': f"Subfamily_{i+1}", 'PvP01': 0, 'PvW1': 0, 'PvPAM': 0, 'Total': len(proteins)}
        
        for prot in proteins:
            genome = genome_map.get(prot)
            if genome:
                counts[genome] += 1
                
        clusters.append(counts)

df = pd.DataFrame(clusters)
df = df.sort_values('Total', ascending=False)

print(df.head(20).to_string(index=False))

print("\n--- Summary ---")
print(f"Total valid subfamilies (N >= 3): {len(df)}")
print("Distribution of universally shared vs continent-specific subfamilies:")

shared_all = df[(df['PvP01'] > 0) & (df['PvW1'] > 0) & (df['PvPAM'] > 0)]
print(f"Subfamilies present in all 3 genomes: {len(shared_all)}")

unique_p01 = df[(df['PvP01'] > 0) & (df['PvW1'] == 0) & (df['PvPAM'] == 0)]
unique_w1 = df[(df['PvW1'] > 0) & (df['PvP01'] == 0) & (df['PvPAM'] == 0)]
unique_pam = df[(df['PvPAM'] > 0) & (df['PvP01'] == 0) & (df['PvW1'] == 0)]

print(f"Subfamilies strictly unique to PvP01 (Indonesia): {len(unique_p01)}")
print(f"Subfamilies strictly unique to PvW1 (Thailand): {len(unique_w1)}")
print(f"Subfamilies strictly unique to PvPAM (Peru): {len(unique_pam)}")

