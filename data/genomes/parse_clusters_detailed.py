import pandas as pd

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

shared_all = df[(df['PvP01'] > 0) & (df['PvW1'] > 0) & (df['PvPAM'] > 0)]
shared_p01_pvw1 = df[(df['PvP01'] > 0) & (df['PvW1'] > 0) & (df['PvPAM'] == 0)]
shared_p01_pvpam = df[(df['PvP01'] > 0) & (df['PvW1'] == 0) & (df['PvPAM'] > 0)]
shared_pvw1_pvpam = df[(df['PvP01'] == 0) & (df['PvW1'] > 0) & (df['PvPAM'] > 0)]

unique_p01 = df[(df['PvP01'] > 0) & (df['PvW1'] == 0) & (df['PvPAM'] == 0)]
unique_w1 = df[(df['PvW1'] > 0) & (df['PvP01'] == 0) & (df['PvPAM'] == 0)]
unique_pam = df[(df['PvPAM'] > 0) & (df['PvP01'] == 0) & (df['PvW1'] == 0)]

print("--- Detailed Subfamily Distribution (N >= 3 members) ---")
print(f"Total subfamilies defined: {len(df)}")
print(f"Universally shared (all 3 genomes): {len(shared_all)}")
print(f"Shared by PvP01 + PvW1 (Asia only): {len(shared_p01_pvw1)}")
print(f"Shared by PvP01 + PvPAM: {len(shared_p01_pvpam)}")
print(f"Shared by PvW1 + PvPAM: {len(shared_pvw1_pvpam)}")
print(f"Unique to PvP01 (Indonesia): {len(unique_p01)}")
print(f"Unique to PvW1 (Thailand): {len(unique_w1)}")
print(f"Unique to PvPAM (Peru): {len(unique_pam)}")

# Print the top 5 largest subfamilies to show as an example
print("\nTop 5 Largest Subfamilies:")
print(df.sort_values('Total', ascending=False).head(5).to_string(index=False))

# Format an output table to write back to notebook
with open("../../results.md", "w") as out:
    out.write("### De Novo VIR Subfamily Distribution\n\n")
    out.write(f"Total *vir* proteins clustered: **{df['Total'].sum()}**\n")
    out.write(f"Total valid subfamilies (N ≥ 3 members): **{len(df)}**\n\n")
    
    out.write("| Distribution | Subfamily Count |\n")
    out.write("| --- | --- |\n")
    out.write(f"| Universally shared (all 3 genomes) | {len(shared_all)} |\n")
    out.write(f"| Shared by PvP01 + PvW1 (Asia only) | {len(shared_p01_pvw1)} |\n")
    out.write(f"| Shared by PvP01 + PvPAM | {len(shared_p01_pvpam)} |\n")
    out.write(f"| Shared by PvW1 + PvPAM | {len(shared_pvw1_pvpam)} |\n")
    out.write(f"| Unique to PvP01 (Indonesia) | {len(unique_p01)} |\n")
    out.write(f"| Unique to PvW1 (Thailand) | {len(unique_w1)} |\n")
    out.write(f"| Unique to PvPAM (Peru) | {len(unique_pam)} |\n\n")
    
    out.write("#### Top 5 Largest Subfamilies\n\n")
    out.write(df.sort_values('Total', ascending=False).head(5).to_markdown(index=False))
