## Literature Review: PIR/PHIST Tandem Expansions in *Plasmodium vivax*

This review focuses on literature from the past 10 years discussing the evolutionary genomics and pathogenesis of the PIR (including the *P. vivax*-specific VIR) and PHIST gene families. These multigene families are predominantly located in subtelomeric regions and are crucial for parasite immune evasion, host cell remodeling, and cytoadherence.

### Key Papers & Summaries

*   **[A new Plasmodium vivax reference sequence with improved assembly of the subtelomeres reveals an abundance of pir genes](https://pubmed.ncbi.nlm.nih.gov/28008421/)** (2016)
    *   **Summary:** Long-read sequencing technologies were used to generate a highly contiguous *P. vivax* genome (P01). By accurately resolving the highly repetitive subtelomeric regions—which are notoriously difficult to sequence—the authors revealed a massive, previously underestimated tandem expansion of *pir* (*vir* in *P. vivax*) genes. This structural variation is central to the parasite's evolutionary genomics and capacity for antigenic variation.
    
*   **[Comparative clinical transcriptome of pir genes in severe Plasmodium vivax malaria](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0013342)** (2024/2025)
    *   **Summary:** This study directly links the *vir* (*pir* superfamily) multigene family to severe *P. vivax* malaria pathogenesis. Through comparative clinical transcriptomics, the researchers demonstrated that the expression of these expanded genes mediates the parasite's capacity for immune system escape and cytoadherence, which exacerbates disease severity.

*   **[The Plasmodium PHIST and RESA-Like Protein Families of Human and Rodent Malaria Parasites](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152510&type=printable)** (2016)
    *   **Summary:** This comparative genomic analysis tracks the expansion of the PHIST (*Plasmodium* helical interspersed subtelomeric) gene family across the genus. It highlights how human-infective parasites exhibit massive expansions (e.g., up to 65 paralogs) compared to rodent malaria models, suggesting a specialized evolutionary role in modifying the human erythrocyte during pathogenesis.

*   **[Plasmodium vivax-like genome sequences shed new insights into Plasmodium vivax biology and evolution](https://pubmed.ncbi.nlm.nih.gov/30142149/)** (2018)
    *   **Summary:** By sequencing the closest genetic relative of *P. vivax* (found in African great apes), this study unravels the evolutionary history and host adaptation pathways of the parasite. It emphasizes how lineage-specific expansions of variant surface antigens, including the PIR/VIR families, drove the successful adaptation of *P. vivax* to human hosts.

*   **[De novo assembly of plasmodium interspersed repeat (pir) genes from Plasmodium vivax RNAseq data suggests geographic conservation of sub-family transcription](https://www.crick.ac.uk/research/publications/de-novo-assembly-of-plasmodium-interspersed-repeat-pir-genes-from-plasmodium-vivax-rnaseq-data-suggests-geographic-conservation-of-sub-family-transcription)** (2019)
    *   **Summary:** The authors bypassed the limits of incomplete reference genomes by assembling *pir* transcripts *de novo* from field isolates. They found that despite the rapid evolution and expansion of the *pir* gene family, specific sub-families exhibit geographically conserved transcriptional profiles, pointing to constrained, essential roles in *P. vivax* pathogenesis worldwide.

*   **[Differential Trafficking and Expression of PIR Proteins in Acute and Chronic Plasmodium Infections](https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2022.877253/full)** (2022)
    *   **Summary:** Focusing on the mechanistic role of the PIR protein family during pathogenesis, this paper explores how differential expression and cellular trafficking of these expanded proteins change between acute and chronic infection stages. While using a rodent model, the findings provide crucial functional context for the massive *pir* tandem expansions seen in *P. vivax*.

*   **[Structural and functional insights from detailed computational analysis of Plasmodium repetome](https://link.springer.com/article/10.1007/s12041-025-01516-x)** (2025)
    *   **Summary:** This recent paper conducts a wide computational survey of tandem repeats across *Plasmodium* proteomes, identifying *P. vivax* as exceptionally rich in these structural features. It discusses how the evolutionary expansion of tandem repeats in multigene families likely contributes to structural protein variations crucial for host-pathogen interactions and immune evasion.

*   **[Structure of the Plasmodium-interspersed repeat proteins of the malaria parasite](https://pubmed.ncbi.nlm.nih.gov/33257570/)** (Harrison & Higgins et al., 2020, *PNAS*)
    *   **Summary:** First crystal structure of a PIR ectodomain (PDB: [6ZYV](https://www.rcsb.org/structure/6ZYV)), solved from *Plasmodium chabaudi chabaudi*. Despite extreme sequence divergence between PIR family members (often <30% identity), all PIRs share a single conserved structural scaffold. This work established that the PIR superfamily is structurally unified even when sequence-based homology searches cannot detect the relationship — a critical observation that motivates the use of structure-aware clustering methods (e.g., Foldseek + ProstT5) for classifying PIR/VIR repertoires.

### Methods papers used in this analysis

The two methods papers below are not about PIR/PHIST biology, but they are the methodological foundation for the structural clustering and structural phylogenetics carried out in this notebook (Plans B and C). They are listed here so the citations live alongside the rest of the literature.

*   **[Multiple Protein Structure Alignment at Scale with FoldMason](https://www.science.org/doi/10.1126/science.ads6733)** (Gilchrist, Mirdita & Steinegger, 2026, *Science*; doi:10.1126/science.ads6733)
    *   **Summary:** Introduces FoldMason, a progressive multiple structural alignment method that produces AA and 3Di alignments in lockstep using a guide tree built from all-versus-all Foldseek pairwise comparisons. The paper benchmarks the alignment quality against HOMSTRAD and demonstrates structure-based phylogenetic reconstruction on Mifsud et al.'s (2024) Flaviviridae E, E1, and E2 glycoprotein families, recovering manually-curated reference phylogenies with high quartet similarity. The glycoprotein replication is the procedure we mirrored for our VIR phylogenetic analysis (Plan C): FoldMason MSTA → trimAl → ModelFinder + IQ-TREE 2 with 1000 UFBoot replicates, repeated for AA-only, 3Di-only, and partitioned AA+3Di.

*   **[A general substitution matrix for structural phylogenetics](https://doi.org/10.1093/molbev/msaf124)** (Garg & Hochberg, 2025, *Mol. Biol. Evol.* 42:msaf124)
    *   **Summary:** Provides the 3Di amino acid substitution matrix used by both the FoldMason paper and our Plan C trees for the 3Di-only and partitioned analyses. Without a dedicated substitution model, the 3Di alphabet would have to be treated as a generic 20-letter protein code, which loses much of the structural signal. The matrix is distributed in NEXUS format and is loaded into IQ-TREE via the `-mdef` flag.

---

## Gene and Protein Structures

### PIR (Plasmodium Interspersed Repeat) / VIR
* **Sub-classification:** The *pir* family is highly diverse and is historically subdivided into **distinct subfamilies**. In *P. vivax*, *vir* genes were initially grouped into subfamilies **A through L** (and later expanded/reclassified) based on sequence homology. Similarly, in rodent malarias, *pir* genes are grouped into "S" (short) and "L" (long) groups, each containing distinct numerical subfamilies (e.g., S1-S8, L1-L4). Recent transcriptomic studies show that specific subfamilies are expressed at different stages of infection, suggesting distinct functional roles.
* **Copy Number:** *pir* is the largest multigene family in *Plasmodium*. In *P. vivax*, it has undergone a massive tandem expansion. While the older, short-read Salvador I reference genome identified ~346 *vir* genes, modern long-read assemblies (like the P01 reference) that accurately resolve the highly repetitive subtelomeres have revealed **over 1,000 *vir* copies** per haploid genome.
* **Gene Structure:** The *pir* genes typically share a highly conserved three-exon structure across different *Plasmodium* species:
  * **Exon 1:** A short sequence that encodes a signal peptide, directing the protein into the secretory pathway.
  * **Exon 2:** A long, highly variable exon encoding the bulk of the extracellular domain (ectodomain) responsible for antigenic variation.
  * **Exon 3:** Encodes the transmembrane domain and a short cytoplasmic tail, anchoring the protein to membranes.
* **Protein Structure:** Recent structural biology (e.g., Harrison & Higgins, 2020) resolved the *pir* ectodomain, showing that despite immense sequence variation, the proteins maintain a conserved structural fold. The core consists of beta-strands and alpha-helices organized into a unique scaffold that can tolerate massive amino acid substitutions. This allows the parasite to continuously change its surface "appearance" to immune cells while keeping the protein structurally sound.
* **Function:** VIR/PIR proteins are exported to the surface of the infected red blood cell. By constantly switching which *vir* variants are expressed, the parasite evades the host’s humoral (antibody) immune response. They also play major roles in cytoadherence (making infected red blood cells sticky so they attach to the host's endothelium and avoid clearance in the spleen) and rosetting (binding uninfected red blood cells). In *P. vivax*, *vir* genes are heavily implicated in severe malaria pathogenesis by enabling the parasite to establish chronic, stealthy infections.

### PHIST (Plasmodium Helical Interspersed Subtelomeric)
* **Sub-classification:** Based on amino acid composition, sequence homology, and overall gene architecture, the PHIST family is formally divided into three distinct subgroups: **PHISTa**, **PHISTb**, and **PHISTc** (with some additional "PHIST-like" or "PHIST-RESA" outliers). These subgroups differ in the length of the protein flanking the core PHIST domain and the specific host cytoskeleton targets they bind to.
* **Copy Number:** This family exhibits significant lineage-specific expansion in human and primate malarias compared to rodent models. There are roughly **39 *phist* genes in *P. vivax*** and **~65-72 copies in *P. falciparum***. By stark contrast, rodent malaria models (like *P. berghei* or *P. yoelii*) possess severely contracted families, containing only 1 to 3 copies.
* **Gene Structure:** Like many *Plasmodium* exported protein families, *phist* genes are primarily located in the hyper-recombinogenic subtelomeric regions and typically share a conserved **two-exon structure**:
  * **Exon 1:** A short sequence that encodes a hydrophobic signal peptide for initial entry into the parasite's secretory pathway.
  * **Exon 2:** A much larger exon that usually begins with a *Plasmodium* Export Element (PEXEL) motif—a targeting signal to export the protein into the host erythrocyte—followed by the sequence encoding the defining PHIST domain and the rest of the protein.
* **Protein Structure:** The defining feature of PHIST proteins is the **PHIST domain**, a conserved region of approximately 150 amino acids. Structurally, this domain consists of four consecutive alpha-helices with conserved aromatic residues. The domain itself does not possess known enzymatic activity; rather, it acts as a critical protein-protein interaction module.
* **Function:** PHIST proteins are essentially the "scaffold builders" and "anchors" inside the infected human red blood cell. Once exported, they localize to the host cell cytoskeleton or to membranous structures called Maurer's clefts. Their primary function is to remodel the host cell. Crucially, they bind to major virulence factors (like PfEMP1 in *P. falciparum* or its equivalents) and anchor them securely to the red blood cell's cytoskeleton (specifically interacting with human host proteins like band 4.1R). Without PHIST proteins securely anchoring these surface antigens, the infected red blood cell cannot properly adhere to blood vessel walls, drastically reducing the parasite's virulence.

---

## Gene Counts Across High-Quality *P. vivax* Reference Genomes

Recent highly contiguous genome assemblies have fundamentally changed our understanding of the scale of subtelomeric multigene families. The table below summarizes the number of functional genes annotated for the PIR (VIR) and PHIST families in the three most prominent modern reference assemblies.

| Reference Genome | Geography / Origin | Technology | PIR / VIR count | PHIST count |
| --- | --- | --- | --- | --- |
| **PvP01** (GCA_900093555.2) | Papua, Indonesia | Illumina (deep) | ~1,219 | 39 |
| **PvW1** (GCA_914969965.1) | Thailand | Hybrid (PacBio + Illumina) | 1,145 | ~39 |
| **PvPAM** (GCA_949152365.1) | Peruvian Amazon | PacBio | 975 | ~39 |

*Note: The older, highly fragmented Salvador-I (Sanger sequencing) reference only captured ~346 VIR genes. The counts above represent fully annotated, functional genes (excluding pseudogenes, which add an additional ~100-116 copies per assembly). These counts reflect the author-submitted, specialized *Companion* annotations mirrored across both PlasmoDB and NCBI's GenBank records (NCBI's automated RefSeq pipeline historically struggles with these hyper-repetitive regions). Notably, in PvPAM, over 600 of its VIR genes share no direct orthology with PvP01, highlighting the massive geographic diversity of these subtelomeric expansions.*

---

### *De Novo* VIR Subfamily Distribution Across Continents

Because the classical 12 subfamilies (A-L) were defined using the highly fragmented ~346 genes of the Salvador-I genome, attempting to force the >1,000 VIR genes from modern long-read assemblies back into that framework results in massive amounts of "unclustered" or misclassified genes. 

To overcome this, a network-based approach (all-vs-all sequence clustering using MMseqs2 and Markov Clustering) was executed combining all VIR proteins from PvP01 (Indonesia), PvW1 (Thailand), and PvPAM (Peru) into a single pool to define subfamilies *de novo*. 

**Results from 2,592 clustered VIR proteins:**
* **Total valid subfamilies (N ≥ 3 members) defined:** 146

| Distribution | Subfamily Count |
| --- | --- |
| Universally shared (all 3 genomes) | 132 |
| Shared by PvP01 + PvPAM | 6 |
| Shared by PvW1 + PvPAM | 5 |
| Shared by PvP01 + PvW1 (Asia only) | 3 |
| Strictly unique to one genome | 0 |

#### Top 5 Largest Universal Subfamilies

| Cluster | PvP01 (Indonesia) | PvW1 (Thailand) | PvPAM (Peru) | Total Genes |
| --- | --- | --- | --- | --- |
| **Subfamily_1** | 72 | 56 | 63 | 191 |
| **Subfamily_2** | 42 | 69 | 71 | 182 |
| **Subfamily_3** | 61 | 51 | 49 | 161 |
| **Subfamily_4** | 50 | 24 | 52 | 126 |
| **Subfamily_5** | 44 | 26 | 48 | 118 |

#### Interpretation of Clustering Results

1.  **Massive Universal Conservation of Core Subfamilies:** Despite the intense geographic diversity and constant ectopic recombination in the subtelomeres, the structural framework of the VIR family is incredibly well-preserved across continents. Out of the 146 defined subfamilies, an overwhelming **132 (90.4%) are universally shared** across Indonesian, Thai, and Peruvian isolates.
2.  **No Truly "Endemic" Subfamilies:** Notably, there were **zero** subfamilies strictly unique to any single genome. Even when a subfamily wasn't universal, it was shared by at least two of the three isolates. This suggests that while individual *vir* genes rapidly duplicate, mutate, and delete (resulting in the poor 1-to-1 orthology often reported between isolates), they do so strictly within the evolutionary boundaries of these ancient, pre-established universal sub-clusters.
3.  **Proportional Expansion:** Looking at the largest subfamilies (e.g., Subfamily 1 through 5), the expansion is not driven by one genome massively amplifying a single cluster. The tandem expansions are proportional; if Subfamily 1 is the largest in PvP01, it is also generally the largest in PvW1 and PvPAM. This implies that the functional roles performed by these specific larger subfamilies are essential to *P. vivax* survival globally, regardless of the local host population or vector species.

## Plan F: Progressive Galaxy UDT Replication [galaxy]

Replicate the complete structure-aware analysis of the P. vivax PIR family on the Galaxy server. In this progressive workflow, we will upload the core reference genomes and proteomes first, establish our functional PIR baseline using standard ToolShed HMMER search, and then iteratively construct, register, and execute the custom User-Defined Tools (UDTs) one-by-one in-line with the analysis.

### Steps

- [x] 1. **Upload input datasets to Galaxy** {#plan-f-step-1} — upload genomes, proteomes, GFFs, Pfam HMM, and 3Di substitution matrix
  - Routing: galaxy
  - Tool: upload1
  - Verification: All 9 core datasets successfully uploaded to history `phist2` (ID: `bbd44e69cb8906b5c0a92f1d9b046fdd`) in 'ok' state under user `aun1` (API key updated).
- [x] 2. **Run functional HMMER screens** {#plan-f-step-2} — screen annotated functional proteomes with HMMER hmmsearch to isolate PIRs
  - Routing: galaxy
  - Tool: toolshed.g2.bx.psu.edu/repos/iuc/hmmer_hmmsearch/hmmer_hmmsearch/3.4+galaxy0
  - Verification: Functional HMMER screens successfully completed on Galaxy server.
    - PvP01: Job `bbd44e69cb8906b55b0db82a3efbc7f4` | HDA `f9cad7b01a47213517257c118cf859c4` | Hits: 931 (100% verified using EXACT local parameters: `-E 1e-05 --domE 10.0 --incE 0.01 --incdomE 0.01`)
    - PvW1: Job `bbd44e69cb8906b593b33af9bc0ab803` | HDA `f9cad7b01a47213577f2be61176efc13` | Hits: 748 (100% verified using EXACT local parameters: `-E 1e-05 --domE 10.0 --incE 0.01 --incdomE 0.01`)
    - PvPAM: Job `bbd44e69cb8906b5df1dc3c283fcfc02` | HDA `f9cad7b01a4721356683494554be2a85` | Hits: 985 (100% verified using EXACT local parameters: `-E 1e-05 --domE 10.0 --incE 0.01 --incdomE 0.01`)
- [x] 3. **Register and run Pseudogene Extractor UDT** {#plan-f-step-3} — create and run the GFF six-frame translation UDT
  - Routing: galaxy
  - Tool: galaxy_create_user_tool + galaxy_run_user_tool (gff_pseudogene_translator)
  - Verification: Registered and executed custom GFF pseudogene translation workflow under hybrid routing.
    - UDT Registered: `anton-1-gff_pseudogene_translator` (UUID: `95e36567-3eab-4af9-94b2-6cb032276707`) with generic name `"GFF Pseudogene Extractor & Translator (1 Core)"` and detailed help markdown.
    - Local translations completed (PvP01: 1,110 translations, PvPAM: 1,932 translations).
    - Uploaded PvP01 translation FASTA to Galaxy -> HDA `f9cad7b01a472135f0fceec9b2aeb6ef` (State: `ok`)
    - Uploaded PvPAM translation FASTA to Galaxy -> HDA `f9cad7b01a4721357f11432add5e1c74` (State: `ok`)
    - Native BioContainers UDT registered as version 1.0.2 with container `quay.io/biocontainers/python:3.12.12`, UUID `ffcf2418-7b0f-4f6c-93ef-6c9e34ae5d40`, output binding `from_work_dir: translated_pseudogenes.fasta`.
    - BioContainers UDT outputs reached `ok`: PvP01 HID 46 / HDA `f9cad7b01a4721359c223f5fa5d69e8c` with 1,110 sequences; PvPAM HID 47 / HDA `f9cad7b01a47213574689e772059517e` with 1,932 sequences.
    - Verification caveat: BioContainers UDT FASTA record IDs/counts matched local outputs, but translated sequences were not byte-identical because the script uses nondeterministic `sorted(set(exons), key=lambda e: e[1])` ordering when transcript and exon records share a start coordinate. A deterministic tie-break is needed before this UDT can be considered an exact local reproduction.
- [ ] 4. **Run pseudogene HMMER screen** {#plan-f-step-4} — screen pseudogene translations with HMMER hmmsearch on the server
  - Routing: galaxy
  - Tool: toolshed.g2.bx.psu.edu/repos/iuc/hmmer_hmmsearch/hmmer_hmmsearch/3.4+galaxy0
  - Verification: verify the final HMMER outputs yield exactly 75 PvP01 and 70 PvPAM unique pseudogenic transcript hits
    - Attempt using BioContainers UDT FASTAs completed on Galaxy with HMMER `hmmsearch` 3.4+galaxy0 and local pseudogene search settings: `-E 1e-3 --domE 10.0`, default inclusion thresholds, `--seed 42`.
    - PvP01 outputs: HIDs 48-50; per-sequence tblout HDA `f9cad7b01a4721357a326a7fd1a5b7d6`; state `ok`; 107 translated-frame hits collapsing to 72 unique pseudogenic transcript loci.
    - PvPAM outputs: HIDs 51-53; per-sequence tblout HDA `f9cad7b01a47213511d2aa7264403c21`; state `ok`; 91 translated-frame hits collapsing to 75 unique pseudogenic transcript loci.
    - Verification result: mismatch relative to local expected 75 PvP01 and 70 PvPAM loci. Step remains pending until the UDT translation ordering is made deterministic and Step 4 is rerun.
    - Follow-up rerun using the previously uploaded verified Step 3 fallback FASTAs completed on Galaxy: PvP01 FASTA HDA `f9cad7b01a472135f0fceec9b2aeb6ef`; PvPAM FASTA HDA `f9cad7b01a4721357f11432add5e1c74`.
    - Fallback PvP01 HMMER outputs: HIDs 54-56; per-sequence tblout HDA `f9cad7b01a472135d491d831288295f7`; state `ok`; 109 translated-frame hits collapsing to 75 unique pseudogenic transcript loci. This matches the expected PvP01 locus count.
    - Fallback PvPAM HMMER outputs: HIDs 57-59; per-sequence tblout HDA `f9cad7b01a472135b098eb058958d668`; state `ok`; 87 reported rows, but only 69 unique pseudogenic transcript loci in the unfiltered Galaxy report and 65 unique loci when considering only full-sequence E-values <= 1e-3. This does not reproduce the expected PvPAM count of 70.
    - Diagnostic result: Galaxy input HMM, GFF, genome FASTA, and fallback pseudogene FASTA files are byte-identical to their local counterparts. Re-running local HMMER 3.4 on the current PvPAM FASTA gives 65 loci, while the older checked-in local table `data/pseudogenes/PvPAM_pseudo_PF05795.tbl` gives 70 loci. Therefore the PvPAM baseline table is stale relative to the current translation FASTA/HMMER 3.4 toolchain; Step 4 remains pending rather than complete.
- [x] 5. **Register and run Foldseek Clustering UDT** {#plan-f-step-5} — create and run Foldseek+ProstT5 structural clustering UDT
  - Routing: galaxy
  - Tool: galaxy_create_user_tool + galaxy_run_user_tool (`anton-gpu-xl-foldseek_prostt5_clustering`)
  - Verification: accepted Galaxy GPU branch completed successfully using UDT v1.0.5 UUID `43fa451a-3592-4cfa-80ea-c9f7d1afb772`, input FASTA HID 115, `--gpu 1`, `threads=8`, coverage `0.8`, E-value `0.001`, and alignment type `2`. Outputs HIDs 121-125 are `ok`; the run produced 76 GPU-mode Foldseek clusters from 2,592 proteins, with GPU FS_001 containing 812 members. This differs from the local CPU baseline (73 clusters; FS_001=1,197), but the user explicitly accepted the GPU result as the Galaxy branch.
- [x] 6. **Register and run FoldMason Alignment UDT** {#plan-f-step-6} — down-sample GPU FS_001 and run progressive structural alignment UDT
  - Routing: galaxy
  - Tool: toolshed.g2.bx.psu.edu/repos/iuc/mmseqs2_easy_linclust_clustering/mmseqs2_easy_linclust_clustering/17-b804f+galaxy1 + galaxy_create_user_tool + galaxy_run_user_tool (`anton-32-foldmason_align`)
  - Verification: GPU FS_001 extraction verified 812 sequences; MMseqs2 downsampling verified 336 representatives; ProstT5-enabled FoldMason UDT v1.0.3 UUID `b9cc1615-2ced-4868-8506-661afbf2d876` using container `quay.io/nekrut/foldmason-prostt5:4.dd3c235-cpu` completed with AA alignment HID 154, 3Di alignment HID 155, guide tree HID 156, and log HID 157 all `ok`. Downloaded AA and 3Di alignments each contain 336 sequences with uniform 10,128-column length and matching sequence IDs; guide tree is non-empty.
- [x] 7. **Register and run Microsynteny Orthology UDT** {#plan-f-step-7} — create and run flanking synteny scoring UDT
  - Routing: galaxy
  - Tool: galaxy_create_user_tool + galaxy_run_user_tool (`anton-1-step7_prepare_fastas`, `anton-8-mmseqs_easy_rbh_pair`, `anton-1-microsynteny_filter`)
  - Verification: GPU-branch Step 7 completed with verified inputs and outputs. GPU FS_001 split produced 234 PvW1 and 306 PvPAM sequences; MMseqs2 RBH produced 141 GPU FS_001 PvW1-PvPAM RBH pairs and 5,120 housekeeping RBH pairs; microsynteny scoring produced 3 high-confidence, 10 medium-confidence, and 128 low-confidence ortholog candidates. Counts differ from the local CPU FS_001 branch (11 high, 26 medium) because the accepted GPU Foldseek branch has different FS_001 membership.
- [x] 8. **Register and run Spatial Analysis UDT** {#plan-f-step-8} — create and run coordinate profiling and permutation testing UDT
  - Routing: galaxy
  - Tool: galaxy_create_user_tool + galaxy_run_user_tool (`anton-1-spatial_analysis`)
  - Verification: final UDT v1.0.2 using verified VIR ID lists and the local top-14 VIR-bearing-contig rule produced all 2,664 functional VIR/PIR coordinates, main-contig counts matching the local baseline (PvP01 347, PvW1 634, PvPAM 735), overall outer-10% subtelomeric enrichment of 64.45%, and only 3/22 tandem tests with p < 0.05. Outputs HIDs 193-199 are `ok` and downloaded/parsed under `galaxy_step8/final/`.
- [ ] 9. **Infer phylogenies via ToolShed IQ-TREE** {#plan-f-step-9} — run IQ-TREE on structural alignments
  - Routing: galaxy
  - Tool: toolshed.g2.bx.psu.edu/repos/iuc/iqtree/iqtree/2.4.0+galaxy2
  - Verification: retrieve Newick trees and verify Q2 parsimony score matches the local baseline of 160 transitions

### Parameters

| Step | Tool / UDT ID | Parameter | Default | Value | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2** | `hmmsearch` | `-E` (Sequence E-value) | `10.0` | **1e-5** | E-value threshold to define functional PIRs |
| **2** | `hmmsearch` | `--domE` (Domain E-value) | `10.0` | **1e-5** | Domain E-value threshold for functional hits |
| **2** | `hmmsearch` | `--incE` (Sequence inclusion) | `0.01` | **1e-5** | Inclusion threshold for sequence reporting |
| **2** | `hmmsearch` | `--incdomE` (Domain inclusion) | `0.01` | **1e-5** | Inclusion threshold for domain reporting |
| **3** | `gff_pseudogene_translator` | `min_len` | `50` | **50** | Minimum amino acid length of translated fragments |
| **4** | `hmmsearch` | `-E` (Sequence E-value) | `10.0` | **1e-3** | E-value threshold for pseudogene search |
| **4** | `hmmsearch` | `--domE` (Domain E-value) | `10.0` | **10.0** | Domain E-value threshold for pseudogenes; matches local run default/explicit Galaxy setting |
| **5** | `foldseek_clustering` | `-c` (Coverage) | `0.0` | **0.8** | Minimum mutual coverage required for clustering |
| **5** | `foldseek_clustering` | `-e` (E-value) | `0.001` | **0.001** | Maximum E-value threshold for pairwise search |
| **5** | `foldseek_clustering` | `--alignment-type` | `2` | **2** | Uses dual alignment scoring (3Di + amino acid) |
| **5** | `foldseek_clustering` | `--cov-mode` | `0` | **0** | Bidirectional coverage mode (coverage of query & target) |
| **6** | `mmseqs_clustering` | `--min-seq-id` | `0.0` | **0.5** | Sequence identity ceiling for down-sampling FS_001 |
| **6** | `mmseqs_clustering` | `-c` (Coverage) | `0.0` | **0.8** | Mutual alignment coverage for down-sampling |
| **6** | `foldmason_align` | `--alignment-type` | `2` | **2** | Progressive structural alignment using 3Di+AA |
| **6** | `trimal` | `-gt` (Gap threshold) | `0.0` | **0.65** | Fraction of sequences with non-gap characters to retain column |
| **7** | `mmseqs_rbh` (FS_001) | `--min-seq-id` | `0.0` | **0.3** | Minimum sequence identity for FS_001 RBH |
| **7** | `mmseqs_rbh` (FS_001) | `-c` (Coverage) | `0.0` | **0.5** | Minimum alignment coverage for FS_001 RBH |
| **7** | `mmseqs_rbh` (FS_001) | `-e` (E-value) | `0.001` | **1e-5** | E-value threshold for FS_001 RBH |
| **7** | `mmseqs_rbh` (HK Core) | `--min-seq-id` | `0.0` | **0.5** | Minimum sequence identity for housekeeping RBH |
| **7** | `mmseqs_rbh` (HK Core) | `-c` (Coverage) | `0.0` | **0.8** | Minimum alignment coverage for housekeeping RBH |
| **7** | `mmseqs_rbh` (HK Core) | `-e` (E-value) | `0.001` | **1e-10** | E-value threshold for housekeeping RBH |
| **7** | `microsynteny_filter` | `neighborhood_radius` | `2` | **2** | Number of upstream/downstream non-VIR genes checked |
| **8** | `spatial_analysis` | `permutations` | `100` | **500** | Label shuffling iterations for NN tandem clustering test |
| **9** | `iqtree` | `-B` (UFBoot) | `1000` | **1000** | Number of Ultrafast Bootstrap replicates |
| **9** | `iqtree` | `-alrt` (SH-aLRT) | `1000` | **1000** | Number of SH-aLRT replicates |
| **9** | `iqtree` | `--bnni` | (off) | **(on)** | BNNI optimization of bootstrap trees |
| **9** | `iqtree` | `--seed` | (random) | **42** | Fixes random seed for absolute reproducibility |

```loom-session
id: 019e69c0-67e9-7f75-9b6b-352498f84e69
started_at: 2026-05-27T14:06:08.021Z
ended_at: 2026-07-31T17:43:05.829Z
notebook: notebook.md
orphaned_active_steps: 0
```

---

## Plan B: Structure-Aware VIR Classification with Foldseek + ProstT5 [local]

Re-classify the 2,592 *P. vivax* VIR proteins using structure-aware clustering. Generate the 3Di structural alphabet directly from sequence via ProstT5 (no folding required), then cluster with Foldseek to capture homology relationships that the prior sequence-based MMseqs2 + MCL pipeline (Plan A) likely missed. Harrison & Higgins (2020) demonstrated PIRs share a unified structural fold despite extreme sequence divergence — this clustering approach should consolidate divergent VIR variants that sequence-based methods cannot link.

### Steps

- [x] 1. **Install Foldseek and download ProstT5 weights** {#plan-b-step-1} — Add Foldseek to the local conda env and fetch ProstT5 model weights via `foldseek databases ProstT5`
  - Routing: local
  - Tool: conda, foldseek databases
  - Verification: confirm `foldseek easy-cluster --help` runs and ProstT5 weights directory exists with model files
- [x] 2. **Structure-aware clustering with ProstT5** {#plan-b-step-2} — Run `foldseek easy-cluster` directly on `all_vir_combined.fasta` using `--prostt5-model` to encode sequences into 3Di on-the-fly, then cluster using 3Di+AA combined alignment
  - Routing: local
  - Tool: foldseek easy-cluster
  - Verification: confirm `result_cluster.tsv` and `result_rep_seq.fasta` exist; count clusters and representatives
- [x] 3. **Compare structural vs sequence clusters** {#plan-b-step-3} — Cross-tabulate the new Foldseek clusters against the prior 146 MCL subfamilies to identify (a) which MCL subfamilies merge under structural clustering and (b) which split
  - Routing: local
  - Tool: python / pandas
  - Verification: produce contingency table and identify merged/split clusters
- [x] 4. **Distribution analysis across genomes** {#plan-b-step-4} — Tabulate how the new structural subfamilies are distributed across PvP01, PvW1, PvPAM (same analysis as Plan A step 5)
  - Routing: local
  - Tool: python / pandas
  - Verification: generate summary table comparable to the sequence-based Plan A result

### Parameters (changes from Foldseek defaults)

| Step | Tool | Parameter | Default | Value | Description |
| --- | --- | --- | --- | --- | --- |
| 2 | foldseek easy-cluster | `-c` | 0.0 | 0.8 | Min mutual coverage (full-length VIRs, not fragments) |
| 2 | foldseek easy-cluster | `-e` | 10.0 | 0.001 | Tighter E-value to reduce false-positive structural matches |
| 2 | foldseek easy-cluster | `--threads` | 10 | 8 | Use 8 of 10 cores (leave 2 for OS) |
| 2 | foldseek easy-cluster | `--prostt5-model` | (empty) | `./prostt5_weights` | Path to ProstT5 weights (encodes FASTA → 3Di on-the-fly) |
| 2 | foldseek easy-cluster | `--alignment-type` | 2 | 2 | 3Di+AA combined alignment (most sensitive; explicit for the record) |

All other ~60 parameters remain at Foldseek's well-tuned defaults.

### Plan B Results: Structural Clustering Reveals Deep Fold Conservation

Foldseek + ProstT5 collapsed the **2,592 VIR proteins** into **73 structural clusters** — half the number found by sequence-based MCL (146). This confirms the prediction from Harrison & Higgins (2020) that the PIR superfamily is structurally unified beyond the reach of sequence-based homology detection.

#### Cluster-count distribution

| Distribution | FS Cluster Count |
| --- | --- |
| Universally shared (all 3 genomes) | 21 |
| Shared by PvP01 + PvPAM | 3 |
| Shared by PvW1 + PvPAM | 1 |
| Shared by PvP01 + PvW1 (Asia only) | 1 |
| Unique to PvP01 (Indonesia) | 27 |
| Unique to PvW1 (Thailand) | 9 |
| Unique to PvPAM (Peru) | 11 |

#### Member-weighted distribution (much more informative)

The cluster-count view above suggests >60% of structural clusters are genome-specific, but those are almost all tiny singletons. When weighted by membership:

| Distribution | Proteins | % of total |
| --- | --- | --- |
| In universally-shared structural clusters | 2,523 | **97.3%** |
| In genome-pair-shared clusters | 17 | 0.7% |
| In genome-unique clusters | 52 | 2.0% |

**~97% of all VIR proteins fall into structural folds shared across all three continents.** The 47 "unique" clusters are mostly singletons that may represent annotation noise, recently emerged variants, or genuine lineage-specific structural innovations.

#### Top 10 largest structural clusters

| FS Cluster | Members | PvP01 | PvW1 | PvPAM | # MCL subfamilies merged |
| --- | --- | --- | --- | --- | --- |
| **FS_001** | 1197 | 400 | 349 | 448 | **89** |
| **FS_002** | 385 | 126 | 101 | 158 | 36 |
| **FS_003** | 248 | 77 | 78 | 93 | 32 |
| **FS_004** | 143 | 53 | 41 | 49 | 20 |
| **FS_005** | 136 | 48 | 37 | 51 | 22 |
| **FS_006** | 96 | 28 | 33 | 35 | 7 |
| **FS_007** | 85 | 39 | 20 | 26 | 16 |
| **FS_008** | 74 | 31 | 18 | 25 | 24 |
| **FS_009** | 53 | 20 | 16 | 17 | 13 |
| **FS_010** | 36 | 15 | 7 | 14 | 6 |

**`FS_001` alone contains 1,197 proteins (46% of the entire VIR repertoire across all three genomes) and absorbs 89 of Plan A's 146 sequence-based subfamilies.** This is the dominant PIR structural class predicted by Harrison & Higgins (2020).

#### Comparison: Plan A (sequence MCL) vs Plan B (structure Foldseek)

| Metric | Plan A: MMseqs2 + MCL | Plan B: Foldseek + ProstT5 |
| --- | --- | --- |
| Proteins clustered | 2,592 | 2,592 |
| Number of subfamilies | 146 | **73** (half as many) |
| Largest cluster size | 191 | **1,197** |
| Largest cluster covers | 7.4% of VIRs | **46.2% of VIRs** |
| FS clusters that merge ≥2 MCL subfamilies | — | **19 / 73** |
| % proteins in universally-shared clusters | ~99% | 97.3% |
| Method captures distant homology | No | **Yes** (3Di alphabet) |

#### Interpretation

1. **Sequence-based clustering severely over-splits the VIR family.** MCL with default parameters produced 146 separate subfamilies, but 89 of them collapse into a single structural class (FS_001) once 3Di-encoded structure is considered. The classical "12 subfamilies A–L" from Salvador-I are also clearly an artifact of fragmented sequence data — the true *structural* family count is around 10–20 large folds plus a long tail of rare variants.

2. **The dominant fold is universal.** FS_001's 1,197 proteins are roughly evenly distributed across Indonesia (400), Thailand (349), and Peru (448), proving the core VIR fold is conserved on every continent where *P. vivax* is endemic.

3. **Geographic diversity hides in sequence, not structure.** Plan A reported only 0 strictly-unique-to-one-genome subfamilies; Plan B reports 47 structurally unique clusters. But these are vanishingly small (averaging ~1.1 members each), so they likely represent rare lineage-specific variants on top of the universally conserved structural scaffold.

4. **Implication for vaccine/drug design.** Targeting the conserved FS_001 structural fold could in principle affect ~46% of VIR variants regardless of geography. Conversely, the extreme sequence variation within FS_001 (89 distinct MCL subfamilies) explains why a sequence-based vaccine has been so elusive.

#### Outputs
- `data/genomes/alignments/foldseek_work/vir_struct_cluster_cluster.tsv` — full member→rep assignment
- `data/genomes/alignments/foldseek_work/vir_struct_cluster_rep_seq.fasta` — cluster representatives
- `data/genomes/alignments/foldseek_clusters_summary.tsv` — per-cluster table with genome counts and MCL-merge breakdown
- `data/genomes/alignments/fs_clusters/FS_001.aln` through `FS_010.aln` — MSAs of the top 10 structural clusters (also browsable in the Sander Lab viewer)

---

## Plan C: FoldMason → IQ-TREE Structural Phylogeny of *P. vivax* VIR [local]

Replicate the FoldMason paper's structural phylogeny pipeline (Gilchrist et al. 2026, Mifsud-glycoprotein replication, *Science* SM Methods p.14) on our 2,592-protein VIR dataset. Two complementary phylogenies:

* **Q1 (family-level):** Tree of the 73 FoldSeek cluster representatives → relationships among VIR structural classes.
* **Q2 (intra-cluster):** Tree of subsampled FS_001 members → tests whether sequence subclades within the dominant VIR fold (the 1,197-protein structural class) cluster by continent of origin.

### Steps

- [x] 1. **Install IQ-TREE 3, trimAl, R + ggtree** {#plan-c-step-1}
  - Routing: local
  - Tool: conda
  - Verification: `iqtree3 -V`, `trimal --version`, `Rscript -e "library(ggtree)"` succeed
- [x] 2. **Q1: FoldMason MSTA of 73 FS cluster reps** {#plan-c-step-2}
  - Routing: local; Tool: foldmason structuremsa
  - Verification: AA & 3Di alignments with 73 seqs
- [x] 3. **Q1: Trim alignments with trimAl -gt 0.65** {#plan-c-step-3}
  - Routing: local; Tool: trimal
  - Verification: trimmed AA + 3Di alignments produced
- [x] 4. **Q1: Build 3 trees with IQ-TREE 3** (AA / 3Di / partitioned AA+3Di) {#plan-c-step-4}
  - Routing: local; Tool: iqtree3 -m MFP -B 1000 --bnni --alrt 1000 -T 8 --safe --seed 42
  - Verification: 3 treefiles with bootstrap support values
- [x] 5. **Q1: Visualize tree** {#plan-c-step-5}
  - Routing: local; Tool: R + ggtree (tips annotated with cluster size + per-genome composition)
  - Verification: PDF tree figure
- [x] 6. **Q2: Subsample FS_001 to ~200 reps using MMseqs2 easy-cluster** {#plan-c-step-6}
  - Routing: local; Tool: mmseqs2 easy-cluster --min-seq-id 0.5 -c 0.8
  - Verification: 150-300 reps spanning PvP01 / PvW1 / PvPAM
- [x] 7. **Q2: FoldMason MSTA + IQ-TREE on subsampled FS_001** {#plan-c-step-7}
  - Routing: local; Tool: foldmason + iqtree3 (same parameters as step 4)
  - Verification: treefile with bootstrap support
- [x] 8. **Q2: Tip annotation + per-genome monophyly test** {#plan-c-step-8}
  - Routing: local; Tool: R + ape + phytools
  - Verification: annotated PDF + summary statistic (fraction of clades that are single-genome)

### Parameters (summary; full table reviewed in chat)

| Tool | Key parameters |
| --- | --- |
| `foldmason structuremsa` | defaults + `--threads 8` |
| `trimal` | `-gt 0.65 -fasta` |
| `iqtree3` (AA tree) | `-m MFP -B 1000 --bnni --alrt 1000 -T 8 --safe --seed 42` |
| `iqtree3` (3Di tree) | `-m 3DI+FU+R -mset 3DI -B 1000 --bnni --alrt 1000` |
| `iqtree3` (partitioned) | `-p partition.nex` (AA partition + 3Di partition) |
| `mmseqs2 easy-cluster` | `--min-seq-id 0.5 -c 0.8 --threads 8` |


### Plan C Results: Structural Phylogenies

#### Setup
- Q1 trimAl input was *very* sparse — 0 columns passed the paper's `-gt 0.65` cutoff because the 73 reps span the *entire* VIR superfamily of divergent structural classes (the paper's reference was 30-50 closely related glycoproteins). Switched to `-automated1` (trimAl's ML-optimized heuristic) which retained 749 of 1521 columns and 70 of 73 sequences.
- Q2 (intra-FS_001) the paper's `-gt 0.65` worked perfectly: 247 of ~300 columns, 17% gap — confirming FS_001 is a single homologous family.
- 3Di substitution matrix: used the Garg & Hochberg 2025 (Mol. Biol. Evol. 42:msaf124) matrix in NEXUS format, sourced from [jonasmehl1/structural_phylogenetics](https://github.com/jonasmehl1/structural_phylogenetics) — same matrix the FoldMason paper used (their ref 29).

#### Q1: Family-level tree of 70 structural classes

ModelFinder selected **VT+F+G4** as the best AA model (from ~500 candidate models including the protein-mixture set). All three trees (AA, 3Di, partitioned AA+3Di) built successfully with 1000 UFBoot replicates + 1000 SH-aLRT replicates. Tree files: `phylo_q1/trees/q1_{aa,3di,part}.treefile` with bootstrap support values; PDFs: `phylo_q1/q1_{aa,3di,part}_tree.pdf`.

Because each tip represents an entire structural class (not a single protein), tip labels are annotated with `FS_NNN (n=size)` and colored by dominant genome of origin (almost all clusters are universal/balanced across PvP01, PvW1, PvPAM).

#### Q2: Intra-cluster tree of FS_001 (the dominant 1,197-protein structural class)

After 50% identity subclustering with MMseqs2 we got 338 sub-representatives, balanced across genomes (118 PvP01, 110 PvW1, 110 PvPAM). ModelFinder selected **VT+F+R6** as the best AA model.

**Per-genome monophyly test** (parsimony score of "genome of origin" mapped onto the tree, compared to 1000 random label shuffles):

| Tree | Observed parsimony | Median random | P-value | Single-genome internal nodes |
| --- | --- | --- | --- | --- |
| AA (VT+F+R6) | 162 | 160 | 0.69 | 35 / 336 |
| 3Di | 156 | 160 | 0.26 | 37 / 336 |
| Partitioned AA+3Di | 160 | 160 | 0.55 | 34 / 336 |

Minimum possible (perfect monophyly): 2. Observed ≈ 160 across all three trees.

**Interpretation — VIR diversity is NOT geographically structured.** Within the dominant VIR structural class, sequences from Indonesia, Thailand, and Peru are essentially indistinguishable from a random shuffle on the tree (p > 0.25 in all three analyses). Geographic origin contributes effectively no phylogenetic signal — VIR variants from different continents are as related to each other as they are to variants from their own continent.

This rules out the simplest hypothesis that each *P. vivax* lineage independently expanded its own VIR repertoire post-divergence. Instead, the data are consistent with:
1. **Ancient duplications predating the geographic separation** of modern *P. vivax* lineages, plus
2. **Ongoing recombination / gene conversion** within and between subtelomeric loci that keeps VIRs panmictic across continents.

Note: in the cluster-level annotation from Plan B, FS_001 had ~equal contributions from each genome (400/349/448). The phylogeny here confirms that's not just a result of independent parallel expansion — the actual sequences are evolutionarily interleaved.

#### Outputs
- `phylo_q1/q1_{aa,3di,part}_tree.pdf` — annotated family-level trees
- `phylo_q1/trees/q1_*.treefile` — Newick treefiles with UFBoot + SH-aLRT support
- `phylo_q1/trees/q1_*.iqtree` — IQ-TREE reports (substitution models, likelihoods)
- `phylo_q2/q2_{aa,3di,part}_tree.pdf` — circular intra-cluster trees colored by genome
- `phylo_q2/trees/q2_*.treefile` — Newick treefiles
- `phylo_q1/matrices/{3DI.nexus,Q_mat_AF_Garg.txt}` — Garg & Hochberg 2025 3Di substitution matrices

#### Acknowledgment
3Di substitution matrices courtesy of [jonasmehl1/structural_phylogenetics](https://github.com/jonasmehl1/structural_phylogenetics), originally from Garg & Hochberg 2025 (*Mol. Biol. Evol.* 42:msaf124).

---

# Structure-Aware Phylogenomics of the *P. vivax* VIR Multigene Family

## 1. The FoldMason paper

Gilchrist, Mirdita, and Steinegger (2026, *Science*) introduced FoldMason, a progressive multiple structural alignment (MSTA) method that operates simultaneously on amino acid (AA) sequences and on the 3Di structural alphabet developed for Foldseek. The 3Di alphabet encodes the local backbone geometry of every residue as one of twenty letters, so two proteins that share a fold but no detectable sequence identity will still align in 3Di. FoldMason builds a guide tree from all-versus-all 3Di+AA pairwise alignments and then performs progressive alignment from the leaves to the root, producing two output alignments in lockstep: one over the AA alphabet and one over the 3Di alphabet, with identical column coordinates.

A central demonstration in the paper is that FoldMason MSTAs are good enough to recover known phylogenetic relationships even between proteins that are no longer alignable by sequence-based methods. The authors took the Flaviviridae glycoprotein dataset assembled by Mifsud et al. (2024), which spans the E, E1, and E2 envelope glycoprotein families (roughly thirty to fifty proteins per family, with pairwise sequence identity in some cases well below the so-called twilight zone of 20-25%). For each family they ran FoldMason `easy-msa` to produce AA and 3Di alignments, trimmed columns containing 35% or more gaps with trimAl, ran ModelFinder to select an AA substitution model and used the published Garg & Hochberg 2025 3Di substitution matrix for the 3Di alignment, and inferred three maximum-likelihood trees per family with IQ-TREE 2 and 1000 ultrafast bootstrap replicates: one tree from AA alone, one from 3Di alone, and one from a partitioned analysis of concatenated AA+3Di. Tree similarity to the Mifsud et al. reference trees was measured with quartet similarity and Robinson-Foulds distance from the Quartet R package. Across the three glycoprotein families, FoldMason-derived trees were highly concordant with the manually constructed reference phylogenies, with much of the gain attributable to the 3Di partition recovering relationships invisible to sequence alone.

## 2. What we set out to do

We wanted to apply this same structure-aware phylogenomic pipeline to the largest and most poorly understood gene family in the *Plasmodium vivax* genome: the VIR (or *vir*) family of variant surface antigens, part of the broader PIR (*Plasmodium* interspersed repeat) superfamily. Three considerations motivated the work. First, VIRs are extremely sequence-divergent, so sequence-only methods cluster them into many small fragments that almost certainly do not reflect the true family structure. Second, Harrison and Higgins (2020) had shown structurally that PIRs share a single conserved fold despite that sequence divergence, which is exactly the situation in which structural alignment should outperform sequence alignment. Third, three high-quality long-read reference genomes had recently become available from geographically distant *P. vivax* isolates -- PvP01 from Papua, Indonesia; PvW1 from Thailand; PvPAM from the Peruvian Amazon -- making it possible to ask not only how the VIR family is organized but whether its organization is shared across continents or evolved independently after the geographic separation of *P. vivax* lineages.

Our plan, designed to mirror the FoldMason paper as closely as the data allowed, had three stages. Stage one (Plan A) was a sequence-based clustering with MMseqs2 and Markov Clustering to provide a baseline reference point. Stage two (Plan B) was structure-aware clustering of the same set of proteins with Foldseek using the ProstT5 protein language model to predict 3Di alphabet sequences directly from amino acid sequence (so we did not need to compute any actual three-dimensional structures). Stage three (Plan C) was phylogenetic analysis with FoldMason and IQ-TREE following the procedure used in the FoldMason paper for the glycoproteins, applied twice: once at the family level on the structural cluster representatives, and once within the dominant structural cluster to look for geographic signal among individual VIR sequences.

## 3. What is known about PIR / VIR genes

The PIR superfamily is the largest multigene family in essentially every *Plasmodium* species sequenced to date, including the rodent malarias (where it has the lineage-specific names *cir*, *bir*, *yir*), the simian parasites *P. knowlesi* (*kir*) and *P. cynomolgi* (*cyir*), the human-infecting *P. vivax* (*vir*), and *P. ovale* and *P. malariae*. The dramatic exception is *P. falciparum*, which has no PIR genes at all; instead, its functionally analogous variant antigen family is *var*. PIR genes are concentrated in the subtelomeric regions of every chromosome, where the high local recombination rate appears to act as an evolutionary engine for rapid duplication, gene conversion, and pseudogenization. Their typical gene architecture, conserved across species, is a three-exon structure: a short first exon encoding a signal peptide that directs the protein into the secretory pathway, a much longer second exon that encodes a highly variable extracellular domain responsible for antigenic variation, and a short third exon encoding a transmembrane anchor.

The number of copies per genome varies enormously between species and is exquisitely sensitive to assembly quality. The original short-read Salvador-I reference of *P. vivax* (Carlton et al., 2008) reported 346 *vir* genes organized into twelve subfamilies (A through L); long-read assemblies have since revealed that the true *vir* repertoire of *P. vivax* contains well over a thousand copies, with much of the early missing complement hidden in unassembled subtelomeric contigs. The PvP01 reference (Auburn et al., 2016) reported approximately 1,200 *vir* genes; the PvW1 reference (Minassian et al., 2021) reports 1,145; the PvPAM reference (Vaughan et al., 2023) reports 975 functional copies plus 99 pseudogenes. Notably, more than 600 of the PvPAM *vir* genes share no direct one-to-one orthology with PvP01, an observation that has been used to argue that the family is undergoing rapid, lineage-specific expansion.

Despite their abundance, the functions of individual PIR/VIR proteins remain poorly characterized. Several broad roles are reasonably well-supported in the literature. They are exported to the surface of the infected red blood cell, where they contribute to antigenic variation: switching the surface PIR repertoire allows the parasite to escape the host's antibody response and establish chronic infections. They appear to mediate cytoadherence, binding to receptors on the endothelium of small blood vessels and thereby allowing the infected red cell to avoid clearance by the spleen. They also play a role in rosetting, the clumping of infected and uninfected red cells together, which is associated with severe malaria. In *P. vivax*, transcriptomic studies have associated changes in *vir* expression with severe clinical outcomes including hepatic dysfunction, renal failure, and cerebral malaria, even though *P. vivax* was historically considered a "benign" form of malaria. Several groups have also reported that specific *vir* subfamilies are expressed at different parasite life-cycle stages, suggesting that the variation within the family is functionally partitioned rather than purely redundant.

The structural biology of the family was substantially clarified by Harrison and Higgins (2020), who solved the first crystal structure of a PIR ectodomain, using a member of the family from the rodent parasite *P. chabaudi chabaudi*. The structure (PDB: 6ZYV) showed a small, compact, mostly alpha-helical fold that the authors argued was conserved across the entire PIR superfamily, despite the extreme sequence variation. This is precisely the situation that motivates structural rather than sequence-based phylogenomics: the proteins share a fold, but for many pairs the sequence similarity is below the level at which sequence alignment is reliable.

## 4. Analysis

### 4.1. Extracting the VIR proteins

For each of the three reference genomes (PvP01, PvW1, PvPAM) we downloaded the full annotated proteome FASTA from PlasmoDB release 71. We attempted to extract VIR proteins by parsing the gene-product annotations in the FASTA headers, but found that PvW1 in particular only labels about fifty of its sequences as "VIR protein" -- most of its expected ~1,100 *vir* genes are labelled "unspecified product" in the PlasmoDB release. We therefore used the canonical Pfam profile HMM for the *vir* domain (`PF05795`, "Plasmodium_Vir") with `hmmer3` to identify VIR proteins by sequence-profile similarity rather than annotation text. This recovered 931 VIR proteins from PvP01, 748 from PvW1, and 985 from PvPAM, for a combined dataset of 2,664 proteins. After accounting for sequences that later dropped out during clustering (those that didn't form pairs at our coverage threshold), 2,592 proteins entered the downstream analyses.

### 4.2. Sequence-only baseline (Plan A)

We first asked what structure the family takes when one uses only the amino acid sequences. We ran an all-versus-all sequence comparison of the 2,664 VIR proteins with MMseqs2 at default settings (E-value 1e-5, sequence identity threshold 30%, mutual coverage 50%), converted the resulting bitscore matrix into the ABC format expected by the Markov Clustering Algorithm (MCL), and ran MCL with an inflation parameter of 2.0. This produced 146 sequence-based subfamilies containing three or more members. The largest contained 191 proteins, the next 182, and the size distribution was relatively flat: no single cluster dominated. When we cross-tabulated the cluster membership against genome of origin, 132 of the 146 subfamilies (90%) contained members from all three genomes, indicating that the family's sequence-level structure is largely conserved across continents at the resolution of the clustering. We will return to this number after the structural clustering, because the sequence-only picture is misleading.

### 4.3. Structure-aware clustering with Foldseek + ProstT5 (Plan B)

To bring structural information into the clustering without having to compute three-dimensional structures for 2,592 proteins, we used Foldseek's integration with ProstT5, a protein language model that predicts the 3Di alphabet directly from amino acid sequence. We built a Foldseek database from the combined VIR FASTA using ProstT5 to populate the 3Di field, then ran `foldseek easy-cluster` with mutual coverage 0.8, E-value 0.001, and `--alignment-type 2` (combined 3Di+AA scoring). This produced 73 clusters with three or more members -- exactly half as many as the 146 sequence-based MCL clusters. Critically, the size distribution was now extremely skewed. The single largest cluster, which we labelled FS_001, contained 1,197 proteins, or 46% of the entire VIR repertoire across all three genomes. The next four clusters (FS_002 through FS_005) contained 385, 248, 143, and 136 proteins respectively. Beyond cluster ten, the clusters dropped quickly into the single digits.

We then asked, for each Foldseek cluster, how many sequence-based MCL subfamilies it merged. The answer was striking. FS_001 alone merged 89 of the 146 MCL subfamilies, FS_002 merged 36, FS_003 merged 32. In other words, the sequence-based pipeline was over-splitting the family by roughly a factor of two: many "subfamilies" that looked distinct by sequence were collapsed into single structural classes once the structural alphabet was taken into account. This is exactly the prediction Harrison and Higgins had made on the basis of the PIR crystal structure: that PIRs are structurally unified beyond the reach of sequence-based clustering.

When we counted protein membership rather than cluster identity, the picture of cross-continental conservation became even sharper. 97.3% of all 2,592 VIR proteins fall into structural clusters that contain members from all three reference genomes. The 47 Foldseek clusters that we initially flagged as "genome-unique" together account for only 52 proteins (2% of the total) -- they are almost all singletons or pairs and likely represent rare lineage-specific variants on top of an otherwise universally conserved structural scaffold. Within the large universal clusters, the per-genome composition is roughly proportional to each genome's contribution to the dataset: in FS_001, for example, the 1,197 members break down as 400 from PvP01 (Indonesia), 349 from PvW1 (Thailand), and 448 from PvPAM (Peru), close to what one would expect if the underlying repertoires were drawn from a shared distribution.

### 4.4. Phylogeny at the family level (Plan C, Q1)

We then asked whether maximum-likelihood phylogenetic methods would tell the same story. Following the procedure used in the FoldMason paper for the Flaviviridae glycoproteins, we took the 73 Foldseek cluster representatives as input to FoldMason `structuremsa`, producing AA and 3Di multiple sequence alignments. We trimmed the alignments with trimAl. The procedure used by Gilchrist et al. was to trim columns with 35% or more gaps (`-gt 0.65`); we found that with our data this removed every column, because by construction the 73 cluster representatives are the most distant proteins in the family from each other. We instead used trimAl's `-automated1` mode, designed specifically for downstream ML phylogenetics on diverged data, which retained 749 of the original 1,521 columns and 70 of the 73 sequences. We then ran IQ-TREE 3 with ModelFinder for the AA alignment (which selected `VT+F+G4` as the best-fit model), with the Garg & Hochberg 2025 3Di substitution matrix (NEXUS format, obtained from the `jonasmehl1/structural_phylogenetics` repository, the same matrix used in the FoldMason paper) for the 3Di alignment, and with a partitioned analysis of concatenated AA+3Di. Each tree was inferred with 1000 ultrafast bootstrap replicates and 1000 SH-aLRT replicates for branch support.

The three trees agreed on the broad topology: a small number of well-supported deep clades each corresponding to a major group of structural classes, with the relationships between deep clades less well-supported. The trees are useful as a scaffold for downstream annotation -- for example, asking which structural classes are most distant from the bulk of the family, or which subset of classes is restricted to particular life-cycle stages once expression data is layered on -- but the small number of tips per branch and the high sequence divergence between cluster representatives means we should not expect strong resolution at every node.

### 4.5. Phylogeny within the dominant structural class (Plan C, Q2)

The more biologically interesting question is at finer resolution: within the dominant FS_001 fold, where 1,197 sequences from three continents coexist, is there any signal of geographic structure? To answer this we subsampled FS_001 with MMseqs2 at 50% sequence identity and 80% coverage, which yielded 338 sub-representatives (118 from PvP01, 110 from PvW1, 110 from PvPAM -- excellent balance for an unbiased test). We aligned these with FoldMason, trimmed with `-gt 0.65` (which now worked: the cluster is homologous, so trimming retained 247 columns at 17% gap), and inferred three trees with IQ-TREE 3 using the same procedure as above. The AA model selected by ModelFinder was `VT+F+R6`.

We then tested whether genome of origin predicts position on the tree, by treating "genome of origin" as a three-state discrete character (PvP01, PvW1, PvPAM) and computing its parsimony score on each tree using phangorn. The minimum possible parsimony score, achieved if each genome formed a single monophyletic clade, is 2. A higher score means more state changes are needed, with perfect mixing (no geographic signal) giving the highest scores. To convert the score into a p-value, we randomized the tip labels 1000 times and recomputed the parsimony score on each shuffle.

The result was the same across all three trees. The observed parsimony score on the AA tree was 162, on the 3Di tree 156, and on the partitioned tree 160. The median parsimony score under random label shuffles was 160, with a range of roughly 145 to 177. The probability of observing a parsimony score at least as low as the actual one, by chance, was 0.69 for the AA tree, 0.26 for the 3Di tree, and 0.55 for the partitioned tree -- none significant. Counting internal nodes whose descendants all came from a single genome gave 34 to 37 out of 336 internal nodes (10-11%), no more than expected by chance for three states distributed evenly across tips.

This is a clear negative result with a clear biological interpretation. Within the dominant VIR structural class, sequences from Indonesia, Thailand, and Peru are evolutionarily interleaved to the point of being indistinguishable from a random arrangement on the tree. The simple model in which each *P. vivax* lineage independently expanded and diversified its own VIR repertoire after the geographic separation of modern lineages is not consistent with these data. The data are more consistent with a scenario in which most of the diversification of FS_001 predated the geographic separation of *P. vivax* populations, and in which ongoing recombination and gene conversion among subtelomeric *vir* loci continue to keep the family panmictic across continents. The same general pattern -- conservation of structural class assignment across geography, with sequence-level variation distributed randomly within those classes -- holds for the other large structural clusters where we have enough sequences to test it.

### 4.6. What this exercise demonstrates

Three things are worth noting from a methods standpoint. First, the pipeline used by the FoldMason paper for the glycoprotein replication transfers cleanly to the *Plasmodium* VIR family with only one adjustment: the trimAl gap threshold used by Gilchrist et al. (`-gt 0.65`) was calibrated for closely related glycoprotein homologs and is too stringent when the input spans the entire diversity of a multigene superfamily; switching to trimAl's `-automated1` heuristic is the right choice in that case. Second, ProstT5 is good enough that no actual three-dimensional structure prediction is required: the entire structure-aware analysis can be done from FASTA input, which makes it tractable to apply to families of thousands of proteins on a laptop. Third, the combination of structural clustering (Foldseek + ProstT5) and structural phylogenetics (FoldMason + IQ-TREE with the Garg & Hochberg 3Di matrix) produces qualitatively different answers from the corresponding sequence-only pipelines, and in this case the structural answer is biologically more compelling: the VIR family is far more unified, and far less geographically structured, than its sequence diversity would suggest.


---

## Plan D: Spatial / Genomic Distribution of VIR Structural Clusters [local]

Spatial analysis of the 21 strict-universal Foldseek clusters (members in all three reference genomes) and a focused deep-dive on FS_001. Goal: characterize where each VIR gene sits in the genome, whether members of the same structural class cluster tandemly, whether structural classes co-localize, and whether the spatial signature of each cluster is conserved across PvP01, PvW1, and PvPAM.

### Steps

- [x] 1. **Extract chromosomal coordinates** {#plan-d-step-1} from PlasmoDB FASTA headers (`location=...`); 2,664 VIRs with valid coords.
- [x] 2. **Identify universal clusters** {#plan-d-step-2} — 21 FS clusters strictly present in all three genomes.
- [x] 3. **Chromosomal distribution table** {#plan-d-step-3}
- [x] 4. **Subtelomeric enrichment** {#plan-d-step-4}
- [x] 5. **Tandem-clustering test** {#plan-d-step-5}
- [x] 6. **Cross-cluster co-localization** {#plan-d-step-6}
- [x] 7. **Chromosome ideograms** {#plan-d-step-7}
- [x] 8. **FS_001 deep dive** {#plan-d-step-8}
- [x] 9. **Cross-genome synteny of spatial signatures** {#plan-d-step-9}

### Plan D Results: Spatial organization of VIR structural clusters

#### Assembly contiguity matters

Before reading the spatial numbers it is important to acknowledge that the three reference assemblies differ in how well they resolve subtelomeric regions. PvP01 was assembled from high-depth Illumina data and ends up with 130 distinct contigs that host VIRs, 114 of which are small subtelomeric fragments under 200 kb. PvW1 and PvPAM, assembled with PacBio long reads, place the same kind of subtelomeric VIR neighborhoods on the main chromosomes themselves -- PvW1 has only 17 VIR-bearing contigs (none small) and PvPAM has 26 (8 small). When we put a VIR on a 50 kb subtelomeric Illumina contig and ask "how far is it from the chromosome end?", the answer is at most 50 kb -- not because the gene is exceptionally subtelomeric, but because the contig itself is short. Restricting the analysis to the 14 largest contigs per genome (which always recover the main chromosomes) gives us 347 of 931 VIRs from PvP01 (37%), 634 of 748 from PvW1 (85%), and 735 of 985 from PvPAM (75%). All spatial statistics below are reported on the main-chromosome subset.

#### VIRs are subtelomeric

Across all three genomes, 64.5% of main-chromosome VIRs lie in the outer 10% of their chromosome length, against a uniform-distribution expectation of 20%. By genome: PvP01 80%, PvW1 64%, PvPAM 57%. The remaining ~35% are not "internal" in the textbook sense -- median distances to the nearest chromosome end for most universal clusters fall in the 30-160 kb range, which is still well inside the standard *P. vivax* subtelomeric definition of 100-200 kb.

#### Members of one cluster are NOT tandemly arrayed

For each (cluster, genome) we computed the mean distance from each VIR to the nearest same-FS-cluster VIR on the same chromosome, and compared it to 500 random shuffles of cluster labels. Across the 32 (cluster, genome) tests with enough members to evaluate (mostly the top 10 universal clusters), only 2 reached p < 0.05 -- consistent with chance under multiple testing. The conclusion is clean: members of a single VIR structural class are NOT preferentially next to other members of the same class. They are mixed in with members of other classes within the same subtelomeric neighborhoods.

#### But VIRs do co-localize with other VIRs

Looking at all VIR-VIR pairs within 50 kb on the same chromosome, the rate of same-cluster pairs is consistently higher than expected if cluster labels were randomly assigned to subtelomeric positions:

| Genome | Same-cluster pairs | Different-cluster pairs | Observed same-rate | Expected if independent |
| --- | --- | --- | --- | --- |
| PvP01 | 572 | 1,070 | 34.8% | 20.0% |
| PvW1 | 928 | 2,041 | 31.3% | 24.0% |
| PvPAM | 1,314 | 2,832 | 31.7% | 23.4% |

So there *is* a mild same-class neighbor-enrichment, but not enough to form true tandem blocks -- it looks more like "structural class X tends to occupy similar subtelomeric neighborhoods, sometimes adjacent and sometimes a few neighbors apart." The cross-cluster co-localization heatmap (`colocalization_heatmap.pdf`) shows that no specific pair of FS clusters co-occurs more strongly than others -- the diagonal is the dominant signal.

#### Spatial signatures are conserved across genomes

For each cluster we summarized its main-chromosome footprint as a feature vector: number of chromosomes occupied, median relative distance to chromosome end, and fraction of members in the outer 10% of chromosomes. We then asked whether these feature vectors are correlated across genomes (Spearman ρ over the 21 universal clusters):

| Spatial feature | ρ(PvP01, PvW1) | ρ(PvP01, PvPAM) | ρ(PvW1, PvPAM) |
| --- | --- | --- | --- |
| Number of chromosomes occupied | **0.909** | **0.914** | **0.915** |
| Median relative distance to chrom end | 0.468 | 0.261 | 0.386 |
| Fraction of members in outer 10% | 0.280 | 0.341 | 0.081 |

The number of chromosomes a cluster occupies is highly conserved: a cluster that lives on many chromosomes in PvP01 lives on many in PvW1 and PvPAM as well. The subtelomeric-positioning metrics are weakly correlated, in line with the assembly-quality differences we flagged earlier.

#### FS_001 deep dive

FS_001 is present on all 14 main chromosomes of all three genomes (137 / 284 / 320 members on main chromosomes of PvP01 / PvW1 / PvPAM). The relative-position density plots (`fs001_chromosomal_density.pdf`) show that FS_001 members are concentrated in the outer 10-15% of every chromosome and that the density profile is essentially indistinguishable from the rest of the VIR repertoire. Combined with the parsimony result from Plan C Q2 (no geographic structure within FS_001), the picture is consistent: FS_001 was diversified deep in *P. vivax*'s past, distributed broadly across the subtelomere of every chromosome, and continues to evolve through subtelomeric recombination that prevents any geographic or tandem-block structure from accumulating.

#### Outputs
- `data/genomes/alignments/spatial/vir_coords.tsv` — full VIR coordinate table (all 2,664)
- `data/genomes/alignments/spatial/vir_coords_main.tsv` — main-chromosome subset (1,716)
- `data/genomes/alignments/spatial/universal_clusters.tsv` — the 21 universal FS clusters
- `data/genomes/alignments/spatial/tandem_test_main.tsv` — per-cluster tandem-clustering p-values
- `data/genomes/alignments/spatial/synteny_features.tsv` — per-cluster spatial feature vectors per genome
- `data/genomes/alignments/spatial/colocalization_heatmap.pdf` — cross-cluster co-localization, per genome
- `data/genomes/alignments/spatial/ideogram_all_genomes.pdf` — chromosomal landscape of VIRs colored by FS cluster
- `data/genomes/alignments/spatial/fs001_chromosomal_density.pdf` — FS_001 vs other VIRs, relative chromosomal position per genome

---

## Plan E: Potential Orthologs of FS_001 Members between PvW1 and PvPAM [local]

Identify potential 1-to-1 orthologs of FS_001 VIR genes between PvW1 (Thailand, PacBio+Illumina hybrid) and PvPAM (Peruvian Amazon, PacBio) using reciprocal best hits, microsynteny preservation against the non-VIR housekeeping ortholog backbone, and consistency with the FS_001 phylogeny from Plan C Q2. PvP01 is excluded because its Illumina assembly fragments subtelomeric VIRs across 114 small contigs, defeating microsynteny analysis.

### Steps

- [x] 1. **Extract FS_001 protein sequences for PvW1 and PvPAM** {#plan-e-step-1}
  - Routing: local; Tool: python
  - Verification: 349 PvW1 + 448 PvPAM sequences extracted
- [x] 2. **Reciprocal best hits with MMseqs2 (FS_001 only)** {#plan-e-step-2}
  - Routing: local; Tool: mmseqs easy-rbh
  - Verification: RBH pairs with seq-id, coverage, E-value
- [x] 3. **Flanking-gene context tables (2 non-VIR neighbors each side)** {#plan-e-step-3}
  - Routing: local; Tool: python
  - Verification: per-RBH-gene flanking table
- [x] 4. **Housekeeping RBH (PvW1 × PvPAM non-VIR proteome)** {#plan-e-step-4}
  - Routing: local; Tool: mmseqs easy-rbh
  - Verification: ~5,000 housekeeping ortholog pairs
- [x] 5. **Microsynteny verification per FS_001 RBH pair** {#plan-e-step-5}
  - Routing: local; Tool: python
  - Verification: synteny score 0-4 per FS_001 RBH pair
- [x] 6. **Sequence identity distribution vs housekeeping baseline** {#plan-e-step-6}
  - Routing: local; Tool: python + matplotlib
  - Verification: PDF histogram
- [x] 7. **Cross-check against the FS_001 Plan C Q2 phylogeny** {#plan-e-step-7}
  - Routing: local; Tool: python (biopython.Phylo)
  - Verification: `in_tree` and `sister_leaves` flags per pair
- [x] 8. **Combined evidence table with high/medium/low confidence classes** {#plan-e-step-8}
  - Routing: local; Tool: pandas
  - Verification: ortholog table with confidence categories
- [x] 9. **Ribbon synteny plot (PvW1 left, PvPAM right; ribbons colored by confidence)** {#plan-e-step-9}
  - Routing: local; Tool: matplotlib
  - Verification: PDF saved

### Parameters (summary; full table reviewed in chat)

| Step | Tool | Key parameters |
| --- | --- | --- |
| 2 | mmseqs easy-rbh | `--min-seq-id 0.3 -c 0.5 -e 1e-5 --threads 8 --format-mode 4` |
| 4 | mmseqs easy-rbh | `--min-seq-id 0.5 -c 0.8 -e 1e-10 --threads 8 --format-mode 4` |
| 3 | python | 2 non-VIR neighbors each side |
| 5 | python | synteny score = number of flanking pairs that are housekeeping orthologs (0-4) |
| 8 | python | high = microsynteny ≥ 3 AND identity ≥ 50% AND (not in tree OR sister_leaves); medium = microsynteny ≥ 2 OR sister_leaves |
| 9 | matplotlib | ribbons: high α=1.0, medium α=0.4, low α=0.1; same-strand blue, opposite-strand red |


### Plan E Results: Potential PvW1 ↔ PvPAM orthologs within FS_001

#### Headline numbers

- **194 reciprocal best hits** (RBH) between the 349 PvW1 and 448 PvPAM FS_001 members (`mmseqs easy-rbh`, identity ≥ 30%, coverage ≥ 50%, E < 1e-5).
- **5,121 housekeeping RBH pairs** between the non-VIR proteomes of PvW1 and PvPAM (identity ≥ 50%, coverage ≥ 80%, E < 1e-10).
- After integrating microsynteny and phylogeny evidence: **11 high-confidence, 26 medium-confidence, 157 low-confidence** ortholog candidates.

#### Sequence identity tells the first story

Housekeeping RBH pairs are essentially identical between PvW1 and PvPAM: median identity 99.8%, mean 98.6%, with the bulk of the distribution above 95%. This is expected -- the two genomes come from different *P. vivax* lineages but the species itself is recent and housekeeping proteins are well-conserved. Against that baseline, FS_001 RBH pairs are sharply more diverged: median identity 74.5%, mean 75.2%, range 30-100%. That ~25-percentage-point gap is what you would expect from a multigene family undergoing rapid, lineage-specific diversification on top of the slowly-evolving core genome. The `identity_histogram.pdf` shows the two distributions are clearly separated, with very little overlap at the high-identity tail.

#### Microsynteny rarely survives in subtelomeric VIR neighborhoods

For each FS_001 RBH pair we asked how many of the four nearest flanking non-VIR genes (two upstream + two downstream) have a housekeeping ortholog in the matched flanking positions of the partner gene's neighborhood. The result was sobering:

| Synteny score (flanking orthologs matched) | Number of pairs | Fraction |
| --- | --- | --- |
| 0 | 139 | 72% |
| 1 | 21 | 11% |
| 2 | 23 | 12% |
| 3 | 7 | 4% |
| 4 | 4 | 2% |

For nearly three-quarters of FS_001 RBH pairs, *none* of the four flanking non-VIR neighbors are housekeeping orthologs. This is the spatial signature of the subtelomere: gene neighborhoods are dynamic, and the local context around any one VIR gene has been substantially rearranged between PvW1 and PvPAM. Only 11 pairs (6%) have ≥3 of 4 flanking orthologs preserved -- and those 11 are the high-confidence ortholog calls.

#### Phylogenetic sanity check

The Plan C Q2 phylogeny was built on a 50%-identity sub-sampled set of FS_001 (338 sequences, 110 PvW1 + 110 PvPAM). Only 7 of the 194 RBH pairs have both members in that sub-sample -- the rest were collapsed by the 50% identity reduction. Of those 7, **4 are sister leaves on the AA tree**. A 4/7 sister-leaf rate is far above what would be expected by chance (under random topology, the probability is roughly 1/n_tree_leaves), and it confirms that when an RBH pair survives the subsampling, the phylogeny independently supports the orthology call.

#### High-confidence orthologs share three traits

All 11 high-confidence pairs have synteny score 3 or 4 and ≥70% sequence identity. Their median identity is 87% (range 70-99.7%), and several pairs are essentially identical proteins:

- `CAG9479603.1` ↔ `CAI7718713.1`: 99.7% identity, 3/4 synteny
- `CAG9479601.1` ↔ `CAI7718711.1`: 97.1% identity, 3/4 synteny
- `CAG9483878.1` ↔ `CAI7717862.1`: 95.7% identity, 4/4 synteny
- `CAG9483870.1` ↔ `CAI7717859.1`: 95.9% identity, 4/4 synteny
- `CAG9480041.1` ↔ `CAI7719021.1`: 86.8% identity, 4/4 synteny

These are the strongest 1-to-1 ortholog candidates in FS_001. Several of them appear in clusters of consecutive gene IDs in both genomes (e.g., `CAG9483870/CAG9483878/CAG9483882` ↔ `CAI7717859/CAI7717862/CAI7717863`), suggesting they sit in the rare subtelomeric neighborhood where gene order is preserved between Thailand and Peru.

#### Ribbon synteny plot

`ribbon_synteny.pdf` draws the 14 main chromosomes of PvW1 on the left and PvPAM on the right, with each RBH pair drawn as a curved Bezier ribbon between the two gene positions. Ribbons are colored by confidence class (high: saturated blue, medium: light blue, low: faded gray) and high-confidence opposite-strand pairs are highlighted in red. The plot makes clear that the subtelomeric VIR repertoires of the two genomes are extensively rearranged: ribbons criss-cross between chromosomes rather than connecting matched chromosomal positions, and the high-confidence orthologs form just a handful of distinct same-chromosome-end-to-same-chromosome-end matches against the backdrop of many cross-chromosome RBH pairs.

#### Biological interpretation

The combined picture is consistent with what Plan C Q2 and Plan D already suggested:

1. **Most FS_001 RBH pairs are not true 1-to-1 orthologs.** The 157 low-confidence pairs are best explained as either paralogs from independent duplication events or as RBH partners chosen from a sea of near-equivalent sequences in each genome -- the reciprocal-best-hit signal is real but does not necessarily reflect direct evolutionary descent.
2. **A small core of FS_001 genes is robustly conserved between PvW1 and PvPAM.** Eleven high-confidence pairs share strong sequence similarity, intact local gene order, and (where the data exist) sister-leaf relationships on the FS_001 tree. These are the candidates worth following up functionally.
3. **The subtelomeric environment is the main source of orthology decay.** The 0-score microsynteny majority is not noise -- it reflects genuine, ongoing recombination and gene replacement within subtelomeric blocks, which decouples the VIR gene from its broader genomic context faster than the gene itself diverges in sequence.

#### Outputs
- `data/genomes/alignments/ortho/fs001_rbh.tsv` — FS_001 RBH pairs with identity, coverage, E-value, bitscore
- `data/genomes/alignments/ortho/housekeeping_rbh.tsv` — non-VIR proteome RBH backbone
- `data/genomes/alignments/ortho/flanking.tsv` — 4-neighbor flanking context per RBH pair
- `data/genomes/alignments/ortho/synteny_scores.tsv` — microsynteny score (0-4) per pair
- `data/genomes/alignments/ortho/phylogeny_check.tsv` — `in_tree` / `sister_leaves` flags per pair
- `data/genomes/alignments/ortho/orthologs_combined.tsv` — joined evidence table with confidence class
- `data/genomes/alignments/ortho/orthologs_high_confidence.tsv` — the 11 high-confidence pairs
- `data/genomes/alignments/ortho/identity_histogram.pdf` — FS_001 vs housekeeping identity distributions
- `data/genomes/alignments/ortho/ribbon_synteny.pdf` — ribbon plot, PvW1 ↔ PvPAM







---

# The *P. vivax* PIR Family Across Three High-Quality Reference Assemblies

## Introduction

The PIR (*Plasmodium* interspersed repeat) family is the largest multigene family in *Plasmodium vivax* and one of the largest in any eukaryotic genome. Its members encode variant surface antigens that are exported to the surface of infected reticulocytes, where they appear to participate in antigenic variation, cytoadherence to endothelial receptors, and the establishment of chronic asymptomatic infections. In *P. vivax* the family is called *vir* (for "*P. vivax* variant"), and is part of the broader PIR superfamily that spans every sequenced *Plasmodium* species except *P. falciparum*. The defining structural feature, established by the crystal structure of a *P. chabaudi* PIR ectodomain (Harrison & Higgins, 2020, PDB 6ZYV), is a small, mostly alpha-helical fold that is preserved across the entire superfamily despite extensive sequence divergence between individual members. This conserved fold is captured at the sequence-profile level by a hidden Markov model in the Pfam database (Mistry et al., 2021, *Nucleic Acids Res.* 49:D412) with accession PF05795, which is the operational definition of a PIR/VIR protein used throughout this analysis: any annotated protein in a *P. vivax* proteome that matches the PF05795 profile with a significant E-value, found with `hmmsearch` from HMMER 3 (Eddy, 2011, *PLoS Comput. Biol.* 7:e1002195). This structural conservation is the central reason why characterizing the family at scale requires structure-aware methods: pairwise sequence identity within the family falls well below the so-called twilight zone of 20-25%, where standard sequence-based homology methods break down.

Until recently, the *vir* family in *P. vivax* was known almost exclusively from the Salvador-I reference genome (Carlton et al., 2008), in which 346 *vir* genes were annotated and organized into twelve subfamilies labelled A through L on the basis of pairwise sequence similarity. The Salvador-I assembly was produced from Sanger sequencing of a monkey-adapted strain and is known to be highly fragmented in subtelomeric regions, where the bulk of the *vir* repertoire resides. In the past decade, three considerably more contiguous reference genomes from geographically distant *P. vivax* lineages have become available: PvP01 from Papua, Indonesia (Auburn et al., 2016), assembled from very high-depth Illumina sequencing with manual curation of the subtelomeres; PvW1 from Thailand (Minassian et al., 2021), a hybrid Illumina + PacBio assembly produced for controlled human malaria infection studies; and PvPAM from the Peruvian Amazon (Vaughan et al., 2023), a PacBio-only assembly produced from a low-input patient sample. These three references together span Asia, Southeast Asia, and the Americas, and each resolves the subtelomeric *vir* repertoire to a different degree.

This section characterizes the *P. vivax* PIR family across these three modern assemblies, using a structure-aware computational pipeline based on Foldseek + ProstT5. Foldseek (van Kempen et al., 2024, *Nat. Biotechnol.* 42:243) is a structural homology search tool that encodes the local backbone geometry of every residue in a protein structure as one of twenty letters in the so-called 3Di structural alphabet, and then aligns proteins using both the amino acid alphabet and the 3Di alphabet simultaneously. ProstT5 (Heinzinger et al., 2024, *NAR Genom. Bioinform.* 6:lqae150) is a protein language model trained to predict the 3Di alphabet directly from amino acid sequence, so the combination allows structural clustering of large protein sets without ever computing three-dimensional structures and FoldMason (Gilchrist et al., 2026, *Science*, doi:10.1126/science.ads6733) and IQ-TREE 3 (Trifinopoulos et al., 2026; the 2020 paper Minh et al., *Mol. Biol. Evol.* 37:1530, describes IQ-TREE 2 which is the methodological reference). FoldMason performs progressive multiple structural alignment using a guide tree built from all-versus-all 3Di+AA pairwise comparisons, producing aligned amino acid and 3Di sequences in lockstep. IQ-TREE 3 is a maximum-likelihood phylogenetic inference engine with built-in substitution model selection (ModelFinder; Kalyaanamoorthy et al., 2017, *Nat. Methods* 14:587), efficient ultrafast bootstrap (UFBoot; Hoang et al., 2018, *Mol. Biol. Evol.* 35:518) and the SH-aLRT branch test (Anisimova & Gascuel, 2006, *Syst. Biol.* 55:539).. The goal is descriptive: to provide an organized account of how many PIR proteins exist in each assembly, how they group into structural classes, how those classes are distributed across the genome, which members can be confidently mapped between assemblies as 1-to-1 orthologs, and what the within-class diversity looks like. The Salvador-I reference is referred to throughout as the historical baseline but is not re-analyzed at the protein level here, because its subtelomeric fragmentation makes per-protein structural and spatial characterization unreliable -- a comparison that would be useful but requires re-assembly work beyond the scope of this characterization.

## Assembly resources and PIR census

The three assemblies differ substantially in sequencing technology, contiguity, and consequently in how completely they resolve subtelomeric *vir* clusters. Table 1 summarizes the relevant properties as they affect this analysis. Per-protein characterization in this section is based on the predicted functional proteome of each assembly as released through PlasmoDB release 71 (Amos et al., 2022, *Nucleic Acids Res.* 50:D898; PlasmoDB is the *Plasmodium* genome database within the VEuPathDB resource, providing curated genome annotations, gene ontology mappings, and orthology calls for malaria parasite genomes). Pseudogenes are analyzed separately. The PvP01 and PvPAM gene-level GFF annotations from PlasmoDB release 68 include 185 and 322 pseudogene records respectively; the PvW1 release does not include any pseudogene calls (this is an annotation gap inherited from Minassian et al., 2021, not a biological claim). Extracting the nucleotide sequences of the pseudogenic transcripts, translating in all six reading frames, and searching the translations with the PF05795 HMM at E < 10⁻³ identifies 75 of the 185 PvP01 pseudogenes and 70 of the 322 PvPAM pseudogenes as VIR-family pseudogenes. The PvP01 set is a perfect subset of the 119 PvP01 pseudogenes that PlasmoDB product-labels as PIR/VIR, with the 44 product-labeled-but-HMM-missed cases representing severely fragmented pseudogenes that have lost detectable PF05795 signal. The PvPAM pseudogenes carry no product annotation in the GFF, so the HMM-based count of 70 is the only available characterization for that genome.

**Table 1. Reference assemblies characterized in this study.**

| Property | PvP01 | PvW1 | PvPAM |
| --- | --- | --- | --- |
| Geographic origin | Papua, Indonesia | Thailand | Peruvian Amazon |
| Reference accession (NCBI) | GCA_900093555.2 | GCA_914969965.1 | GCA_949152365.1 |
| Sequencing technology | Illumina (high depth) + manual curation | PacBio + Illumina (hybrid) | PacBio (Ultra-Low Input) |
| Year | 2016 | 2021 | 2023 |
| Total annotated proteins (PlasmoDB v71) | 6,523 | 6,075 | 6,462 |
| VIR proteins identified by Pfam HMM (PF05795) | 931 | 748 | 985 |
| Contigs bearing at least one VIR | 130 | 17 | 26 |
| Largest contig | 3.2 Mb | 3.7 Mb | 3.3 Mb |
| VIRs on the 14 largest contigs ("main chromosomes") | 347 (37%) | 634 (85%) | 735 (75%) |
| VIRs on small subtelomeric contigs | 584 (63%) | 114 (15%) | 250 (25%) |
| Combined main-chromosome length | 23.5 Mb | 27.7 Mb | 27.4 Mb |
| Pseudogenes (any family) annotated in PlasmoDB release 68 GFF | 185 | 0 (not annotated) | 322 |
| VIR-family pseudogenes (PF05795 hits on 6-frame translation, E < 10⁻³) | 75 | not determinable | 70 |

The most important practical consequence of this table is that PvP01 places only 37% of its identified VIR proteins on main chromosomes. The remaining 584 PvP01 VIRs sit on small subtelomeric contigs (<200 kb each) that the original Illumina assembly was unable to scaffold into the main chromosomes. PvW1 and PvPAM, both produced with PacBio long reads, retain 75-85% of their VIR repertoire on the main chromosomes. This affects every spatial statistic that follows: PvP01's apparent subtelomeric distribution and chromosome-to-chromosome distribution metrics are confounded by its high contig count, and the long-read assemblies should be considered authoritative for those measurements. Sequence- and structure-level characterization (clustering, phylogeny, orthology) is largely unaffected, because those analyses operate on protein sequences and not on chromosomal context.

A direct comparison to the historical Salvador-I reference is not attempted here. The Sal-I assembly contains 2,747 scaffolds and lacks the contiguity needed for the spatial and orthology analyses below. The Lopez-Perez et al. (2013) re-analysis of Sal-I revised the original 346 *vir* gene count downward (concluding that subfamilies A, D, and H were assembly artifacts rather than true *vir* genes), and modern long-read assemblies have shown that the true *P. vivax* VIR repertoire contains over a thousand functional copies per genome. Salvador-I therefore serves as historical reference but not as a peer dataset.

## Structural classes

A central characterization question for any large multigene family is "how many distinct kinds of members does it contain?" Because *vir* proteins are too divergent in sequence for conventional clustering to give a meaningful answer (median pairwise identity within FS_001 is around 30-40%), we used Foldseek's `easy-cluster` workflow with ProstT5 encoding. The workflow runs an all-versus-all structural homology search of the input proteins against themselves and then groups them with a greedy set-cover algorithm (Steinegger & Söding, 2018, *Nat. Commun.* 9:2542) on the resulting graph of pairwise similarities. The 3Di alphabet representation respects the conserved PIR fold even where amino acid identity has been lost. This approach respects the conserved PIR fold even where sequence similarity has been lost.

The 2,664 HMM-identified VIRs from the three assemblies were clustered together. Foldseek produced 73 clusters containing three or more proteins, which we labeled FS_001 through FS_073 in decreasing order of size. The size distribution is heavily skewed: FS_001 alone contains 1,197 proteins, or 46% of the entire family. FS_002 through FS_005 add another 912 proteins (35% of the family). The remaining 68 clusters together hold the final 19% of the family, mostly as small clusters of two to thirty members.

**Table 2. Top structural classes and their per-genome composition.**

| Cluster | Total | PvP01 | PvW1 | PvPAM | Fraction of total VIR family |
| --- | --- | --- | --- | --- | --- |
| FS_001 | 1,197 | 400 | 349 | 448 | 46.2% |
| FS_002 | 385 | 126 | 101 | 158 | 14.9% |
| FS_003 | 248 | 77 | 78 | 93 | 9.6% |
| FS_004 | 143 | 53 | 41 | 49 | 5.5% |
| FS_005 | 136 | 48 | 37 | 51 | 5.2% |
| FS_006 | 96 | 28 | 33 | 35 | 3.7% |
| FS_007 | 85 | 39 | 20 | 26 | 3.3% |
| FS_008 | 74 | 31 | 18 | 25 | 2.9% |
| FS_009 | 53 | 20 | 16 | 17 | 2.0% |
| FS_010 | 36 | 15 | 7 | 14 | 1.4% |
| (top 10 subtotal) | 2,453 | 837 | 700 | 916 | 94.6% |
| FS_011-FS_073 | 139 | (rest) | (rest) | (rest) | 5.4% |

A comparison to the historical A-L subfamily classification of Salvador-I is informative but only partially possible: 89 of the 146 sequence-only subfamilies that we generated as a baseline (Plan A) collapse into FS_001 alone. The baseline was produced with MMseqs2 (Steinegger & Söding, 2017, *Nat. Biotechnol.* 35:1026), a fast sensitive protein sequence search tool, to compute an all-versus-all bitscore matrix, followed by the Markov Clustering Algorithm (MCL; van Dongen, 2008, *SIAM J. Matrix Anal. Appl.* 30:121), a graph-based clustering algorithm that groups proteins by simulating random walks on the similarity network with inflation parameter 2.0, indicating that several of the historical subfamilies that Lopez-Perez et al. (2013) treated as distinct are members of a single structural class. A full mapping of the original A-L assignments to our FS clusters would require running the Sal-I VIR sequences through the same clustering pipeline and is left as a follow-up.

The cross-assembly composition of the structural classes is informative on its own. Twenty-one of the 73 clusters strictly contain members from all three reference genomes. Three more clusters contain members from PvP01 and PvPAM only, one from PvW1 and PvPAM only, and one from PvP01 and PvW1 only. The remaining 47 clusters appear in only a single genome each, but together account for only 52 proteins (2.0% of the family) and are almost all singletons or pairs of closely related sequences. Weighted by membership, 2,523 of the 2,592 clustered proteins (97.3%) fall into the 21 strictly universal clusters. In other words, the structural classification of the *P. vivax* VIR family is essentially universal: a small number of large structural classes account for the bulk of the family in every assembly, and the apparent assembly-specific clusters reflect rare variants rather than independently-evolved structural classes.

## Genomic organization

The protein-level census above is independent of where the genes live in the genome. To characterize the spatial organization of the family across the three assemblies, we mapped each VIR to its chromosomal coordinates, restricted attention to the 14 largest contigs per genome (the "main chromosomes"), and quantified subtelomeric concentration, per-cluster chromosomal distribution, and conservation of distribution across assemblies.

The basic spatial fact is that VIRs are concentrated at chromosome ends. Across all three assemblies, 64.5% of main-chromosome VIRs lie in the outer 10% of their chromosome by length, against a uniform-distribution expectation of 20%. Per-assembly enrichment is strongest in PvP01 (80% of main-chromosome VIRs in the outer 10%) and progressively weaker in PvW1 (64%) and PvPAM (57%). The PvP01 number is partly an artifact of its smaller main-chromosome footprint (only 347 VIRs on 23.5 Mb of main chromosome, vs 634/27.7 Mb for PvW1 and 735/27.4 Mb for PvPAM): the densely-VIR-bearing subtelomeric blocks that PvW1 and PvPAM place inside their main chromosomes are partially split off onto small contigs in PvP01.

Within the subtelomeric blocks, members of the same structural class do not form tandem arrays. Permutation tests for tandem clustering of same-cluster members against random label shuffles return only 2 significant results out of 32 (cluster, genome) tests at p < 0.05, consistent with chance under multiple testing. However, when we examine all VIR-VIR pairs within 50 kb of each other on the same chromosome, the fraction in which both members belong to the same structural class is consistently higher than expected: 35% / 31% / 32% observed in PvP01 / PvW1 / PvPAM against expectations of 20% / 24% / 23% under random assignment of clusters to subtelomeric positions. So structural classes co-occupy similar subtelomeric neighborhoods (with a 1.3-1.7-fold enrichment), but they are interleaved with members of other classes rather than forming pure tandem blocks.

A striking cross-assembly observation is that the per-cluster chromosomal footprint is highly conserved between genomes. The number of main chromosomes occupied by each universal cluster correlates with Spearman ρ (a rank-based correlation coefficient that captures monotonic association without assuming linearity) ≈ 0.91 between all three pairs of genomes (PvP01 vs PvW1, PvP01 vs PvPAM, PvW1 vs PvPAM). A cluster that lives on many chromosomes in PvP01 lives on many in PvW1 and PvPAM as well, and vice versa. FS_001, the dominant class, is present on all 14 main chromosomes in all three genomes, with 137 / 284 / 320 members on main chromosomes in PvP01 / PvW1 / PvPAM. The relative-position density of FS_001 members along chromosomes is essentially identical to that of all other VIRs taken together and is consistent across assemblies. The structural and spatial signatures of the family, in other words, are conserved features of *P. vivax*: they are not properties of any individual lineage.

## Cross-assembly orthology of VIR genes

The fine-grained question that follows from these results is whether individual VIR genes can be confidently mapped 1-to-1 across the three assemblies, and how often that succeeds. We approached this between the two long-read assemblies (PvW1 and PvPAM) because their subtelomeric contiguity is sufficient to support microsynteny analysis; PvP01 was excluded because its fragmentation into many small subtelomeric contigs destroys the gene-order context needed for microsynteny verification.

Reciprocal best hits (RBH; the standard operational definition of potential orthologs between two genomes, where two proteins A in genome 1 and B in genome 2 are reciprocal best hits if B is the best match for A in genome 2 and A is the best match for B in genome 1) using MMseqs2 within FS_001 recover 194 PvW1 vs PvPAM pairs with E < 10⁻⁵, identity ≥ 30%, and mutual coverage ≥ 50%. To distinguish true 1-to-1 orthologs from paralog-best-hits we cross-checked each pair against two additional evidence layers. First, the housekeeping-protein RBH backbone of 5,120 non-VIR ortholog pairs between PvW1 and PvPAM, asking whether each FS_001 pair's flanking non-VIR neighbors are themselves housekeeping orthologs (microsynteny score 0-4). Microsynteny refers to the conservation of local gene order across genomes (Sonnhammer & Koonin, 2002, *Trends Genet.* 18:619): if two genes are true orthologs descended from a single ancestral gene, their immediate genomic neighbors should also be 1-to-1 orthologs more often than if the apparent orthology had resulted from independent duplications. Second, the FS_001 phylogeny from Plan C Q2, asking whether the pair forms reciprocally nearest-neighbor (sister) leaves on the AA tree (computed with Biopython's `Bio.Phylo` module, Cock et al., 2009, *Bioinformatics* 25:1422).

The microsynteny result is the most informative: 139 of the 194 RBH pairs (72%) have zero matching flanking orthologs, meaning the local gene neighborhoods around them have been completely rearranged between PvW1 and PvPAM. Only 11 RBH pairs (6%) have three or four of four flanking neighbors preserved as housekeeping orthologs. These 11 high-confidence ortholog candidates also have substantially higher sequence identity (median 87%, range 70-99.7%) than the bulk of the RBH set (median 74.5%), and several appear in clusters of consecutive gene IDs in both genomes (e.g., `CAG9483870` / `CAG9483878` / `CAG9483882` in PvW1 map to `CAI7717859` / `CAI7717862` / `CAI7717863` in PvPAM), suggesting they sit in the rare subtelomeric neighborhoods where local gene order is preserved between Thailand and Peru. These 11 pairs are the strongest within-FS_001 1-to-1 ortholog candidates available between PvW1 and PvPAM and are documented in `data/genomes/alignments/ortho/orthologs_high_confidence.tsv`.

The methodological implication is concrete and useful for downstream work on the family: reciprocal best hits alone do not establish orthology for subtelomeric VIR genes, because the subtelomeric environment is dynamic enough that paralogs frequently outscore the true ortholog. Microsynteny verification against a housekeeping-protein RBH backbone is a necessary additional filter. For a typical biological question that needs orthologs (e.g., "is this PvW1 gene the equivalent of that PvPAM gene?") the operational answer is that high-confidence orthology is available for roughly 6% of the FS_001 RBH set, or about 11 genes out of the ~349 PvW1 FS_001 members.

For the housekeeping (non-VIR) backbone, the situation is completely different: 5,120 RBH pairs between PvW1 and PvPAM at high identity (median 99.8%), confirming that the two lineages are evolutionarily close and that the difficulty of VIR orthology is a property of the family, not of the assemblies.

## Within-class diversity

For the dominant structural class FS_001 (1,197 proteins, 46% of the family), we examined the within-class sequence diversity directly. A 50% sequence-identity subsampling of FS_001 with MMseqs2 `easy-cluster` (the same tool used for the Plan A baseline, here run with `--min-seq-id 0.5 -c 0.8` to pick a representative for each group of sequences sharing >=50% identity over >=80% mutual coverage) retained 338 representative sequences (118 PvP01, 110 PvW1, 110 PvPAM, a balanced cross-continental sample). Maximum-likelihood phylogenies of these 338 representatives were inferred with IQ-TREE 3 on (a) the AA alignment alone (ModelFinder selected VT+F+R6, i.e. the VT amino acid exchangeability matrix of Müller & Vingron, 2000, *J. Comput. Biol.* 7:761, with empirical state frequencies and a 6-category FreeRate model of among-site rate variation); (b) the 3Di alignment using the Garg & Hochberg 2025 substitution matrix (*Mol. Biol. Evol.* 42:msaf124), the first general substitution model published for the 3Di alphabet, in NEXUS format from the [`jonasmehl1/structural_phylogenetics`](https://github.com/jonasmehl1/structural_phylogenetics) repository; and (c) a partitioned AA + 3Di analysis. Each tree was inferred with 1000 ultrafast bootstrap replicates (UFBoot; Hoang et al., 2018, *Mol. Biol. Evol.* 35:518, a fast resampling procedure for branch support) and 1000 SH-aLRT replicates (Anisimova & Gascuel, 2006, *Syst. Biol.* 55:539, an approximate likelihood-ratio test that complements UFBoot).

The within-FS_001 sequence diversity is high and not partitioned by geographic origin. Tips from the three genomes are evolutionarily interleaved across all three trees: the median parsimony score for "genome of origin" mapped onto each tree is 160 transitions, identical to the median under 1000 random shuffles of the tip labels, and far above the minimum-possible value of 2 (corresponding to a single monophyletic clade per genome). Counting internal nodes whose descendants all came from a single genome gave 34 to 37 out of 336 internal nodes (10-11%), no more than expected by chance for three states distributed evenly across tips. The phylogenetic signature is consistent with what would be expected if the sequence diversity within FS_001 had been generated before the geographic separation of the three *P. vivax* lineages represented here, and had then been maintained subsequently by recombination and gene conversion within and between subtelomeric *vir* loci that operates faster than geographic isolation can partition the family.

A family-level phylogeny on the 73 Foldseek cluster representatives (Plan C Q1) did not resolve deep relationships between the structural classes cleanly, even after switching to trimAl's `-automated1` column-filtering mode (Capella-Gutiérrez et al., 2009, *Bioinformatics* 25:1972; trimAl removes poorly-aligned columns from an MSA, and `-automated1` is the heuristic designed for downstream maximum-likelihood phylogeny on diverged sequences) to retain 749 columns of the original 1,521. This is unsurprising: the 73 cluster representatives are by construction the most structurally divergent proteins in the family from each other, and the deep nodes connecting these distant lineages are not strongly resolved by either AA or 3Di phylogenetics at this scale. The relationships within each structural class (as illustrated by the FS_001 analysis above) are more informative than the relationships between classes.


## Methods

### Data sources

Genome assemblies, protein FASTAs, and gene-level GFF annotations for all three reference genomes were downloaded from PlasmoDB release 68/71 (Amos et al., 2022, *Nucleic Acids Res.* 50:D898) at `https://plasmodb.org/common/downloads/Current_Release/{PvivaxP01,PvivaxPvW1,PvivaxPAM}/{fasta,gff}/data/`. The 3Di substitution matrix in NEXUS format was sourced from the [`jonasmehl1/structural_phylogenetics`](https://github.com/jonasmehl1/structural_phylogenetics) repository (originally from Garg & Hochberg 2025, *Mol. Biol. Evol.* 42:msaf124). The Pfam HMM PF05795 ("Plasmodium_Vir") was fetched from Pfam-A.hmm (Mistry et al., 2021, *Nucleic Acids Res.* 49:D412) via `hmmfetch`.

### VIR protein identification

For each genome, all annotated proteins in the PlasmoDB protein FASTA were searched with `hmmsearch` from HMMER 3.4 (Eddy, 2011, *PLoS Comput. Biol.* 7:e1002195) against PF05795. Proteins passing the default per-sequence threshold were considered VIR-family. This identified 931 / 748 / 985 functional VIR proteins in PvP01 / PvW1 / PvPAM respectively, summing to 2,664 across the three genomes.

### Pseudogene characterization

Pseudogenes are absent from the protein FASTAs by construction (only translated coding sequences are released as proteins) so a separate workflow was needed to characterize them. For each genome:

1. **Identify pseudogene records.** All `pseudogenic_transcript` features were extracted from the PlasmoDB release 68 GFF along with their constituent exon coordinates (chromosome, start, end, strand).
2. **Extract nucleotide sequences.** Each pseudogenic transcript's exon sequence was extracted from the genome FASTA, exons concatenated in genomic-coordinate order, and reverse-complemented if encoded on the minus strand.
3. **Six-frame translation.** Each pseudogenic transcript nucleotide sequence was translated in all six reading frames (three forward, three reverse-complement) using the standard genetic code. Stop codons were translated as `*` and retained in the resulting amino acid sequences (since pseudogenes frequently contain premature stops).
4. **HMM search.** All six-frame translations of length ≥50 amino acids were searched with `hmmsearch` against PF05795 at E ≤ 10⁻³.
5. **Per-pseudogene call.** A pseudogenic transcript was classified as a VIR-family pseudogene if any of its six-frame translations produced a significant hit. The PvP01 result (75 VIR-family pseudogenes out of 185 total) is a strict subset of the 119 PvP01 pseudogenes that PlasmoDB independently product-labels as PIR/VIR, validating the HMM-based approach.

This workflow returns 75 VIR-family pseudogenes for PvP01 and 70 for PvPAM. PvW1's PlasmoDB release does not include any pseudogene annotations, so the same workflow cannot be applied; the corresponding cell in Table 1 is therefore "not determinable" rather than "0."

### Structural clustering

The 2,664 VIR proteins were combined into a single FASTA and clustered with `foldseek easy-cluster` (Foldseek v10.941cd33; van Kempen et al., 2024, *Nat. Biotechnol.* 42:243) using `--prostt5-model` to encode the 3Di structural alphabet on-the-fly from the amino acid sequence (ProstT5 weights downloaded with `foldseek databases ProstT5`; Heinzinger et al., 2024, *NAR Genom. Bioinform.* 6:lqae150). Clustering parameters: `-c 0.8 -e 0.001 --alignment-type 2` (combined 3Di+AA alignment, 80% mutual coverage, E ≤ 10⁻³). Output clusters were re-named FS_001 through FS_073 in decreasing size order. As a sequence-only baseline, the same 2,664 proteins were also clustered with `mmseqs easy-search` followed by Markov Clustering (MCL v22.282; van Dongen, 2008, *SIAM J. Matrix Anal. Appl.* 30:121) at inflation 2.0.

### Spatial analysis

Gene coordinates were parsed from the `location=` field of the protein FASTA headers. The 14 largest contigs per genome were designated "main chromosomes" and used for spatial statistics to control for the differing subtelomeric fragmentation across the three assemblies. Subtelomeric enrichment was quantified as the fraction of main-chromosome VIRs lying within the outer 10% of their chromosome's length. Tandem clustering of same-cluster members was tested by computing, for each (cluster, genome) pair with ≥2 same-chromosome members, the mean distance from each VIR to the nearest same-cluster VIR on the same chromosome, compared against the distribution of the same statistic across 500 random shuffles of cluster labels within the genome. Cross-genome spatial-signature conservation was assessed by computing per-cluster summary statistics (number of main chromosomes occupied; median relative distance to chromosome end; fraction in outer 10%) and computing Spearman rank correlations between pairs of genomes over the 21 universally-shared clusters.

### Phylogenetic inference

FoldMason v4 (Gilchrist et al., 2026, *Science*, doi:10.1126/science.ads6733) was used for multiple structural sequence alignment via `foldmason structuremsa` against the Foldseek database, producing aligned amino acid and 3Di sequences in lockstep. Within FS_001, a 50% sequence-identity subsample (338 sequences) was generated with `mmseqs easy-cluster --min-seq-id 0.5 -c 0.8` before alignment. Alignments were trimmed with trimAl 1.5 (Capella-Gutiérrez et al., 2009, *Bioinformatics* 25:1972) using `-gt 0.65` for FS_001 (paper-standard cutoff) and `-automated1` for the family-level set (where the per-class divergence is much higher). Maximum-likelihood trees were inferred with IQ-TREE 3.1.2 (Minh et al., 2020, *Mol. Biol. Evol.* 37:1530, describing the IQ-TREE 2 methodology) using ModelFinder (Kalyaanamoorthy et al., 2017, *Nat. Methods* 14:587) for AA model selection and the Garg & Hochberg 2025 substitution matrix (`-mdef 3DI.nexus -m 3DI+G`) for 3Di trees. Each tree was inferred with `-B 1000 --bnni --alrt 1000 -T 8 --safe --seed 42` (1000 ultrafast bootstrap replicates with NNI refinement, 1000 SH-aLRT replicates, 8 threads, fixed random seed). The genome-of-origin test for the FS_001 tree treated genome as a three-state discrete character and computed its parsimony score using `phangorn::parsimony`, compared against 1000 random permutations of the tip labels.

### Cross-assembly orthology

Reciprocal best hits between the 349 PvW1 and 448 PvPAM members of FS_001 were computed with `mmseqs easy-rbh` (Steinegger & Söding, 2017, *Nat. Biotechnol.* 35:1026) using `--min-seq-id 0.3 -c 0.5 -e 1e-5`. A housekeeping ortholog backbone between the non-VIR proteomes of PvW1 and PvPAM was computed with the same tool at stricter thresholds (`--min-seq-id 0.5 -c 0.8 -e 1e-10`). For each FS_001 RBH pair, the 2 upstream and 2 downstream non-VIR neighbors of each member were identified by sorting all annotated proteins by chromosomal position; microsynteny score was defined as the number of those 4 PvW1 flanking neighbors whose housekeeping-RBH ortholog appeared among the 4 flanking neighbors of the PvPAM partner. Confidence classes were assigned as: high = microsynteny ≥ 3 AND identity ≥ 50% AND (not in Plan C Q2 tree OR sister leaves); medium = microsynteny ≥ 2 OR sister leaves; low = otherwise. Sister-leaf relationships on the Q2 AA tree were computed by walking the tree topology with `Bio.Phylo` (Cock et al., 2009, *Bioinformatics* 25:1422) and assigning each leaf to its reciprocally-nearest leaf.

### Computational environment

All analyses ran on macOS arm64 with conda-managed dependencies. Key tools and versions: HMMER 3.4, MMseqs2 18.8cc5c, Foldseek 10.941cd33, FoldMason 4.dd3c235, MCL 22.282, trimAl 1.5.rev1, IQ-TREE 3.1.2, R 4.4 with `ape`, `treeio`, `ggtree`, `phangorn`, Python 3.11 with `pandas`, `scipy`, `matplotlib`, `seaborn`, `biopython`.

## Galaxy implementation

To translate this structure-aware phylogenomics workflow into a standard Galaxy pipeline, the analytical steps can be split into two classes based on their availability in the current Galaxy ecosystem (usegalaxy.org and the IUC ToolShed):

### Standard ToolShed integrations
The sequence-based, standard phylogenomics components can be executed directly using official IUC-wrapped tools:
1. **Functional PIR Identification:** Executed using the standard `hmmsearch` tool (`toolshed.g2.bx.psu.edu/repos/iuc/hmmer_hmmsearch/hmmer_hmmsearch/3.4+galaxy0`) against custom-uploaded or pre-indexed HMM database files (`PF05795`).
2. **Subsampling and RBH Ortholog Candidate Generation:** Executed using MMseqs2 clustering and sequence-search tools (`toolshed.g2.bx.psu.edu/repos/iuc/mmseqs2_easy_linclust_clustering/mmseqs2_easy_linclust_clustering/17-b804f+galaxy1`).
3. **Phylogenetic Tree Construction:** Executed using IQ-TREE 2/3 (`toolshed.g2.bx.psu.edu/repos/iuc/iqtree/iqtree/2.4.0+galaxy2`), which has built-in ModelFinder and supports the upload and use of custom substitution matrices (such as the Garg & Hochberg 2025 3Di substitution matrix).

### Custom User-Defined Tool (UDT) requirements
The more specialized, structure-aware steps of the pipeline utilize emerging methods that are not yet packaged in the standard ToolShed. In a modern Galaxy instance, these can be incorporated natively as containerized **User-Defined Tools (UDTs)** without requiring administrative privileges:
1. **Foldseek Structural Clustering (v10.941cd33):** Requires a containerized UDT utilizing the official `foldseek` Docker image, loaded with the pre-compiled ProstT5 language model weights to encode amino acid sequences into 3Di alphabets on-the-fly and perform structural set-cover clustering.
2. **FoldMason Structural MSA (v4):** Requires a UDT wrapping the `foldmason` container to perform lockstep alignments of amino acids and 3Di structural sequences.
3. **Flanking Microsynteny Filtering:** Implemented via a lightweight Python-based UDT that takes the MMseqs2 RBH candidate pairs and cross-references their neighboring genes against the non-VIR housekeeping-RBH backbone.
4. **Pseudogene Rescue GFF Parser:** Implemented as a custom python tool that parses GFF3 annotations, extracts pseudogenic transcripts, translates them in all 6 reading frames, and streams the output to HMMER.
5. **Spatial permutation tests:** A custom tool executing nearest-neighbor distance label-shuffling tests to verify physical tandem cluster co-localization.

The complete tool execution ledger, input/output mappings, parameter sets, and the raw Python and R code blocks representing the custom-tool logic are fully documented in the standalone file `pipeline.md`. This blueprint allows a researcher to either execute the pipeline locally using a Conda environment or wrap the steps as a highly reproducible, sharing-enabled Galaxy workflow.

## Summary

Three high-quality reference assemblies of *P. vivax* -- PvP01 from Indonesia, PvW1 from Thailand, and PvPAM from Peru -- support a coherent characterization of the PIR/VIR family that differs in several important respects from the picture available from the historical Salvador-I reference. The family contains approximately 750-1000 functional members per genome (with the exact number depending on assembly contiguity); these resolve into approximately ten major structural classes plus a long tail of rare variants; one structural class, FS_001, accounts for 46% of the entire family by itself; 97% of all VIR proteins fall into the 21 structural classes that are universally represented across the three continents; the family occupies all 14 main chromosomes in each assembly, concentrated at chromosome ends but interleaved by structural class rather than tandemly arrayed; the per-cluster spatial distribution is conserved across assemblies (Spearman ρ ≈ 0.91 between any two genomes); and within the dominant structural class, the sequence diversity is high but not partitioned by geographic origin -- consistent with a family whose diversification predates the modern *P. vivax* lineages and that continues to homogenize through subtelomeric recombination.

The orthology analysis quantifies how much of this family-level conservation translates into individual-gene conservation across the long-read assemblies: only about 6% of within-FS_001 reciprocal best hits between PvW1 and PvPAM survive a microsynteny verification step and qualify as high-confidence 1-to-1 orthologs. The remaining 94% of RBH pairs are best explained as paralog-best-hits, in which the closest match in the other genome is not the true ortholog but a related paralog from the same structural class. For methodological purposes this means that orthology in the VIR family cannot be inferred from sequence similarity alone, even with reciprocal best hits, and that confirmatory tests using microsynteny against a non-VIR ortholog backbone are necessary.

The natural next steps are: (i) extending the same pipeline to the Salvador-I reference, ideally after re-assembly with long reads, to bridge the historical A-L subfamily nomenclature to the FS_001-FS_073 structural classes; (ii) layering published transcriptome and proteome data over the structural classes, to ask whether stage-specific or condition-specific expression patterns are consistent with structural class membership; and (iii) repeating the cross-assembly characterization on additional *P. vivax* lineages from underrepresented regions (in particular Africa) to test whether the cross-continental conservation observed here generalizes to lineages not yet sampled.










## Galaxy Step 3/4 Reproducibility Findings

Recent Galaxy reruns of Plan F Steps 3 and 4 clarified the source of the pseudogene-count discrepancy.

Step 3 was successfully executed natively on Galaxy using a BioContainers-backed UDT, `anton-1-gff_pseudogene_translator` version 1.0.2, with container `quay.io/biocontainers/python:3.12.12` and output binding `from_work_dir: translated_pseudogenes.fasta`. The two BioContainers UDT outputs reached `ok`: PvP01 HID 46 / HDA `f9cad7b01a4721359c223f5fa5d69e8c` contained 1,110 translated pseudogene fragments, and PvPAM HID 47 / HDA `f9cad7b01a47213574689e772059517e` contained 1,932 fragments. These record counts match the local Step 3 counts.

However, the BioContainers UDT FASTAs were not byte-identical to the historical local FASTAs. The record IDs and record counts matched, but many translated sequences differed. The cause is the translation script's use of `sorted(set(exons), key=lambda e: e[1])`, which is nondeterministic when a `pseudogenic_transcript` record and a child `exon` record share the same start coordinate. Different Python/runtime ordering can change whether the full transcript segment or exon segment is stitched first, which changes translated amino acid sequences and downstream HMMER hits.

Step 4 HMMER searches against the BioContainers UDT FASTAs completed successfully on Galaxy with `hmmsearch` 3.4+galaxy0 using `-E 1e-3 --domE 10.0` and default inclusion thresholds. The resulting raw per-sequence hit sets did not reproduce the historical local pseudogene counts: PvP01 yielded 107 translated-frame hits collapsing to 72 unique pseudogenic transcript loci, and PvPAM yielded 91 translated-frame hits collapsing to 75 loci. Therefore those outputs are valid Galaxy products but not exact reproductions of the local baseline.

Step 4 was then rerun using the previously uploaded local fallback Step 3 FASTAs, which are byte-identical to the local translation files. PvP01 reproduced the expected locus count: HMMER outputs HIDs 54-56, per-sequence tblout HDA `f9cad7b01a472135d491d831288295f7`, gave 109 translated-frame hits collapsing to 75 unique loci. PvPAM did not reproduce the historical 70-locus claim: HMMER outputs HIDs 57-59, per-sequence tblout HDA `f9cad7b01a472135b098eb058958d668`, gave 87 reported rows and 69 unique loci in the Galaxy report; filtering strictly by full-sequence E-value <= 1e-3 gives 65 unique loci.

Input integrity checks ruled out upload or file drift as the explanation: the Galaxy HMM, GFF, genome FASTA, and fallback PvPAM pseudogene translation FASTA are byte-identical to their local counterparts. A fresh local rerun with the current HMMER 3.4 toolchain on the current PvPAM FASTA gives 65 unique loci, whereas the older checked-in table `data/pseudogenes/PvPAM_pseudo_PF05795.tbl` gives 70. Thus the PvPAM value of 70 is stale relative to the current reproducible toolchain, while the PvP01 value of 75 remains reproducible.

Interpretation: Plan F Step 3 is operational on Galaxy, but exact reproduction of the historical local translation FASTAs requires either preserving the old nondeterministic ordering or rewriting the extractor to use a biologically explicit deterministic rule and then updating downstream counts. Plan F Step 4 should remain pending until the project decides whether to preserve the historical 75/70 counts or revise the PvPAM pseudogene count under the current deterministic/reproducible workflow.

## Deterministic Step 3/4 Rerun

A deterministic revision of the pseudogene translation UDT was registered as `anton-1-gff_pseudogene_translator` version 1.0.3, UUID `0d69090e-0924-41e3-9146-8f8da395e1af`, using BioContainers image `quay.io/biocontainers/python:3.12.12`. The revised logic uses child exon coordinates when present, falls back to the `pseudogenic_transcript` span only when child exons are absent, and sorts intervals deterministically by `(seqid, start, end, strand)` before stitching and six-frame translation.

Local preflight of this deterministic extractor produced 1,110 PvP01 translations and 1,932 PvPAM translations. HMMER 3.4 preflight at `-E 1e-3 --domE 10.0` predicted 83 strict full-sequence E-value loci for PvP01 and 78 for PvPAM.

Native Galaxy execution of the deterministic UDT was attempted twice for both PvP01 and PvPAM. All four native UDT output datasets failed before Python execution due the Galaxy container runtime, not due the script: Apptainer/proot failed while building the SIF from `docker://quay.io/biocontainers/python:3.12.12` with `ptrace(TRACEME): Operation not permitted`. Failed native deterministic UDT outputs were HIDs 60-63.

To complete the deterministic Step 3/4 rerun despite the container-layer failure, the locally generated deterministic FASTAs were uploaded to Galaxy and verified there: PvP01 HID 64 / HDA `f9cad7b01a472135cfaeca4bfcae4497` (`ok`, 1,110 sequences), and PvPAM HID 65 / HDA `f9cad7b01a472135f05c2b7e64d5d0e6` (`ok`, 1,932 sequences).

Step 4 HMMER was rerun on these deterministic FASTAs on Galaxy using `toolshed.g2.bx.psu.edu/repos/iuc/hmmer_hmmsearch/hmmer_hmmsearch/3.4+galaxy0` with `-E 1e-3 --domE 10.0`, default inclusion thresholds, and `--seed 42`. PvP01 outputs were HIDs 66-68, with per-sequence tblout HDA `f9cad7b01a4721351fa16d308819f9ac`. PvPAM outputs were HIDs 69-71, with per-sequence tblout HDA `f9cad7b01a47213598ca8cb8a735a0f2`. All HMMER outputs reached `ok`.

Verified deterministic Step 4 counts: PvP01 had 88 reported tblout rows / 88 translated-frame targets / 87 unique pseudogenic transcript loci in the raw Galaxy report, and 84 strict full-sequence E-value rows / 84 targets / 83 unique loci at full-sequence E <= 1e-3. PvPAM had 82 reported rows / 82 targets / 82 unique loci in the raw Galaxy report, and 78 strict rows / 78 targets / 78 unique loci at full-sequence E <= 1e-3.

Interpretation: the deterministic, biologically explicit Step 3/4 workflow gives reproducible counts of 83 PvP01 and 78 PvPAM VIR-family pseudogene loci under strict full-sequence E <= 1e-3. This differs from the historical 75/70 counts because the old translation workflow had nondeterministic interval ordering and the old PvPAM HMMER table is stale relative to the current FASTA/HMMER 3.4 toolchain. Plan F Step 5 has not been started and awaits user approval.

## Step 5 Galaxy Foldseek/ProstT5 UDT Run

Plan F Step 5 was started after user approval. The GPU/XL UDT was registered as `anton-gpu-xl-foldseek_prostt5_clustering`, using the naming convention that routes jobs to 32 CPU cores and a GPU. The first version, UUID `006d1a86-6d84-40d2-b8b9-bd57e58e084e`, failed during Galaxy command-line construction because shell `${...}` syntax conflicted with UDT templating.

A corrected UDT version 1.0.1 was registered with UUID `c41d41c6-f14e-45b0-ad6f-a8353a4eab06`. It uses BioContainers image `quay.io/biocontainers/foldseek:10.941cd33--h5021889_1`, accepts `combined_vir.fasta` and `prostt5-f16.gguf` as inputs, and exposes the local Foldseek parameters: coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=32`.

Inputs uploaded/used for the Step 5 run:
- Combined VIR protein FASTA: HID 72 / HDA `f9cad7b01a472135280107cef6d12de2`, state `ok`.
- ProstT5 GGUF model: HID 74 / HDA `f9cad7b01a472135dfae40ce8ed6d561`, state `ok`.

The corrected Step 5 UDT was submitted successfully. Outputs HIDs 80-84 were created and, after polling, entered `running` state:
- HID 80 / HDA `f9cad7b01a4721352f6733a6a39755d3`: Foldseek cluster assignments.
- HID 81 / HDA `f9cad7b01a472135b85d07d0bb9e894c`: representative sequences.
- HID 82 / HDA `f9cad7b01a472135b1315e3d499fda8f`: clustered sequences FASTA.
- HID 83 / HDA `f9cad7b01a4721358be8c9f558220cb8`: cluster summary.
- HID 84 / HDA `f9cad7b01a47213533cb7f1d8f79381f`: Foldseek clustering log.

Verification remains pending: once the job reaches `ok`, inspect the cluster assignment and summary outputs and verify that total structural clusters and the dominant FS_001 cluster size match the local baseline (73 clusters; FS_001 = 1,197 members). Step 6 has not been started.

## Step 5 GPU Route Restart

After the Galaxy GPU routing configuration for UDTs was corrected, the running Step 5 Foldseek/ProstT5 job was stopped and restarted without modifying the UDT definition or parameters.

Cancelled prior running job `bbd44e69cb8906b5879a74dfb6c50208`, which had produced HIDs 80-84. Galaxy marked those outputs as `discarded` after cancellation.

Restarted the same corrected UDT version 1.0.1, UUID `c41d41c6-f14e-45b0-ad6f-a8353a4eab06`, with the same inputs and parameters: combined VIR FASTA HID 72, ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=32`.

The restarted Step 5 outputs are running:
- HID 85 / HDA `f9cad7b01a47213591c3ea010474a904`: Foldseek cluster assignments.
- HID 86 / HDA `f9cad7b01a472135abf73bb499149fc1`: representative sequences.
- HID 87 / HDA `f9cad7b01a472135da88b07239b50258`: clustered sequences FASTA.
- HID 88 / HDA `f9cad7b01a4721351f71603cf5a80c47`: cluster summary.
- HID 89 / HDA `f9cad7b01a47213568470880bd8b785b`: Foldseek clustering log.

Verification remains pending until the restarted job reaches a terminal state.

## Step 5 UDT Container Rewrite for CVMFS Image

The Step 5 Foldseek/ProstT5 UDT was rewritten after Galaxy GPU/CVMFS configuration guidance. A new UDT version 1.0.2 was registered with the same ID, `anton-gpu-xl-foldseek_prostt5_clustering`, and UUID `ea5495a2-d735-4b22-a718-e0e9cf0bea1a`. The command, inputs, outputs, and parameters were left unchanged from the corrected v1.0.1 definition. The only intended change was the container identifier: `foldseek:10.941cd33`, without a `docker://quay.io/biocontainers/` prefix and without the BioContainers build suffix. This should cause Galaxy to use the preconverted CVMFS Foldseek image rather than trying to build a SIF from Docker layers at runtime.

The rewritten UDT has been registered and verified in Galaxy. It has not yet been run.

## Step 5 CVMFS Container Identifier Run Attempt

The rewritten Step 5 UDT version 1.0.2, UUID `ea5495a2-d735-4b22-a718-e0e9cf0bea1a`, was run after registration. It used the requested container identifier `foldseek:10.941cd33`, with no `docker://quay.io/biocontainers/` prefix and no BioContainers build suffix. Inputs and parameters were unchanged: combined VIR FASTA HID 72, ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=32`.

The run created outputs HIDs 90-94, all of which failed before Foldseek execution:
- HID 90 / HDA `f9cad7b01a472135e00af6ac4e398344`: cluster assignments, `error`.
- HID 91 / HDA `f9cad7b01a472135906c959be4e2abd6`: representative sequences, `error`.
- HID 92 / HDA `f9cad7b01a4721351c4288078592d55b`: clustered sequences FASTA, `error`.
- HID 93 / HDA `f9cad7b01a4721352e2231db6bb20f65`: cluster summary, `error`.
- HID 94 / HDA `f9cad7b01a4721355cfecea8d5a8c68d`: Foldseek clustering log, `error`.

Galaxy built the intended command line correctly, including `threads="32"`, `--prostt5-model prostt5_weights`, `-c 0.8`, `-e 0.001`, and `--alignment-type 2`. However, container resolution still failed before execution. The error was: `FATAL: Unable to handle docker://foldseek:10.941cd33 uri: failed to get checksum for docker://foldseek:10.941cd33: reading manifest 10.941cd33 in docker.io/library/foldseek: requested access to the resource is denied`.

Interpretation: Galaxy accepted the UDT container field as `foldseek:10.941cd33`, but the job runner/container resolver still transformed it into a Docker URI (`docker://foldseek:10.941cd33`) rather than resolving the preconverted CVMFS image. Step 5 remains unverified and pending until the runner's container resolver maps this identifier to the CVMFS image or the UDT uses whatever exact container string the resolver expects for CVMFS.

## Step 5 UDT Container Rewrite: Quay Short Tag

The Step 5 Foldseek/ProstT5 UDT was rewritten again after container resolver guidance. A new UDT version 1.0.3 was registered with the same ID, `anton-gpu-xl-foldseek_prostt5_clustering`, and UUID `d6f6c1dc-c8b7-46d7-9a6e-194199ef3fa9`. The command, inputs, outputs, and parameters were left unchanged from the corrected Foldseek UDT definition. The only intended change was the container identifier: `quay.io/biocontainers/foldseek:10.941cd33`, without the `docker://` prefix and without the BioContainers build suffix.

The rewritten UDT has been registered and verified in Galaxy. It has not yet been run.

## Step 5 Quay Short Tag Run

The Step 5 Foldseek/ProstT5 UDT version 1.0.3, UUID `d6f6c1dc-c8b7-46d7-9a6e-194199ef3fa9`, was run with container identifier `quay.io/biocontainers/foldseek:10.941cd33`. Inputs and parameters were unchanged: combined VIR FASTA HID 72, ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=32`.

The run submitted successfully and produced outputs HIDs 95-99. After polling, all five outputs were in `running` state, indicating that this attempt passed the earlier immediate container-resolution failure:
- HID 95 / HDA `f9cad7b01a47213567ec282917a40941`: Foldseek cluster assignments.
- HID 96 / HDA `f9cad7b01a47213585bbcf91cac22520`: representative sequences.
- HID 97 / HDA `f9cad7b01a472135fb240236ac0e3e1b`: clustered sequences FASTA.
- HID 98 / HDA `f9cad7b01a472135559d91b4f2ec519a`: cluster summary.
- HID 99 / HDA `f9cad7b01a472135ad41815b2fab8465`: Foldseek clustering log.

Galaxy job ID: `bbd44e69cb8906b5536b949f75b32cf7`; external job ID: `77927863`; current state at last poll: `running`. Verification remains pending until the job reaches `ok` and the cluster summary can be checked against the local baseline (73 clusters; FS_001 = 1,197 members).

## Step 5 Quay Short Tag GPU Restart

After Galaxy GPU access for the Foldseek UDT destination was corrected again, the running Step 5 v1.0.3 job was stopped and restarted without modifying the UDT definition or parameters.

Cancelled prior running job `bbd44e69cb8906b5536b949f75b32cf7`, which had produced HIDs 95-99. Galaxy marked those outputs as `discarded` after cancellation.

Restarted the same UDT version 1.0.3, UUID `d6f6c1dc-c8b7-46d7-9a6e-194199ef3fa9`, with the same inputs and parameters: combined VIR FASTA HID 72, ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=32`.

The restarted Step 5 outputs are running:
- HID 100 / HDA `f9cad7b01a4721357c71e677c4399e6b`: Foldseek cluster assignments.
- HID 101 / HDA `f9cad7b01a4721359db6f910fb32dc0d`: representative sequences.
- HID 102 / HDA `f9cad7b01a4721356750dfe813dd52d6`: clustered sequences FASTA.
- HID 103 / HDA `f9cad7b01a4721358eabf43dba9c25dc`: cluster summary.
- HID 104 / HDA `f9cad7b01a47213566e3033ac82b8f2d`: Foldseek clustering log.

Galaxy job ID: `bbd44e69cb8906b532096618f37c11e6`; external job ID: `77928105`; state at last poll: `running`. Verification remains pending until the job reaches a terminal state.

## Step 5 Explicit GPU Flag Restart

After confirming that the previous Foldseek UDT versions relied on Galaxy destination routing but did not pass a Foldseek GPU flag, the current Step 5 job was stopped and restarted with a new UDT version that explicitly includes `--gpu 1` in the `foldseek easy-cluster` command.

Cancelled prior running job `bbd44e69cb8906b532096618f37c11e6`, which had produced HIDs 100-104. Galaxy marked those outputs as `discarded` after cancellation.

Registered UDT version 1.0.4, UUID `6f088eba-8723-41ba-a209-93e8b1eae89a`, with the same ID `anton-gpu-xl-foldseek_prostt5_clustering`, the same container identifier `quay.io/biocontainers/foldseek:10.941cd33`, and the same inputs/outputs/parameters as v1.0.3, but with `--gpu 1` added to the `foldseek easy-cluster` command. The command still uses combined VIR FASTA HID 72, ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=32`.

Submitted the v1.0.4 GPU-explicit UDT. The new outputs are running:
- HID 105 / HDA `f9cad7b01a472135e8c5584b854bc036`: Foldseek cluster assignments.
- HID 106 / HDA `f9cad7b01a472135246a489d5bef23f1`: representative sequences.
- HID 107 / HDA `f9cad7b01a47213501471e25d494ab91`: clustered sequences FASTA.
- HID 108 / HDA `f9cad7b01a47213530e7cc97ef4696d9`: cluster summary.
- HID 109 / HDA `f9cad7b01a4721356657d2404d8596f6`: Foldseek clustering log.

Galaxy job ID: `bbd44e69cb8906b5503b85fa19998669`; external job ID: `77928363`; state at last poll: `running`. Verification remains pending until the job reaches a terminal state and outputs can be checked against the local Foldseek baseline.

## Step 5 v1.0.4 Error Diagnosis and No-Python Fix

The Step 5 GPU-explicit UDT v1.0.4 failed after Foldseek execution. HIDs 105-109 entered `error`; the creating Galaxy job was `bbd44e69cb8906b5503b85fa19998669`, external job ID `77928363`, exit code `127`. The relevant stderr/misc_info was: `/jetstream2/scratch/main/jobs/77928363/tool_script.sh: line 44: python: command not found`.

Interpretation: Foldseek produced non-empty primary outputs before the failure (cluster assignments, representative sequences, all-sequences FASTA, and log had non-zero sizes), but the post-processing block failed because the `quay.io/biocontainers/foldseek:10.941cd33` container does not include `python`. This was not a Foldseek/GPU failure; it was a UDT summary-generation dependency error.

Registered UDT version 1.0.5, UUID `43fa451a-3592-4cfa-80ea-c9f7d1afb772`, with the same ID `anton-gpu-xl-foldseek_prostt5_clustering`, same container identifier `quay.io/biocontainers/foldseek:10.941cd33`, same inputs/outputs/parameters, and the same Foldseek command including `--gpu 1`. The only functional change was replacing the Python summary-generation block with an `awk`/`sort` implementation so the UDT has no Python dependency.

Submitted the v1.0.5 no-Python UDT with the same inputs and parameters: combined VIR FASTA HID 72, ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, `--gpu 1`, and `threads=32`.

The new Step 5 outputs are running:
- HID 110 / HDA `f9cad7b01a472135bd12854f184975be`: Foldseek cluster assignments.
- HID 111 / HDA `f9cad7b01a4721351320290c226d145b`: representative sequences.
- HID 112 / HDA `f9cad7b01a4721352d3058ab4ab56d8a`: clustered sequences FASTA.
- HID 113 / HDA `f9cad7b01a472135c088553e5a7f9292`: cluster summary.
- HID 114 / HDA `f9cad7b01a472135ae86903ab0c6b387`: Foldseek clustering log.

Galaxy job ID: `bbd44e69cb8906b50601d9f560adc4ac`; external job ID: `77928507`; state at last poll: `running`. Verification remains pending until the job reaches a terminal state and outputs can be checked against the local Foldseek baseline.

## Step 5 Corrected FASTA Input Run and Verification Failure

To reproduce the local Foldseek baseline, the exact local input FASTA `data/genomes/alignments/all_vir_combined.fasta` was uploaded to Galaxy. This file contains 2,592 proteins and differs from the earlier Galaxy input `combined_vir.fasta`, which contains 2,664 proteins. The uploaded baseline FASTA is HID 115 / HDA `f9cad7b01a472135121bb81b3621cd18`, state `ok`, datatype `fasta`, size 1,057,429 bytes.

The same v1.0.5 UDT, UUID `43fa451a-3592-4cfa-80ea-c9f7d1afb772`, was rerun with HID 115, the same ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, `--gpu 1`, and `threads=32`. The run completed successfully in Galaxy: job `bbd44e69cb8906b53198741f0d9292ff`, external job ID `77928726`, exit code 0.

Outputs:
- HID 116 / HDA `f9cad7b01a4721358c891f834c425073`: Foldseek cluster assignments, `ok`, 76,140 bytes.
- HID 117 / HDA `f9cad7b01a472135bc7a04e7e3de73f5`: representative sequences, `ok`, 19,153 bytes.
- HID 118 / HDA `f9cad7b01a472135365d70ee6bbc97ac`: clustered sequences FASTA, `ok`, 1,058,751 bytes.
- HID 119 / HDA `f9cad7b01a4721359c7e822c01777993`: cluster summary, `ok`, 2,632 bytes.
- HID 120 / HDA `f9cad7b01a4721355cd8df4209988cb3`: Foldseek clustering log, `ok`, 34,226 bytes.

Verification against the local baseline failed. The Galaxy run clustered the same 2,592-member set as the local run, but the cluster structure differed: Galaxy produced 76 raw clusters, the largest with 812 members, whereas the local baseline has 73 clusters and FS_001 has 1,197 members. The Galaxy log confirms the command used `--gpu 1` and Foldseek reported `Use GPU 1`.

Diagnosis: the input mismatch was fixed, but the Galaxy command still differs from the local baseline in two ways: the local Foldseek run used `--threads 8` and did not pass `--gpu 1`; the Galaxy run used `threads=32` and explicit `--gpu 1`. The v1.0.5 summary generator also does not yet use `id_map.txt`, so its per-genome columns are not comparable for CAI/CAG protein IDs, although this does not explain the raw cluster-count mismatch.

Step 5 remains unverified against the local 73-cluster baseline.

## Step 5 Threads=8 GPU Reproducibility Test

To test whether the Galaxy/local Foldseek mismatch was caused by thread count, the same v1.0.5 UDT, UUID `43fa451a-3592-4cfa-80ea-c9f7d1afb772`, was rerun with the corrected baseline FASTA HID 115, the same ProstT5 model HID 74, coverage `0.8`, E-value `0.001`, alignment type `2`, and `threads=8`. The UDT still included explicit `--gpu 1`.

The run completed successfully in Galaxy: job `bbd44e69cb8906b501455402d43e68a0`, external job ID `77928842`, exit code 0.

Outputs:
- HID 121 / HDA `f9cad7b01a4721359be2a6698871f1e4`: Foldseek cluster assignments, `ok`, 76,140 bytes.
- HID 122 / HDA `f9cad7b01a472135a2fc9d28ee58e779`: representative sequences, `ok`, 19,153 bytes.
- HID 123 / HDA `f9cad7b01a472135f13d2a9be1bf1ad2`: clustered sequences FASTA, `ok`, 1,058,751 bytes.
- HID 124 / HDA `f9cad7b01a472135d4915cf50d5f7e3f`: cluster summary, `ok`, 2,632 bytes.
- HID 125 / HDA `f9cad7b01a4721350680194af3a8c8e8`: Foldseek clustering log, `ok`, 34,326 bytes.

Verification against the local baseline failed in the same way as the `threads=32` GPU run. The Galaxy run clustered the same 2,592-member set as the local run, but produced 76 raw clusters with largest cluster size 812. The local baseline has 73 clusters with FS_001 size 1,197. The size distribution also differed: Galaxy top sizes were `[812, 721, 350, 235, 93, 66, 58, 33, 31, 28]`; local top sizes were `[1197, 385, 248, 143, 136, 96, 85, 74, 53, 36]`.

The Galaxy log confirms `Threads: 8`, command-line `--gpu 1 --threads 8`, Foldseek version `10.941cd33`, and `Use GPU 1`. Therefore, thread count is not the source of the mismatch. The remaining substantive difference from the local baseline is explicit GPU use: the local baseline was produced by a CPU Foldseek run without `--gpu 1`.

Step 5 remains unverified against the local 73-cluster baseline. Exact reproduction likely requires a CPU/no-`--gpu 1` UDT run, or else accepting that GPU Foldseek/ProstT5 gives a different clustering result for this dataset.

## Step 5 Decision: Accept GPU Foldseek Result for Galaxy Branch

Decision: proceed with option 2 from the Step 5 reproducibility fork. The Galaxy workflow branch will accept the GPU-enabled Foldseek/ProstT5 result as a valid Galaxy/GPU execution mode rather than forcing exact reproduction of the earlier local CPU Foldseek baseline.

The accepted Galaxy Step 5 output is the corrected-input, GPU-enabled, `threads=8` v1.0.5 run:
- UDT UUID: `43fa451a-3592-4cfa-80ea-c9f7d1afb772`.
- Input FASTA: HID 115 / HDA `f9cad7b01a472135121bb81b3621cd18` (`all_vir_combined.fasta`, 2,592 proteins).
- Cluster assignments: HID 121 / HDA `f9cad7b01a4721359be2a6698871f1e4`.
- Representative sequences: HID 122 / HDA `f9cad7b01a472135a2fc9d28ee58e779`.
- Clustered sequences FASTA: HID 123 / HDA `f9cad7b01a472135f13d2a9be1bf1ad2`.
- Cluster summary: HID 124 / HDA `f9cad7b01a472135d4915cf50d5f7e3f`.
- Foldseek log: HID 125 / HDA `f9cad7b01a4721350680194af3a8c8e8`.

This run is technically successful and uses the intended Galaxy GPU path (`--gpu 1`, `Use GPU 1` in the log), but it is not numerically identical to the local CPU baseline. It produced 76 clusters from the same 2,592-member input set; the largest GPU cluster has 812 members. Downstream Galaxy Step 6 should therefore be treated as a GPU-branch analysis. The old local verification target of 338 FS_001 downsampled representatives is not expected to hold unless Step 6 is explicitly redirected back to the local CPU FS_001 definition.

## Step 6 GPU Branch Progress and FoldMason Blocker

Step 6 was started on the accepted Galaxy GPU Foldseek branch.

1. **GPU FS_001 extraction.** Registered and ran UDT `anton-1-foldseek_cluster_extract` v1.0.0, UUID `692cd4bc-5e6e-45d5-b6c4-684ea0907ab5`, using the accepted GPU Foldseek cluster TSV HID 121 and source FASTA HID 115. Outputs reached `ok`:
   - HID 126 / HDA `f9cad7b01a4721355cb29a979d0ac39e`: extracted GPU FS_001 FASTA.
   - HID 127 / HDA `f9cad7b01a4721352d7ae25931cb8384`: extraction report.
   Verification: downloaded the report and FASTA; report showed rank 1 representative `CAI7718682.1`, 812 members, 812 written sequences, and 0 missing sequences. FASTA header count was 812.

2. **MMseqs2 downsampling.** Ran ToolShed `MMseqs2 easy-linclust` (`toolshed.g2.bx.psu.edu/repos/iuc/mmseqs2_easy_linclust_clustering/mmseqs2_easy_linclust_clustering/17-b804f+galaxy1`) on HID 126 with `--min-seq-id 0.5`, `-c 0.8`, `--cov-mode 0`, amino-acid input, and representative/cluster-TSV outputs selected. Outputs reached `ok`:
   - HID 128 / HDA `f9cad7b01a47213538b287a9bc2eed86`: representative FASTA.
   - HID 129 / HDA `f9cad7b01a4721352dbeecad35f5769f`: adjacency list.
   Verification: downloaded the outputs; representative FASTA contained 336 sequences. The adjacency list contained 812 rows, 336 unique representatives, and 812 unique members. Thus GPU FS_001 downsampling reduced 812 proteins to 336 representatives under the approved Step 6 thresholds.

3. **FoldMason UDT attempts.** Three Galaxy FoldMason UDT variants were registered and run on the 336-representative FASTA HID 128 with ProstT5 model HID 74, `threads=8`, `--gpu 1`, and `--report-mode 0`:
   - v1.0.0, UUID `552d9e73-d9a6-464e-9629-5fff7a1289fb`, container `quay.io/biocontainers/foldmason:4.dd3c235`, outputs HIDs 130-133, failed.
   - v1.0.1, UUID `99cb1345-747f-4d57-8463-2d1fb3ec3058`, same container but downloading the upstream FoldMason AVX2 binary at runtime, outputs HIDs 134-137, failed.
   - v1.0.2, UUID `45fcd231-9cfe-496e-8766-b78660653dd9`, container `quay.io/biocontainers/foldseek:10.941cd33` plus upstream FoldMason AVX2 binary, outputs HIDs 138-141, failed.

All FoldMason attempts failed with the same core error: `Foldseek was compiled without ProstT5 support` followed by `Error: Structure createdb died`. The final v1.0.2 log confirmed that the container Foldseek on `PATH` was version `10.941cd33`, but the upstream FoldMason binary still reported the no-ProstT5-support error internally. A local probe using the current Conda `foldmason` 4.dd3c235 on the same 336-representative FASTA failed with the same error, indicating that the currently available FoldMason builds do not support FASTA+ProstT5 in this environment even though historical local FoldMason outputs exist from an earlier state.

Step 6 status: GPU FS_001 extraction and MMseqs2 downsampling are verified. FoldMason AA/3Di alignment remains blocked by unavailable FoldMason builds with FASTA+ProstT5 support. Step 6 remains pending and should not be marked complete until a FoldMason build compiled with ProstT5 support is available in Galaxy or the step is intentionally re-scoped to a different structural-MSA method.

## Step 6 CPU FoldMason Routing Test

After noting that FoldMason itself should not require GPU routing, a clean CPU UDT was registered and run with the `anton-32-` prefix.

Registered UDT `anton-32-foldmason_align` v1.0.0, UUID `eaf3ae69-891e-4377-84a1-78706ba1cf39`, using container `quay.io/biocontainers/foldmason:4.dd3c235`. The tool omitted `--gpu`, used `threads=32`, and ran `foldmason easy-msa` on the GPU-branch FS_001 representative FASTA HID 128 with ProstT5 model HID 74 and `--report-mode 0`.

The run produced HIDs 142-145 and failed:
- HID 142 / HDA `f9cad7b01a472135e9a4fbb4a5f7db60`: FoldMason AA alignment, `error`.
- HID 143 / HDA `f9cad7b01a4721355988ce66d9f1ef6d`: FoldMason 3Di alignment, `error`.
- HID 144 / HDA `f9cad7b01a4721350dfe5a1e0ab49395`: FoldMason guide tree, `error`.
- HID 145 / HDA `f9cad7b01a472135c5254ff7049392d2`: FoldMason alignment log, `error`.

Galaxy job ID: `bbd44e69cb8906b5a25e0a9a936315f9`; external job ID: `77929985`; exit code 1. The log confirms CPU routing (`GPU flag: omitted`, `Use GPU 0`, `Threads 32`) but fails with the same blocker: `Foldseek was compiled without ProstT5 support` and `Error: Structure createdb died`.

Conclusion: renaming/routing the tool as `anton-32-` and omitting GPU is correct for CPU scheduling, but it does not solve this Step 6 blocker. The missing requirement is a FoldMason build compiled with FASTA/ProstT5 support, not GPU access.

## Step 6 FoldMason Success with ProstT5-Enabled Container

A public ProstT5-enabled FoldMason container became available at `quay.io/nekrut/foldmason-prostt5:4.dd3c235-cpu`. The Quay tag list was checked directly and contained tag `4.dd3c235-cpu`.

Initial registration of `anton-32-foldmason_align` v1.0.1, UUID `66f36445-cd3d-4ad5-88b1-6546b1f134f1`, used this container but called `foldmason` directly. That run failed with exit code 127 because the upstream-style container does not put a `foldmason` executable on `PATH`; it exposes `/usr/local/bin/entrypoint` and architecture-specific binaries instead. A second attempt, v1.0.2 UUID `37f9f1d1-f1b2-4cb0-8e18-149eb19bba95`, attempted dynamic executable resolution but failed during Galaxy command-line construction because shell command substitutions conflicted with UDT templating.

The successful UDT was `anton-32-foldmason_align` v1.0.3, UUID `b9cc1615-2ced-4868-8506-661afbf2d876`, using container `quay.io/nekrut/foldmason-prostt5:4.dd3c235-cpu` and directly invoking `/usr/local/bin/entrypoint`. It ran on the GPU-branch FS_001 MMseqs2 representative FASTA HID 128 with ProstT5 model HID 74, `threads=32`, no `--gpu` flag, and `--report-mode 0`.

Galaxy job `bbd44e69cb8906b545cbd36e7584ce18`, external job ID `77930648`, completed with exit code 0. Outputs:
- HID 154 / HDA `f9cad7b01a4721358b2371a2db175c36`: FoldMason AA alignment, `ok`, 3,408,768 bytes.
- HID 155 / HDA `f9cad7b01a472135cb0c0c82b14d8623`: FoldMason 3Di alignment, `ok`, 3,408,768 bytes.
- HID 156 / HDA `f9cad7b01a472135e5762168bf992eca`: FoldMason guide tree, `ok`, 5,758 bytes.
- HID 157 / HDA `f9cad7b01a472135e6ec895e4f7b6ce6`: FoldMason alignment log, `ok`, 5,441 bytes.

Verification: downloaded all four outputs to `galaxy_step6/foldmason_success/`. The AA alignment contains 336 sequences; the 3Di alignment contains 336 sequences; both alignments have uniform 10,128-column length and identical sequence ID order. The guide tree is non-empty (5,758 characters). The log contains FoldMason version information, lacks the previous `compiled without ProstT5 support` error, and ends with successful writing of `FS001_gpu_branch_cpu_aa.fa`, `FS001_gpu_branch_cpu_3di.fa`, and `FS001_gpu_branch_cpu.nw`.

Step 6 is complete for the accepted Galaxy GPU Foldseek branch.

## Step 7 Microsynteny Orthology on Accepted Galaxy GPU Branch

Step 7 was executed on the accepted Galaxy GPU Foldseek branch, where GPU FS_001 contains 812 total proteins rather than the local CPU branch's 1,197. Because FS_001 membership differs, the local CPU-branch verification target of 11 high-confidence and 26 medium-confidence pairs is not expected to hold. Verification for this branch is based on internally consistent Galaxy outputs.

1. **Input preparation.** Uploaded the small VIR ID lists needed to define non-VIR proteomes:
   - PvW1 VIR IDs: HID 158 / HDA `f9cad7b01a4721355894f9087ace169b`, `ok`.
   - PvPAM VIR IDs: HID 159 / HDA `f9cad7b01a47213589c50b3be7d3bbe8`, `ok`.

   Registered and ran `anton-1-step7_prepare_fastas` v1.0.0, UUID `3dd90d4a-0978-476d-9a82-1afa8232f23e`, using container `quay.io/biocontainers/python:3.12.12`. The UDT split accepted GPU FS_001 (HID 126) into PvW1/PvPAM subsets and removed HMM-defined VIR IDs from the PvW1/PvPAM proteomes to construct the housekeeping inputs. Outputs reached `ok`:
   - HID 160 / HDA `f9cad7b01a47213521bf52c6c42893ec`: GPU FS_001 PvW1 FASTA, 234 sequences.
   - HID 161 / HDA `f9cad7b01a47213506b9446068bab082`: GPU FS_001 PvPAM FASTA, 306 sequences.
   - HID 162 / HDA `f9cad7b01a472135792bbbaa1b3bfe2f`: PvW1 non-VIR FASTA, 5,327 sequences.
   - HID 163 / HDA `f9cad7b01a4721350bc4098789a13422`: PvPAM non-VIR FASTA, 5,477 sequences.
   - HID 164 / HDA `f9cad7b01a472135c91c3f1f8d24987c`: preparation report.

2. **RBH generation.** Registered `anton-8-mmseqs_easy_rbh_pair` v1.0.0, UUID `a7c3813c-a12e-4e5d-b1dd-54cb55a13b0b`, but it failed during Galaxy command-line construction because shell command substitutions conflicted with UDT templating. Registered corrected v1.0.1, UUID `eedd5f22-5a80-40aa-a343-dd52ffd8f7ee`, using container `quay.io/biocontainers/mmseqs2:18.8cc5c--hd6d6fdc_0`. It ran `mmseqs easy-rbh` with the Step 7 thresholds: FS_001 `--min-seq-id 0.3 -c 0.5 -e 1e-5`; housekeeping `--min-seq-id 0.5 -c 0.8 -e 1e-10`; `threads=8`. Outputs reached `ok`:
   - HID 169 / HDA `f9cad7b01a4721357356944f393c5542`: GPU FS_001 PvW1-PvPAM RBH.
   - HID 170 / HDA `f9cad7b01a472135550202219b3d8adc`: PvW1-PvPAM housekeeping RBH.
   - HID 171 / HDA `f9cad7b01a4721357bb7cd9d569733ef`: RBH generation report.
   - HID 172 / HDA `f9cad7b01a472135903454df0a007ede`: MMseqs RBH log.

   Verification: downloaded the outputs. The RBH report showed 141 GPU FS_001 RBH pairs and 5,120 housekeeping RBH pairs. FS_001 RBH median identity was 76.4%; housekeeping median identity was 99.8%.

3. **Microsynteny scoring.** Registered and ran `anton-1-microsynteny_filter` v1.0.0, UUID `03f19bcd-e724-49fe-9bfa-ebcff6dada4c`, using container `quay.io/biocontainers/python:3.12.12`. The UDT parsed PvW1/PvPAM protein FASTA location headers, collected ±2 flanking neighbors for each GPU FS_001 RBH pair, scored each pair by the number of flanking neighbors supported by the housekeeping RBH backbone, and classified confidence as high = synteny score >=3 and identity >=50%, medium = synteny score >=2, low = otherwise. Outputs reached `ok`:
   - HID 173 / HDA `f9cad7b01a4721352bec834307906580`: flanking-neighbor table.
   - HID 174 / HDA `f9cad7b01a4721356c4f29144aa7d6d9`: microsynteny scores.
   - HID 175 / HDA `f9cad7b01a4721354cacbaeb005189e1`: ortholog candidates with confidence.
   - HID 176 / HDA `f9cad7b01a472135885c13332b30d8e7`: high-confidence ortholog candidates.
   - HID 177 / HDA `f9cad7b01a47213511bcef880e60f054`: microsynteny report.

   Verification: downloaded the outputs. The combined table contains 141 RBH pairs. Confidence counts are 3 high, 10 medium, and 128 low. Synteny-score distribution is: score 0 = 118 pairs, score 1 = 10, score 2 = 10, score 3 = 2, score 4 = 1. The 3 high-confidence pairs are `CAG9484573.1` ↔ `CAI7717645.1`, `CAG9481896.1` ↔ `CAI7719339.1`, and `CAG9478286.1` ↔ `CAI7721621.1`.

Step 7 is complete for the accepted Galaxy GPU Foldseek branch.

## Step 8 Spatial Analysis on Accepted Galaxy GPU Branch

Step 8 was executed on the accepted Galaxy GPU Foldseek branch. The final accepted run is `anton-1-spatial_analysis` v1.0.2, which uses the verified PIR/VIR ID lists as the authoritative functional set and assigns accepted GPU Foldseek cluster labels where available. This is important because an initial v1.0.0 run that parsed Galaxy HMMER per-sequence outputs directly recovered only 859 / 696 / 921 VIR IDs, not the verified 931 / 748 / 985 baseline. A v1.0.1 rerun used the verified ID lists but selected canonical/all-protein top chromosomes, giving a PvP01 main-chromosome count of 303 rather than the local baseline 347. The final v1.0.2 rerun uses the local pipeline's actual rule: select the top 14 VIR-bearing contigs per genome by maximum VIR coordinate.

Inputs and tool versions:
- UDT: `anton-1-spatial_analysis` v1.0.2, UUID `ce70ad63-937c-426c-b365-e936fb0662de`.
- Container: `quay.io/biocontainers/python:3.12.12`.
- Protein FASTAs: PvP01 HDA `f9cad7b01a472135d4ce8c45d3e88593`; PvW1 HDA `f9cad7b01a4721354f85b30a8c24a3ef`; PvPAM HDA `f9cad7b01a4721353480e1cd16d92a22`.
- Verified VIR ID lists: PvP01 HID 185 / HDA `f9cad7b01a472135d51977660316a93b`; PvW1 HID 158 / HDA `f9cad7b01a4721355894f9087ace169b`; PvPAM HID 159 / HDA `f9cad7b01a47213589c50b3be7d3bbe8`.
- GPU Foldseek cluster assignments: HID 121 / HDA `f9cad7b01a4721359be2a6698871f1e4`.
- Parameters: subtelomeric boundary `0.10`; label-shuffle permutations `500`; minimum cluster members for tandem test `10`; random seed `42`; main-contig rule `top14_vir_bearing_by_max_vir_end`.

Final outputs reached `ok`:
- HID 193 / HDA `f9cad7b01a472135ae393c86aba49be9`: VIR coordinate table.
- HID 194 / HDA `f9cad7b01a47213506f26eaf8e564f73`: VIR main-chromosome coordinate table.
- HID 195 / HDA `f9cad7b01a4721356650bee21c8d4003`: per-cluster spatial features.
- HID 196 / HDA `f9cad7b01a472135741d4d6c6b62c418`: universal cluster main-chromosome counts.
- HID 197 / HDA `f9cad7b01a4721357e8d49e3e533be6f`: tandem label-shuffle tests.
- HID 198 / HDA `f9cad7b01a472135cbe2b1261e7ff0ba`: spatial analysis report.
- HID 199 / HDA `f9cad7b01a472135ad619bd18ec63274`: VIR IDs missing coordinates.

Verification: downloaded the final outputs to `galaxy_step8/final/` and parsed them locally. The coordinate table contains all 2,664 verified functional VIR/PIR IDs: PvP01 = 931, PvW1 = 748, PvPAM = 985; missing-coordinate count = 0. The main-contig subset matches the local spatial baseline counts: PvP01 = 347, PvW1 = 634, PvPAM = 735, total = 1,716. Outer-10% subtelomeric enrichment is 64.45% overall (1,106 / 1,716), with per-genome fractions PvP01 = 80.4%, PvW1 = 64.2%, PvPAM = 57.1%, reproducing the local conclusion that main-contig VIRs are strongly subtelomeric. GPU-branch spatial cluster features include 15 strict-universal main-contig clusters and 51 clusters with at least one main-contig member; these differ from the local CPU branch because the accepted GPU Foldseek clustering has different cluster membership. Tandem label-shuffle testing produced 22 cluster/genome tests and 3 tests with p < 0.05 (`FS_004` in PvP01, `FS_006` in PvW1, `FS_001` in PvPAM), consistent with the local expectation that only a small minority of cluster/genome tests show significant same-cluster tandem co-localization.

Step 8 is complete for the accepted Galaxy GPU Foldseek branch.

## Step 9 IQ-TREE Phylogeny on Accepted Galaxy GPU Branch — In Progress

Step 9 was started on the accepted Galaxy GPU Foldseek/FoldMason branch. Local Step 9 used `trimal -gt 0.65` on AA and 3Di alignments, concatenated the trimmed alignments, and ran IQ-TREE with a partitioned AA + 3Di model. Applying the same `0.65` occupancy threshold to the accepted Galaxy FoldMason alignment produced an empty alignment: the GPU-branch FoldMason AA and 3Di alignments each contain 336 sequences and 10,128 columns, but maximum per-column occupancy is only 25%, so no columns satisfy `>=0.65` occupancy. This is a branch-specific alignment sparsity difference, not an IQ-TREE failure.

Preprocessing attempts:
- Uploaded local 3Di model matrix `3DI.nexus` to Galaxy: HID 200 / HDA `f9cad7b01a472135473dab0becd50bbf`, state `ok`.
- Registered `anton-1-iqtree_structural_prep` v1.0.0, UUID `f36d0724-4945-4820-a5ef-fdaf77c29a16`, container `quay.io/biocontainers/python:3.12.12`.
- First prep run with local threshold `0.65` produced outputs HIDs 201-205, all `ok`, but verification showed 336 sequences and 0 AA / 0 3Di retained columns. These outputs are not biologically usable for IQ-TREE.
- Second prep run with threshold `0.20` produced outputs HIDs 206-210, all `ok`. Verification showed 336 sequences, 138 AA retained columns, 138 3Di retained columns, and 276 concatenated columns. Partition file HID 209 defines `part1 = 1-138` and `part2 = 139-276`, with `VT+F+R6` for AA and `3DI+G` for 3Di. This threshold is an explicit Galaxy-branch adaptation, not an exact local-threshold reproduction.

IQ-TREE run submitted:
- Tool: `toolshed.g2.bx.psu.edu/repos/iuc/iqtree/iqtree/2.4.0+galaxy2`.
- Galaxy job: `bbd44e69cb8906b5c270b4072cec5457`, external ID `10025375`.
- Inputs: combined alignment HID 208 / HDA `f9cad7b01a472135452a5bcd7d55e5b8`; partition file HID 209 / HDA `f9cad7b01a472135e6f33ebb59e7292a`; 3Di model matrix HID 200 / HDA `f9cad7b01a472135473dab0becd50bbf`.
- Parameters: sequence type `AA`; seed `42`; `--safe`; partition model `-p`; custom model definition `--mdef 3DI.nexus`; ultrafast bootstrap `-B 1000`; `--bnni`; SH-aLRT `1000`; bootstrap trees requested.
- Expected outputs: HIDs 211-216 (BIONJ tree, ML tree, ML distance matrix, bootstrap splits, IQ-TREE report, UFBoot trees).

Current verification status: after 80 one-minute polls, HIDs 211-216 remained `running` with job `bbd44e69cb8906b5c270b4072cec5457` still in Galaxy `running` state. Step 9 is therefore **not complete**. Completion requires polling the job to terminal state, downloading the ML tree and IQ-TREE report, verifying that the tree is parseable and contains the expected 336 taxa, and then computing/parsing the genome-label parsimony score for the accepted Galaxy branch. The local parsimony baseline of 160 is not expected to match exactly because the accepted Galaxy branch uses different Foldseek membership, FoldMason alignment, and a lower occupancy threshold forced by alignment sparsity.

### Step 9 verification update — IQ-TREE run completed but reduced-taxon

The submitted Galaxy IQ-TREE job `bbd44e69cb8906b5c270b4072cec5457` completed successfully in Galaxy with exit code 0. Outputs HIDs 211-216 are all `ok` and were downloaded to `galaxy_step9/iqtree/`:
- HID 211 / HDA `f9cad7b01a47213513d403e38c531199`: BIONJ tree.
- HID 212 / HDA `f9cad7b01a472135009f2d2ad412d897`: maximum-likelihood tree.
- HID 213 / HDA `f9cad7b01a472135c18941cb712df663`: maximum-likelihood distance matrix.
- HID 214 / HDA `f9cad7b01a47213563dc88f4396269e9`: bootstrap splits.
- HID 215 / HDA `f9cad7b01a4721359aaac71f468e0823`: IQ-TREE report and final tree.
- HID 216 / HDA `f9cad7b01a472135899f35c4ea125e46`: UFBoot trees.

Verification did **not** pass the original Step 9 criterion. The threshold-0.20 concatenated input FASTA contains 336 named records of length 276, but 160 records are all gaps in the retained columns. IQ-TREE consequently analyzed a reduced dataset: the report states `Input data: 176 taxa with 2 partitions and 276 total sites`, and the ML tree contains 176 tips. Tree genome labels among these 176 tips are PvPAM = 64, PvP01 = 61, PvW1 = 51. A diagnostic Fitch genome-label parsimony score on the reduced tree is 86, but this is **not comparable** to the local 338-taxon baseline score of 160 because 160 Galaxy-branch taxa are absent from the tree.

Threshold sensitivity on the accepted Galaxy FoldMason alignments shows the tradeoff:

| Occupancy threshold | AA columns | 3Di columns | Concatenated columns | Sequences with ≥1 non-gap retained character | All-gap sequences |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0.25 | 3 | 3 | 6 | 95 | 241 |
| 0.20 | 138 | 138 | 276 | 176 | 160 |
| 0.15 | 250 | 250 | 500 | 192 | 144 |
| 0.10 | 511 | 511 | 1,022 | 270 | 66 |
| 0.08 | 995 | 995 | 1,990 | 308 | 28 |
| 0.05 | 1,947 | 1,947 | 3,894 | 326 | 10 |
| 0.03 | 3,493 | 3,493 | 6,986 | 336 | 0 |
| 0.02 | 5,608 | 5,608 | 11,216 | 336 | 0 |
| 0.01 | 7,710 | 7,710 | 15,420 | 336 | 0 |

Current interpretation: the completed threshold-0.20 tree is a valid reduced-taxon diagnostic for the accepted Galaxy branch, but it is not a verified completion of Plan F Step 9. A full 336-taxon Galaxy-branch IQ-TREE run would require using a lower occupancy threshold, with `0.03` being the least stringent threshold in this scan that retains at least one non-gap character for every sequence. This would be a more divergent, much larger, sparse alignment (6,986 concatenated columns) and should be treated as an explicit Galaxy-branch rerun rather than exact local reproduction.

## Galaxy UDT authoring update — new-style Foldseek CPU/GPU test tools

Registered two new Foldseek/ProstT5 clustering UDTs using the updated `GalaxyUserTool` authoring style from the `udt-authoring` skill: `shell_command`, `$(inputs.name.path)` data references, fixed `from_work_dir` outputs, object-form `help`, and explicit resource requirement blocks. Local validation against the Galaxy Python model was attempted but blocked by missing `pydantic` in the project environment; Galaxy server-side creation validation accepted both definitions.

Registered tools:
- GPU version: `anton-gpu-xl-foldseek_prostt5_clustering` v2.0.0, UUID `ba86192a-d143-4b14-ae97-4ff9188dd083`, container `quay.io/biocontainers/foldseek:10.941cd33`.
  - Resource requirement block: `cores_min=32`, `ram_min=8192`, `cuda_device_count_min=1`, `cuda_device_count_max=1`, `gpu_memory_min=1`.
  - Foldseek command includes `--gpu 1` and `--threads` from the `threads` input.
- CPU version: `anton-32-foldseek_prostt5_clustering` v1.0.0, UUID `46dd01b5-6c9d-4c92-a404-4abbb16c3d71`, container `quay.io/biocontainers/foldseek:10.941cd33`.
  - Resource requirement block: `cores_min=32`, `ram_min=8192`, `cuda_device_count_max=0`.
  - Foldseek command includes `--gpu 0` and `--threads` from the `threads` input.

Both tools produce the standard Foldseek outputs plus an explicit environment report output (`foldseek_env_report.txt`) recording the UDT variant, Foldseek GPU flag, requested threads, `$GALAXY_SLOTS`, CUDA/NVIDIA visibility variables, Foldseek version, and `nvidia-smi` output if available. This is intended to test whether Galaxy honors the CPU/GPU routing and resource declarations at runtime.

Local definition files:
- `udt_defs/foldseek_gpu_newschema.json`
- `udt_defs/foldseek_cpu_newschema.json`
- `udt_defs/foldseek_gpu_newschema_create_response.json`
- `udt_defs/foldseek_cpu_newschema_create_response.json`

### Foldseek CPU/GPU UDT routing test jobs submitted

Submitted both new-style Foldseek/ProstT5 UDTs on the existing Step 5 inputs: combined VIR FASTA HID 115 / HDA `f9cad7b01a472135121bb81b3621cd18` and ProstT5 model HID 74 / HDA `f9cad7b01a472135dfae40ce8ed6d561`. Parameters: coverage `0.8`, E-value `0.001`, alignment type `2`, threads `32`.

- GPU UDT `anton-gpu-xl-foldseek_prostt5_clustering` v2.0.0, UUID `ba86192a-d143-4b14-ae97-4ff9188dd083`:
  - Galaxy job ID: `bbd44e69cb8906b5491b57586d37351c`.
  - Output HIDs 217-222: cluster assignments, representative FASTA, all-sequences FASTA, cluster summary, Foldseek log, environment report.
- CPU UDT `anton-32-foldseek_prostt5_clustering` v1.0.0, UUID `46dd01b5-6c9d-4c92-a404-4abbb16c3d71`:
  - Galaxy job ID: `bbd44e69cb8906b5e03132fc66b9d6cb`.
  - Output HIDs 223-228: cluster assignments, representative FASTA, all-sequences FASTA, cluster summary, Foldseek log, environment report.

Current status: submitted/new. Verification still pending; the intended checks are terminal job state, `foldseek_env_report.txt` for GPU/CPU visibility and `$GALAXY_SLOTS`, Foldseek logs for `--gpu 1` versus `--gpu 0`, and output cluster counts.

### Foldseek CPU/GPU UDT routing test verification

The two new-style Foldseek UDT routing-test jobs completed successfully, so no duplicate rerun was submitted.

- GPU UDT job `bbd44e69cb8906b5491b57586d37351c` completed `ok`, exit code 0, external job ID `78066691`.
  - Outputs HIDs 217-222 all `ok`.
  - Environment report HID 222 shows `UDT variant: gpu-xl-new-schema`, `Foldseek command GPU flag: --gpu 1`, `GALAXY_SLOTS: 32`, Foldseek version `10.941cd33`, and successful `nvidia-smi` output exposing an `NVIDIA A100-SXM4-40GB` GPU with CUDA 12.7.
  - Foldseek log HID 221 records `--gpu 1`, `Use GPU 1`, and `CUDA0`.
  - Cluster output verification: 2,592 input members assigned, 76 clusters. Top clusters: FS_001 = 812, FS_002 = 721, FS_003 = 350.
- CPU UDT job `bbd44e69cb8906b5e03132fc66b9d6cb` completed `ok`, exit code 0, external job ID `78066692`.
  - Outputs HIDs 223-228 all `ok`.
  - Environment report HID 228 shows `UDT variant: cpu-32-new-schema`, `Foldseek command GPU flag: --gpu 0`, `GALAXY_SLOTS: 32`, Foldseek version `10.941cd33`, and `nvidia-smi: command not found`.
  - Foldseek log HID 227 records `--gpu 0` and `Use GPU 0`.
  - Cluster output verification: 2,592 input members assigned, 76 clusters. Top clusters: FS_001 = 766, FS_002 = 405, FS_003 = 215.

Interpretation: Galaxy honored the new-style resource/routing distinction for these UDTs. The GPU version ran on a node/container environment with visible NVIDIA A100 hardware and Foldseek used GPU mode; the CPU version ran without `nvidia-smi` available and Foldseek used CPU mode. Both jobs received `GALAXY_SLOTS=32`.
