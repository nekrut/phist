# phist — Structure-Aware Phylogenomics of the *Plasmodium vivax* PIR/VIR Multigene Family

This repository is the archived working state of the `phist2` analysis
(`~/.loom/analyses/phist2`), covering **2026-05-27 through 2026-07-31**. It contains two parallel
implementations of the same study: a **completed local pipeline** and an **in-progress Galaxy
replication** (Plan F). Work is expected to continue from here.

---

## 1. The scientific question

The PIR (*Plasmodium* interspersed repeat) superfamily — called *vir* in *P. vivax* — is the largest
multigene family in the genome and encodes variant surface antigens involved in antigenic variation,
cytoadherence, and rosetting. PIRs are extremely sequence-divergent yet, per Harrison & Higgins (2020,
PDB 6ZYV), share a single conserved mostly-α-helical fold. Sequence-based clustering therefore
over-splits the family.

We apply the FoldMason structural phylogenomics pipeline (Gilchrist, Mirdita & Steinegger, 2026,
*Science*) to *vir* across three long-read reference assemblies from geographically distant isolates:

| Assembly | Origin | Reference |
| :--- | :--- | :--- |
| **PvP01** | Papua, Indonesia | Auburn et al., 2016 |
| **PvW1** | Thailand | Minassian et al., 2021 |
| **PvPAM** | Peruvian Amazon | Vaughan et al., 2023 |

Two questions drive the analysis. First, does structure-aware clustering unify the family in a way
sequence clustering cannot? Second, does the *vir* repertoire carry geographic structure — did each
lineage expand its own repertoire after separation, or does the family predate that separation?

## 2. Headline findings (local branch, fully verified)

- **Structural clustering halves the family's apparent complexity.** Foldseek + ProstT5 collapses
  2,592 VIR proteins into **73 structural clusters**, against **146 MCL sequence clusters**. The
  dominant cluster **FS_001 holds 1,197 proteins (46%)** and alone absorbs 89 of the 146 MCL
  subfamilies.
- **The family is structurally universal across continents.** **97.3%** of VIR proteins fall in
  clusters containing members from all three genomes. Genome-unique clusters account for 52 proteins
  (2%), almost all singletons or pairs.
- **No geographic signal within FS_001.** Genome-of-origin parsimony on 338 sub-representatives gives
  observed scores of 162 (AA), 156 (3Di), 160 (partitioned) against a shuffled median of 160 —
  *p* = 0.69, 0.26, 0.55. Sequences from Indonesia, Thailand, and Peru are interleaved
  indistinguishably from random. This supports ancient diversification predating lineage separation,
  plus ongoing recombination and gene conversion keeping the family panmictic.
- **Strong subtelomeric enrichment.** 64.5% of main-chromosome VIRs sit in the outer 10% of chromosome
  length (PvP01 80%, PvW1 64%, PvPAM 57%). Per-chromosome VIR counts correlate tightly across
  assemblies (Spearman ρ = 0.909–0.915).
- **Orthology is scarce and needs synteny.** Of 194 FS_001 RBH pairs between PvW1 and PvPAM, only
  **11 are high-confidence** after microsynteny filtering against a 5,120-pair housekeeping backbone;
  26 medium, 157 low.
- **A methodological caveat worth carrying forward:** the trimAl `-gt 0.65` threshold used by
  Gilchrist et al. removes *every* column when the input spans a whole superfamily. Use
  `-automated1` at family level; `-gt 0.65` works within a homologous cluster.

Every one of these numbers is machine-checked: `verification/verify_claims.py` validates **77 claims
against the raw outputs, 77 PASS / 0 FAIL** (see `verification/verification_report.md`).

## 3. Repository layout

```
notebook.md                 Primary lab notebook (1,273 lines) — the authoritative record
pipeline.md                 Reproducible command ledger: 8 modules, every parameter justified
paper_full.md / paper.pdf   Narrative manuscript of the local branch
pvivax_PIR_characterization.pdf   Longer characterization write-up
results.md                  De novo VIR subfamily distribution table
reviewer_prompt.txt         LLM-reviewer critique prompt used to stress-test the initial plan
verification/               verify_claims.py + the 77/77 verification report
figures/                    fig1 ideogram, fig2 FS_001 density, fig3 identity hist,
                            fig4 ribbon synteny, fig5 Q2 tree
data/                       Inputs and derived data (see §5 for what was excluded)
  genomes/                  Proteomes, GFFs, HMMER tables, MCL clusters, id_map
  genomes/alignments/       foldseek_work, fs_clusters, phylo_q1, phylo_q2, ortho, spatial
  pseudogenes/              Six-frame translations and PF05795 screens
  hmm/VIR.hmm               The extracted PF05795 profile
udt_defs/                   Galaxy user-defined tool (UDT) JSON definitions
galaxy_step2_check/ … galaxy_step9/   Galaxy run outputs, named hid<N>_* after Galaxy
                            history dataset IDs; failure logs deliberately retained
smbe-a/                     Unrelated SMBE demo sub-project (see §6)
sessions/                   Agent session transcripts (phist2, smbe-a)
activity.jsonl              Agent activity log for the phist2 session
docs/EXCLUDED_DATA.md       Everything dropped from the 9.4 GB working dir, and how to restore it
```

## 4. The two branches

### Local branch — complete

Eight modules, documented command-by-command in `pipeline.md`: HMMER functional PIR identification →
pseudogene six-frame rescue → MMseqs2/MCL sequence baseline → Foldseek+ProstT5 structural clustering →
FS_001 subsampling + FoldMason MSA → trimAl + IQ-TREE partitioned phylogeny → microsynteny orthology →
spatial distribution analysis. Tool versions: HMMER 3.4, Foldseek 10.941cd33, MMseqs2 18.8cc5c,
MCL 22.282, FoldMason 4.dd3c235, trimAl 1.5.rev1, IQ-TREE 3.1.2.

### Galaxy branch (Plan F) — 7 of 9 steps done

Progressive replication on **usegalaxy.org**, history `phist2`
(`bbd44e69cb8906b5c0a92f1d9b046fdd`), user `aun1`, mixing ToolShed tools with custom UDTs registered
through the Galaxy API.

| Step | What | State |
| ---: | :--- | :--- |
| 1 | Upload genomes, proteomes, GFFs, Pfam HMM, 3Di matrix | done — 9 datasets `ok` |
| 2 | ToolShed HMMER functional screens | done — 931 / 748 / 985, exact match to local |
| 3 | Pseudogene extractor/translator UDT | done with caveat — see §5 |
| 4 | Pseudogene HMMER screen | **OPEN** — see §5 |
| 5 | Foldseek+ProstT5 clustering UDT | done — GPU result accepted, diverges from local |
| 6 | FoldMason structural alignment UDT | done — after a long container fight |
| 7 | Microsynteny orthology UDTs | done — 3 high / 10 medium / 128 low |
| 8 | Spatial analysis UDT | done — reproduces local main-chromosome counts and 64.45% enrichment |
| 9 | ToolShed IQ-TREE phylogeny | **OPEN** — see §5 |

Two hard-won infrastructure results are worth preserving. FoldMason on Galaxy required a purpose-built
ProstT5-enabled container, `quay.io/nekrut/foldmason-prostt5:4.dd3c235-cpu`, after six consecutive
failures with stock containers (logs in `galaxy_step6/`). And a CPU/GPU UDT routing test confirmed
Galaxy honors new-style resource declarations: the GPU variant landed on an NVIDIA A100-SXM4-40GB with
CUDA 12.7 and ran `--gpu 1`, the CPU variant had no `nvidia-smi` and ran `--gpu 0`, both with
`GALAXY_SLOTS=32`.

## 5. Where to pick up — open threads

**Step 9 — IQ-TREE on the Galaxy branch is the main blocker.** The Galaxy FoldMason alignment is far
sparser than the local one: 336 sequences × 10,128 columns at only 25% maximum per-column occupancy.
At the local `-gt 0.65` threshold, zero columns survive. A threshold-0.20 run completed
(job `bbd44e69cb8906b5c270b4072cec5457`, outputs HIDs 211–216, downloaded to `galaxy_step9/iqtree/`)
but **160 of 336 sequences were all-gap in the retained columns**, so IQ-TREE analyzed only 176 taxa.
Its diagnostic parsimony score of 86 is *not* comparable to the local 338-taxon baseline of 160. The
notebook records a full occupancy-threshold scan; **0.03 is the least stringent threshold retaining at
least one non-gap character for every sequence**, at the cost of a 6,986-column sparse alignment. The
decision to make: rerun at 0.03 as an explicit Galaxy-branch analysis, or investigate why the Galaxy
FoldMason alignment is so much sparser than the local one.

**Step 4 — the PvPAM pseudogene baseline is stale, not wrong.** Galaxy reproduces PvP01 exactly
(75 loci) but yields 65 PvPAM loci against an expected 70. Diagnosis: all Galaxy inputs are
byte-identical to local, and re-running local HMMER 3.4 on the *current* PvPAM FASTA also gives 65.
The checked-in `data/pseudogenes/PvPAM_pseudo_PF05795.tbl` (70 loci) predates the current
translation/HMMER toolchain. Resolution is to regenerate the baseline and update the expected count —
which also means `verification/verify_claims.py` will need its PvPAM pseudogene claim revised.

**Step 3 — the translator UDT is nondeterministic.** `gff_pseudogene_translator` uses
`sorted(set(exons), key=lambda e: e[1])`, which does not break ties when transcript and exon records
share a start coordinate. Record IDs and counts match local output but sequences are not
byte-identical. A deterministic tie-break is needed before this UDT can be called an exact
reproduction.

**The GPU/CPU Foldseek divergence is unresolved and consequential.** Local CPU gives 73 clusters with
FS_001 = 1,197. Galaxy GPU gives 76 clusters with FS_001 = 812. The routing test's CPU variant gives
76 clusters with FS_001 = 766. All three differ. The user explicitly accepted the GPU result as *the*
Galaxy branch, which is why downstream Galaxy counts (Step 7's 3 high-confidence orthologs vs the
local 11) legitimately differ. Any comparison across branches must account for this.

## 6. `smbe-a/` — separate sub-project

An unrelated SMBE conference demo, not part of the PIR analysis. It sets up a Galaxy collection-
operations demo from Zenodo record 5119008. Uploads failed on **usegalaxy.org**
(`Error occurred while building config files for tool 'upload1'`, tus server 500) and succeeded on
**usegalaxy.eu** instead (history `smbe-demo`, `11ac94870d0bb33a0987eaf8ad836c69`). A haploid
variant-calling workflow was invoked on history `smbe26` (`11ac94870d0bb33a0a38ca6171654a84`),
invocation `886a87e4e0bb6974`, and **its status was never polled to completion** — 0 of 16 steps
recorded as of last poll. The FASTQ files are excluded from this repo; refetch from Zenodo.

## 7. Reproducing

```bash
python3 verification/verify_claims.py      # expect 77/77 PASS
```

`pipeline.md` carries the full command ledger with a justification for every parameter. Paths in it
are relative to the repository root, so they resolve as-is — except for the inputs listed in
`docs/EXCLUDED_DATA.md`, which must be refetched first (chiefly the ProstT5 weights and the
nucleotide genomes).

## 8. A note on scope

The bulk data — a 1.9 GB conda environment, 4.4 GB of ProstT5 weights and download scratch, a 2 GB
Pfam-A library, 85 MB of nucleotide genomes, and regenerable MMseqs2/Foldseek databases — is
deliberately absent. `docs/EXCLUDED_DATA.md` lists every excluded path with its size and restoration
route. The session logs were scanned for credentials before committing; none are present. Galaxy API
keys were always passed via the `GALAXY_API_KEY` environment variable and never written to disk.
