# Data excluded from this repository

The working analysis directory (`~/.loom/analyses/phist2`) is **9.4 GB across ~92,000 files**.
This repository holds **~170 MB / ~680 files**: every script, notebook, log, report, figure,
alignment, tree, and derived table, but none of the bulk binaries. What follows is the complete
list of what was dropped and how to get it back.

| Excluded path | Size | Nature | How to restore |
| :--- | ---: | :--- | :--- |
| `.loom/env/` | 1.9 GB | Conda environment created by loom for the local pipeline | Recreate from the tool registry in [`pipeline.md`](../pipeline.md) §1 (all tools are `bioconda` packages with pinned versions) |
| `data/genomes/alignments/prostt5_weights/` | 2.3 GB | ProstT5 model weights (`prostt5-f16.gguf`) | `foldseek databases ProstT5 <outdir> tmp`, or let `foldseek createdb --prostt5-model` download them |
| `data/genomes/alignments/tmp_prostt5/` | 2.1 GB | Download scratch for the same weights (`prostt5-f16-gguf.tar.gz`) | Not needed |
| `data/hmm/Pfam-A.hmm` | 2.0 GB | Full Pfam-A HMM library | Download from InterPro/Pfam; only `PF05795` is used, and the extracted `data/hmm/VIR.hmm` (176 KB) **is** committed |
| `data/genomes/alignments/AlignmentViewer2.0/` | 514 MB | Vendored third-party checkout used to eyeball alignments | `git clone` upstream if needed |
| `data/genomes/alignments/fs_clusters/struct_msa/` + `foldmason_work/` | 441 MB | FoldMason/Foldseek intermediate databases | Regenerate with `fs_clusters/build_struct_msa.sh` (committed) |
| `data/genomes/nuc/` | 85 MB | Nucleotide genome FASTAs for PvP01, PvW1, PvPAM | PlasmoDB release 71 |
| `*.ufboot`, `*.ckp.gz` under `phylo_q1/trees`, `phylo_q2/trees` | ~55 MB | IQ-TREE bootstrap replicate dumps and checkpoints | Regenerate by rerunning IQ-TREE; the `.treefile`, `.iqtree`, `.mldist`, `.splits.nex`, and `.log` outputs **are** committed |
| MMseqs2/Foldseek `*.db*` blobs, `mmseqs_tmp/`, `mm_tmp/`, `tmp_hk/`, `foldseek_work/tmp/` | ~20 MB | Binary databases and scratch | Regenerate with the `mmseqs createdb` / `foldseek createdb` commands in `pipeline.md` |
| `smbe-a/zenodo_5119008_fastq/` | ~1 MB | Raw FASTQ read pairs (M117, M117C1; blood + cheek) | Zenodo record 5119008 |
| `data/pseudogenes/galaxy_input_Pvivax{P01,PAM}.gff` | 15 MB | Byte-identical duplicates of `data/genomes/gff/Pvivax{P01,PAM}.gff` | Already in repo under `data/genomes/gff/` |

## What *is* committed

- All prose: `notebook.md` (the primary lab notebook, 1,273 lines), `pipeline.md` (the reproducible
  command ledger), `paper_full.md`, `paper.pdf`, `pvivax_PIR_characterization.pdf`, `results.md`.
- All code: `verification/verify_claims.py`, `data/genomes/*.py`, `data/genomes/alignments/*.py`,
  `phylo_q1/plot_trees.R`, `phylo_q2/plot_and_test.R`, `fs_clusters/build_struct_msa.sh`.
- All Galaxy user-defined tool (UDT) definitions under `udt_defs/`.
- All Galaxy run outputs under `galaxy_step*/` (named `hid<N>_*` after their Galaxy history dataset IDs),
  including the failure logs — the FoldMason container failures in `galaxy_step6/` are part of the record.
- Proteome FASTAs, GFFs, HMMER tables, cluster assignments, alignments, trimmed alignments, trees,
  ortholog tables, and spatial tables.
- Agent session transcripts under `sessions/` (`phist2_session.jsonl`, `smbe-a_session.jsonl`) and
  `activity.jsonl`, so the reasoning behind each decision stays recoverable.

The session logs were scanned for credentials before committing: no API keys, tokens, or passwords are
present. Galaxy API keys were always supplied through the `GALAXY_API_KEY` environment variable and
never written to disk.
