# Agentic Development of Galaxy User-Defined Tools: A Case Study from the PIR/VIR Analysis

This document summarizes how Galaxy **User-Defined Tools (UDTs)** were authored, registered, executed,
diagnosed, and revised by an LLM agent over the course of Plan F — the Galaxy replication of the
*Plasmodium vivax* PIR/VIR structure-aware phylogenomics pipeline. The work ran on **usegalaxy.org**
(history `phist2`, `bbd44e69cb8906b5c0a92f1d9b046fdd`, user `aun1`) between 2026-05-27 and 2026-07-31.

Our interest here is methodological rather than biological. The scientific results live in
[`../notebook.md`](../notebook.md) and [`../paper_full.md`](../paper_full.md); what follows is a record
of what it actually takes for an agent to extend a public Galaxy server with containerized tools that
do not exist in the ToolShed, and what fails along the way.

---

## 1. Why UDTs were needed at all

The pipeline splits cleanly into components that the IUC ToolShed already covers and components it does
not. Three steps ran on stock ToolShed tools: `hmmsearch`
(`hmmer_hmmsearch/3.4+galaxy0`), MMseqs2 clustering
(`mmseqs2_easy_linclust_clustering/17-b804f+galaxy1`), and `iqtree/2.4.0+galaxy2`. Everything
structure-aware, plus every bespoke analysis script, had no wrapper — Foldseek with ProstT5 3Di
encoding, FoldMason lockstep AA+3Di alignment, six-frame pseudogene rescue from GFF3, reciprocal-best-hit
pairing, flanking-microsynteny scoring, spatial permutation testing, and alignment preprocessing for
IQ-TREE.

UDTs are the mechanism that closes this gap: containerized tools registered through the Galaxy API by an
ordinary user, with no administrative privileges and no ToolShed submission. That property is what makes
them tractable for an agent — the agent can author a tool definition, `POST` it, run it, read the
failure, and revise, all inside one loop.

## 2. Inventory

We registered **10 distinct UDT IDs across roughly 27 versions**, plus three early FoldMason variants
whose IDs the notebook does not record. Definitions for the final Foldseek pair are checked in under
[`../udt_defs/`](../udt_defs/).

| UDT ID | Purpose | Versions | Final container |
| :--- | :--- | ---: | :--- |
| `anton-1-gff_pseudogene_translator` | Parse GFF3 pseudogenic transcripts, six-frame translate | 3 | `quay.io/biocontainers/python:3.12.12` |
| `anton-gpu-xl-foldseek_prostt5_clustering` | Foldseek `easy-cluster` with ProstT5 3Di, GPU | 7 | `quay.io/biocontainers/foldseek:10.941cd33` |
| `anton-32-foldseek_prostt5_clustering` | Same, CPU-routed control | 1 | `quay.io/biocontainers/foldseek:10.941cd33` |
| `anton-1-foldseek_cluster_extract` | Pull one cluster's members out of a Foldseek TSV | 1 | `quay.io/biocontainers/python:3.12.12` |
| `anton-32-foldmason_align` | FoldMason lockstep AA + 3Di structural MSA | 4 | `quay.io/nekrut/foldmason-prostt5:4.dd3c235-cpu` |
| `anton-1-step7_prepare_fastas` | Split FS_001 by genome, subtract VIRs to build housekeeping sets | 1 | `quay.io/biocontainers/python:3.12.12` |
| `anton-8-mmseqs_easy_rbh_pair` | Paired reciprocal best hits | 2 | `quay.io/biocontainers/mmseqs2:18.8cc5c--hd6d6fdc_0` |
| `anton-1-microsynteny_filter` | Score RBH pairs against a flanking housekeeping backbone | 1 | `quay.io/biocontainers/python:3.12.12` |
| `anton-1-spatial_analysis` | Coordinate profiling, subtelomeric enrichment, label-shuffle tests | 3 | `quay.io/biocontainers/python:3.12.12` |
| `anton-1-iqtree_structural_prep` | trimAl-style occupancy trimming, concatenation, partition file | 1 | `quay.io/biocontainers/python:3.12.12` |

Version counts are the headline finding on their own. The Foldseek clustering tool took **seven
registrations** to reach a working state, and FoldMason took **seven attempts across two tool IDs**.
Only four of the ten tools worked on the first registration, and every one of those four was a plain
Python data-munging tool on a stock BioContainers image.

## 3. Naming as routing

Galaxy routes UDT jobs by a prefix convention embedded in the tool ID, which the agent had to learn and
then use deliberately:

- `anton-1-` → 1 core, the default destination for lightweight Python tools.
- `anton-8-`, `anton-32-` → 8 or 32 cores on CPU destinations.
- `anton-gpu-xl-` → 32 cores plus a GPU.

This is unusual and worth flagging for anyone automating against Galaxy: **the tool's identifier is
load-bearing infrastructure configuration, not just a label.** Renaming a tool changes where it runs.
We used this deliberately in Step 6, registering `anton-32-foldmason_align` specifically to move
FoldMason off the GPU destination once we established it needed no GPU — though that turned out not to
be the actual blocker (§4.4).

## 4. A failure taxonomy

The value of this record is in the failures. Seven distinct classes appeared, and only the last two are
about the science.

### 4.1 Templating collisions between shell syntax and the UDT engine

The very first Foldseek UDT (v1.0.0, UUID `006d1a86`) failed during Galaxy command-line construction
because shell `${...}` parameter expansion collided with UDT templating. The same class of failure
recurred twice more: `anton-8-mmseqs_easy_rbh_pair` v1.0.0 and `anton-32-foldmason_align` v1.0.2 both
died at command-line construction because shell command substitutions `$(...)` conflicted with the
`$(inputs.name.path)` reference syntax.

We diagnosed this empirically at the time. The official documentation supplies the mechanism: a
`shell_command` is **not** a shell string with variable interpolation but a string containing
**sandboxed JavaScript expressions inside `$( ... )`**. The documented example makes the evaluator
visible —

```yaml
shell_command: |
  cat $(inputs.datasets.map((input) => input.path).join(' ')) > output.txt
```

— `.map()` and `.join()` are JavaScript, evaluated before the shell ever sees the string. So a shell
command substitution `$(nproc)` is not passed through; it is parsed as a JavaScript expression and
fails. This is the single most useful thing to know before authoring a UDT, and it turns our empirical
rule into a principled one: **`$(...)` is reserved for the JavaScript layer, and shell syntax that
needs it must be avoided entirely.**

Our working tools assign inputs to shell variables once at the top (`threads="$(inputs.threads)"`) and
use plain `$threads` thereafter — which is correct precisely because `$threads` without parentheses is
invisible to the JavaScript evaluator and reaches the shell intact.

### 4.2 Container reference resolution

Three separate container-string formats were attempted before one resolved:

| Attempt | Container string | Outcome |
| :--- | :--- | :--- |
| v1.0.1 | `quay.io/biocontainers/foldseek:10.941cd33--h5021889_1` | Submitted, but superseded before verification |
| v1.0.2 | `foldseek:10.941cd33` (bare, for CVMFS) | `FATAL: Unable to handle docker://foldseek:10.941cd33 ... requested access to the resource is denied` |
| v1.0.3 | `quay.io/biocontainers/foldseek:10.941cd33` | **Resolved and ran** |

The bare identifier was an attempt to make Galaxy use a preconverted CVMFS image rather than build a SIF
at runtime. Galaxy accepted the field but the job runner's resolver still prefixed it into
`docker://foldseek:10.941cd33` and looked it up under `docker.io/library`, where it does not exist. The
working form is a fully qualified Quay path **without** the `docker://` prefix and **without** the
BioContainers build suffix.

A related failure hit the deterministic pseudogene translator: all four native runs (HIDs 60–63) died
before Python ever started, with Apptainer/proot failing to build a SIF from
`docker://quay.io/biocontainers/python:3.12.12` — `ptrace(TRACEME): Operation not permitted`. The agent
worked around this by generating the FASTAs locally and uploading them, which unblocked Step 4 at the
cost of that step no longer being a native Galaxy execution.

### 4.3 Missing interpreters inside the tool container

Foldseek UDT v1.0.4 ran Foldseek successfully — cluster assignments, representatives, and log all had
non-zero size — and then died with exit code 127:
`tool_script.sh: line 44: python: command not found`. The `foldseek` BioContainer ships no Python, and
the UDT's summary-generation block assumed one.

The fix in v1.0.5 was to rewrite per-cluster summarization in `awk` and `sort`, removing the Python
dependency entirely. That `awk` block survives in
[`../udt_defs/foldseek_gpu_newschema.json`](../udt_defs/foldseek_gpu_newschema.json) and is a small
lesson in itself: **a single-tool container is a single tool, and post-processing must be written
against what that container actually contains.**

### 4.4 Missing capabilities in the container *build*

The hardest blocker was not configuration but compilation. Three FoldMason UDT variants and a fourth
CPU-routed one all failed identically:

```
Foldseek was compiled without ProstT5 support
Error: Structure createdb died
```

The agent tested three hypotheses and disproved each: swapping to the Foldseek container plus an
upstream FoldMason AVX2 binary failed the same way; removing `--gpu` and re-routing to a CPU
destination failed the same way; and a **local** probe using Conda `foldmason` 4.dd3c235 on the same
input failed the same way. That last test is the decisive one — it moved the diagnosis from "Galaxy is
misconfigured" to "no available FoldMason build supports FASTA+ProstT5," which is a fundamentally
different problem and correctly ended the retry loop.

Resolution required a purpose-built image, `quay.io/nekrut/foldmason-prostt5:4.dd3c235-cpu`. Even then
two more registrations were needed: v1.0.1 failed with exit 127 because the upstream-style container
puts no `foldmason` on `PATH`, exposing `/usr/local/bin/entrypoint` instead, and v1.0.2 failed on the
templating collision of §4.1. Version 1.0.3 (UUID `b9cc1615`) invoked `/usr/local/bin/entrypoint`
directly and produced 336 sequences aligned across 10,128 columns in both AA and 3Di.

### 4.5 Silent semantic errors in the tool's own logic

`anton-1-spatial_analysis` illustrates the failure mode that container plumbing cannot catch, because
every version ran to `ok`:

- **v1.0.0** parsed Galaxy HMMER per-sequence output directly and recovered 859 / 696 / 921 VIR IDs
  instead of the verified 931 / 748 / 985.
- **v1.0.1** used the verified ID lists but chose top chromosomes across all proteins, giving a PvP01
  main-chromosome count of 303 against the local baseline of 347.
- **v1.0.2** applied the local pipeline's actual rule — top 14 VIR-bearing contigs per genome ranked by
  maximum VIR coordinate — and reproduced 347 / 634 / 735 exactly.

All three were green in Galaxy. Only comparison against an independent local baseline distinguished
them, which is the strongest argument in this whole record for maintaining a verified reference
implementation alongside any agentic platform port.

### 4.6 Nondeterminism in the ported science

Step 3's translator matched local record IDs and counts (1,110 PvP01, 1,932 PvPAM) but produced
sequences that were not byte-identical. The cause was
`sorted(set(exons), key=lambda e: e[1])` — unstable when a `pseudogenic_transcript` record and a child
`exon` record share a start coordinate, so runtime ordering decides which segment is stitched first,
which changes the translation and therefore the downstream HMMER hits.

The agent rewrote the rule to be biologically explicit — prefer child exons, fall back to the transcript
span only when no exons exist, sort by `(seqid, start, end, strand)` — and registered it as v1.0.3. The
deterministic workflow yields 83 PvP01 and 78 PvPAM pseudogene loci at strict full-sequence E ≤ 1e-3,
against the historical 75 / 70. Chasing that discrepancy also exposed that the checked-in
`PvPAM_pseudo_PF05795.tbl` is stale relative to the current HMMER 3.4 toolchain: a fresh local rerun
gives 65 loci, not 70. **A reproducibility investigation that started as a Galaxy port ended by
invalidating a number in the local baseline.**

### 4.7 Platform-level defects outside the tool

Not every failure was ours. In the `smbe-a/` sub-project, usegalaxy.org returned
`Error occurred while building config files for tool 'upload1'` for the standard uploader,
the same for `__DATA_FETCH__`, and a tus 500 for local-file upload. The agent diagnosed this as
server-side, switched to usegalaxy.eu, and completed the import there. Recognizing that a failure is
*not* the agent's to fix is its own competence.

## 5. Instrumentation: making jobs self-describing

A recurring difficulty is that an agent cannot inspect a compute node. Its only channel is what the job
writes to disk. The mature UDTs therefore emit a dedicated **environment report** output alongside their
scientific outputs — a deliberate design pattern rather than an afterthought. The Foldseek tools write
`foldseek_env_report.txt` containing the UDT variant name, the literal GPU flag compiled into the
command, the requested thread count, `$GALAXY_SLOTS`, `CUDA_VISIBLE_DEVICES`, `NVIDIA_VISIBLE_DEVICES`,
`$PATH`, `foldseek version`, and `nvidia-smi` output, all wrapped in `|| true` so diagnostics never fail
the job.

This paid off directly in the CPU/GPU routing test, which produced the cleanest infrastructure result of
the project. The GPU variant reported `UDT variant: gpu-xl-new-schema`, `--gpu 1`, `GALAXY_SLOTS: 32`,
and an `NVIDIA A100-SXM4-40GB` under CUDA 12.7; the CPU variant reported `--gpu 0`, `GALAXY_SLOTS: 32`,
and `nvidia-smi: command not found`. **Galaxy honors new-style UDT resource declarations** — a claim we
could state as verified rather than assumed, purely because the tools were built to report on
themselves.

## 6. The new-style schema

The final Foldseek pair was rewritten against the updated `GalaxyUserTool` authoring style, which is the
form worth copying:

```json
{
  "class": "GalaxyUserTool",
  "id": "anton-gpu-xl-foldseek_prostt5_clustering",
  "version": "2.0.0",
  "container": "quay.io/biocontainers/foldseek:10.941cd33",
  "requirements": [{
    "type": "resource",
    "cores_min": 32, "ram_min": 8192,
    "cuda_device_count_min": 1, "cuda_device_count_max": 1,
    "gpu_memory_min": 1
  }],
  "shell_command": "...",
  "inputs":  [{"name": "seqs", "type": "data", "format": "fasta"}, ...],
  "outputs": [{"name": "cluster_tsv", "type": "data", "format": "tabular",
               "from_work_dir": "vir_struct_cluster_cluster.tsv"}, ...],
  "help": {"format": "markdown", "content": "..."}
}
```

Four properties matter. `shell_command` replaces older command templating. Data inputs are referenced as
`$(inputs.NAME.path)` and scalars as `$(inputs.NAME)`. Outputs bind to fixed filenames via
`from_work_dir`, so the shell command must write predictable names. And an explicit `requirements` block
of type `resource` declares cores, RAM, and GPU count — which, per §5, Galaxy genuinely honors.

Local validation of these definitions against the Galaxy Python model was attempted and blocked by a
missing `pydantic` in the project environment; server-side creation validation accepted both. Registration
was scripted in
[`../udt_defs/foldseek_udt_newstyle_register.py`](../udt_defs/foldseek_udt_newstyle_register.py).

## 6a. Reconciling with the official documentation

After the fact we checked our findings against the two official sources — the community page at
[galaxyproject.org/tools/user-defined-tools](https://galaxyproject.org/tools/user-defined-tools) and the
admin reference at
[docs.galaxyproject.org/en/master/admin/user_defined_tools.html](https://docs.galaxyproject.org/en/master/admin/user_defined_tools.html).
Three things we relied on turn out to be **undocumented behavior**, which is worth stating plainly
because it means they can change without notice.

| What we did | Documentation status |
| :--- | :--- |
| `requirements: [{type: resource, cores_min, ram_min, cuda_device_count_min/max, gpu_memory_min}]` | **Not documented.** No resource-requirement block appears in either source. The server accepted it and, per §5, demonstrably honored it. |
| Tool-ID prefix drives job routing (`anton-1-`, `anton-32-`, `anton-gpu-xl-`) | **Not documented.** Neither source mentions job routing, destination selection, or ID conventions. |
| Container string must be a fully-qualified Quay path with no `docker://` and no build suffix | **Not documented.** Both sources require the `container` key but describe no resolution mechanism or fallback. |
| Registration scripted through the Galaxy API | **Not documented.** Both sources describe authoring through the Tools panel UI only. |

Conversely, the documentation states several constraints we should have known up front:

- **UDTs are a beta feature, currently UseGalaxy.org only.** They require `enable_beta_tool_formats:
  true` plus **Custom Tool Creation** and **Custom Tool Execution** roles.
- **Definitions are canonically YAML**, not JSON. Our JSON payloads work because JSON is a subset of
  YAML, but examples and future tooling assume YAML.
- **Every UDT must run in a container** — there is no host-execution option. This is why §4.3 and §4.4
  are structural rather than incidental: the container *is* the environment, so anything it lacks is
  simply unavailable.
- **The input vocabulary is deliberately restricted** to `boolean`, `integer`, `float`, `text`,
  `select`, `color`, `data`, `data_collection`, plus the structural groups `conditional`, `repeat`, and
  `section`. Types such as `hidden`, `drill_down`, `data_column`, `genomebuild`, `group_tag`, `baseurl`,
  `rules`, and `directory` are **rejected at parse time**.
- **Three hard limitations:** no access to Galaxy reference data, no access to dataset metadata or
  metadata files (BAM indexes and the like), and no access to a tool's `extra_files` directory.

The most consequential documented limitation, for our purposes, is this one:

> *"Test cases aren't supported yet."*

There is no in-platform mechanism for asserting that a UDT produces the right answer. That single line
retroactively justifies the entire download-and-verify loop of §7: external verification against an
independent baseline is not merely good hygiene here, it is **the only available form of testing**. The
three silently-wrong `spatial_analysis` versions in §4.5 are what that gap looks like in practice.

One useful thing we did not need but which matters for anyone building on this: **UDTs are private to
their creator by default.** Embedding a UDT in a workflow and sharing that workflow gives each importer
their own copy of the tool automatically, and an administrator can export a UDT to disk and install it
instance-wide. That is the migration path from a personal UDT to a shared tool.

## 7. Verification discipline

The agent's working loop was uniform across all nine steps and is the reason the failures above were
caught rather than absorbed: register the UDT, submit with explicit parameters, poll to a terminal
state, **download every output to a local `galaxy_step<N>/` directory, re-parse it locally, and compare
against the local baseline.** Outputs are stored under filenames of the form `hid<N>_*`, preserving the
Galaxy history dataset ID, so any committed file maps back to the exact Galaxy dataset that produced it.
Failure logs are retained under the same convention — `galaxy_step6/` holds six `*_failed.log` files, and
they are the primary evidence for §4.4.

Polling deserves a note. Step 9's IQ-TREE job stayed `running` through **80 one-minute polls**, and the
agent's correct behavior was to record the step as incomplete rather than infer success. An agent that
treats "submitted" as "done" would have reported Plan F as finished.

## 8. What the infrastructure work revealed about the science

Two results emerged from platform work rather than analysis, and both change how the Galaxy branch must
be interpreted.

**GPU and CPU Foldseek do not agree.** With input, coverage, E-value, and alignment type all held fixed
on the same 2,592 proteins, the local CPU run gives 73 clusters with FS_001 = 1,197, while the Galaxy GPU
run gives 76 clusters with FS_001 = 812. The agent isolated the variable properly: a `threads=8` rerun
reproduced the GPU result exactly (76 clusters, largest 812), eliminating thread count as the cause and
leaving `--gpu 1` as the only substantive difference. Top-ten size distributions diverge sharply —
GPU `[812, 721, 350, 235, 93, ...]` against local `[1197, 385, 248, 143, 136, ...]`. The later CPU
routing test produced a third answer again (76 clusters, FS_001 = 766).

You explicitly accepted the GPU result as *the* Galaxy branch rather than forcing bit-level reproduction.
That decision is why Galaxy Step 7 legitimately reports 3 high-confidence orthologs where the local
branch reports 11 — the branches cluster differently, so downstream counts differ by construction, and
any cross-branch comparison must account for it.

**Sparse alignments propagate into phylogenetics.** The Galaxy FoldMason alignment reaches only 25%
maximum per-column occupancy, so the local `trimal -gt 0.65` threshold retains zero columns. At the
0.20 threshold that was used instead, 160 of 336 sequences are all-gap in the retained columns and
IQ-TREE silently analyzed 176 taxa. This is documented in
[`../README.md`](../README.md) §5 as the main open thread.

## 9. Practical guidance

For anyone driving Galaxy UDTs from an agent, the record supports six concrete recommendations.

1. **Verify against an independent baseline.** Job state `ok` is not correctness. Three consecutive
   green `spatial_analysis` runs were wrong in three different ways.
2. **Make every tool report its own environment.** A diagnostics output wrapped in `|| true` costs
   nothing and converts guesses about the runtime into evidence.
3. **Prefer fully-qualified Quay paths without `docker://` and without build suffixes.** Bare names get
   rewritten toward Docker Hub and fail.
4. **Never assume an interpreter.** Post-processing inside a single-tool container should use POSIX
   text utilities, or run as a separate tool on an image that has what it needs.
5. **Probe locally before iterating remotely.** One local Conda run ended a four-attempt Galaxy retry
   loop by proving the blocker was the FoldMason build, not the platform.
6. **Treat nondeterminism as a defect to fix, not a discrepancy to explain.** Making the exon-ordering
   rule explicit both fixed the tool and exposed a stale number in the reference baseline.
7. **Read `shell_command` as JavaScript, not shell.** `$(...)` is a sandboxed JS expression evaluated
   before the shell runs. Assign inputs to shell variables once at the top, then use bare `$var`.
8. **Know which of your dependencies are undocumented.** Resource requirements, ID-prefix routing, and
   container-string resolution all worked for us but appear in no official documentation, so they carry
   no stability guarantee. Pin what you can and re-verify after platform upgrades.

The broader observation is that the agent spent far more effort on containers, routing, templating, and
verification than on the biology. Of roughly 27 UDT registrations, only about ten encoded new
scientific logic; the rest were responses to infrastructure failures. That ratio is the honest cost of
porting a research pipeline to a shared platform, and it is precisely the kind of long, low-novelty,
high-persistence work that suits an agent — provided it verifies every result against something it did
not produce itself.
