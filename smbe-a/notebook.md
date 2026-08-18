# SMBE-A Project Notebook

## 2026-06-29 — Galaxy history setup: SMB Demo

- Created Galaxy history **SMB Demo** on usegalaxy.org.
  - History ID: `bbd44e69cb8906b50b0cab212dbf865a`
- Source requested: Zenodo record `https://zenodo.org/records/5119008` (`Datasets for Galaxy Collection Operations Tutorial`).
- Intended FASTQ files:
  - `M117C1-ch_2.fq.gz`
  - `M117-ch_1.fq.gz`
  - `M117C1-bl_2.fq.gz`
  - `M117C1-bl_1.fq.gz`
  - `M117-ch_2.fq.gz`
  - `M117-bl_2.fq.gz`
  - `M117-bl_1.fq.gz`
  - `M117C1-ch_1.fq.gz`
- Upload attempts:
  - Galaxy MCP `upload_file_from_url` submitted datasets, but all failed with `Error occurred while building config files for tool 'upload1'`.
  - Direct Galaxy `/api/tools/fetch` URL and pasted-text smoke tests also failed with `Error occurred while building config files for tool '__DATA_FETCH__'`.
  - Galaxy MCP local-file upload failed before job submission with `Communication with tus server failed with status 500`.
- Local fallback download:
  - Downloaded the 8 FASTQ files to `zenodo_5119008_fastq/`.
  - Verification: `gzip -t *.fq.gz` completed successfully; local FASTQ gzip integrity is OK.
- Current status: Galaxy history exists, but FASTQ import into Galaxy is **not verified / not complete** because Galaxy upload/fetch infrastructure returned server-side errors.

```loom-session
id: 019f11e7-ab3c-78cc-917f-010d47fb0f58
started_at: 2026-06-29T05:43:43.661Z
ended_at: 2026-06-29T06:35:38.390Z
notebook: notebook.md
orphaned_active_steps: 0
```

## 2026-06-29 — Galaxy history setup on usegalaxy.eu: smbe-demo

- Connected to **usegalaxy.eu** and created Galaxy history **smbe-demo**.
  - History ID: `11ac94870d0bb33a0987eaf8ad836c69`
- Imported 8 FASTQ datasets from Zenodo record `https://zenodo.org/records/5119008`:
  - `M117C1-ch_2.fq.gz` — dataset `26c75dcccb616ac82bdb258c967d8f0a`
  - `M117-ch_1.fq.gz` — dataset `26c75dcccb616ac8244052abb1709646`
  - `M117C1-bl_2.fq.gz` — dataset `26c75dcccb616ac8cfe54a2d1e628959`
  - `M117C1-bl_1.fq.gz` — dataset `26c75dcccb616ac8f6a94f691831029c`
  - `M117-ch_2.fq.gz` — dataset `26c75dcccb616ac87cda66da6aea637a`
  - `M117-bl_2.fq.gz` — dataset `26c75dcccb616ac8bda8c90d31525646`
  - `M117-bl_1.fq.gz` — dataset `26c75dcccb616ac805b776a25cb070a7`
  - `M117C1-ch_1.fq.gz` — dataset `26c75dcccb616ac8283d58e0ff1b5387`
- Verification:
  - `galaxy_get_history_contents` returned 8 visible datasets in state `ok`.
  - Each dataset has datatype `fastqsanger.gz`, `metadata_sequences: 1000`, and `metadata_data_lines: 4000`.
  - Dataset sizes are non-zero (range 93,563–119,127 bytes).
  - Preview inspection showed valid FASTQ structure (`@...`, sequence, `+`, quality) for uploaded reads.

### Added reference FASTA

- Uploaded `chrM.fa.gz` from Zenodo record `https://zenodo.org/records/5119008` to **smbe-demo** on usegalaxy.eu.
  - Dataset ID: `26c75dcccb616ac8feedf118df533e3c`
- Verification:
  - Dataset state is `ok`.
  - Datatype is `fasta.gz`; file size is 5,549 bytes.
  - Metadata reports `metadata_sequences: 1` and `metadata_data_lines: 333`.
  - Preview begins with FASTA header `>chrM` followed by mitochondrial sequence content.

## 2026-06-29 — Launched haploid variant calling on smbe26

- Workflow: **Paired end variant calling in haploid system** (`#workflow/github.com/iwc-workflows/haploid-variant-calling-wgs-pe/main`), imported as Galaxy workflow `1622bef4ea184f60`.
- Galaxy history: **smbe26** (`11ac94870d0bb33a0a38ca6171654a84`) on usegalaxy.eu.
- Invocation ID: `886a87e4e0bb6974`.
- Inputs:
  - Paired FASTQ collection `data`: `216f370ebbef0c0b`
  - Annotation GTF: `26c75dcccb616ac8a081e9f5d53c5247`
  - Genome FASTA: `26c75dcccb616ac8189cc31b82d38b65`
- Verification pending: workflow invocation has been submitted; final status and outputs still need to be polled and inspected.

```loom-invocation
invocation_id: 886a87e4e0bb6974
galaxy_server_url: https://usegalaxy.eu
notebook_anchor: smbe26-haploid-variant-calling
label: Haploid variant calling on smbe26
submitted_at: 2026-06-29T06:15:18.794Z
status: in_progress
summary: 
total_steps: 16
completed_steps: 0
total_jobs: 0
completed_jobs: 0
failed_jobs: 0
last_polled_at: 2026-06-29T06:35:33.597Z
```
