import json
from pathlib import Path

COMMON_AWK = r'''awk -F '\t' '
function genome(pid) {
    if (pid ~ /^PVP01/) return "PvP01";
    if (pid ~ /^PVPAM/) return "PvPAM";
    if (pid ~ /PvW1/ || pid ~ /PVW1/ || pid ~ /PVPVW/ || pid ~ /PVPV/) return "PvW1";
    if (pid ~ /^CAG/) return "PvW1";
    if (pid ~ /^CAI/) return "PvPAM";
    return "unknown";
}
{
    rep=$1; member=$2; key=rep SUBSEP member;
    if (!(key in seen)) {
        seen[key]=1;
        size[rep]++;
        g=genome(member);
        count[rep,g]++;
    }
}
END {
    for (rep in size) {
        printf "%d\t%s\t%d\t%d\t%d\t%d\t%d\n", -size[rep], rep, size[rep]+0, count[rep,"PvP01"]+0, count[rep,"PvW1"]+0, count[rep,"PvPAM"]+0, count[rep,"unknown"]+0;
    }
}' vir_struct_cluster_cluster.tsv | sort -k1,1n -k2,2 | awk -F '\t' 'BEGIN {print "cluster_id\trepresentative\tsize\tPvP01\tPvW1\tPvPAM\tunknown"} {printf "FS_%03d\t%s\t%s\t%s\t%s\t%s\t%s\n", NR, $2, $3, $4, $5, $6, $7}' > foldseek_clusters_summary.tsv'''

def shell(gpu_flag: int, variant: str) -> str:
    return f'''set -eo pipefail
threads="$(inputs.threads)"
mkdir -p prostt5_weights tmp
cp '$(inputs.prostt5_model.path)' prostt5_weights/prostt5-f16.gguf

{{
  echo "UDT variant: {variant}"
  echo "Foldseek command GPU flag: --gpu {gpu_flag}"
  echo "Requested threads input: $threads"
  echo "GALAXY_SLOTS: $GALAXY_SLOTS"
  echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
  echo "NVIDIA_VISIBLE_DEVICES: $NVIDIA_VISIBLE_DEVICES"
  echo "PATH: $PATH"
  echo "Foldseek version:"
  foldseek version
  echo "nvidia-smi:"
  nvidia-smi
}} > foldseek_env_report.txt 2>&1 || true

echo "Foldseek version:" > foldseek.log
foldseek version >> foldseek.log 2>&1 || true
echo "UDT variant: {variant}" >> foldseek.log
echo "Threads input: $threads" >> foldseek.log
echo "GALAXY_SLOTS: $GALAXY_SLOTS" >> foldseek.log
echo "GPU flag: --gpu {gpu_flag}" >> foldseek.log
echo "Resource diagnostics written to foldseek_env_report.txt" >> foldseek.log

foldseek easy-cluster \
  '$(inputs.seqs.path)' \
  vir_struct_cluster \
  tmp \
  --prostt5-model prostt5_weights \
  -c '$(inputs.coverage)' \
  -e '$(inputs.evalue)' \
  --alignment-type '$(inputs.alignment_type)' \
  --gpu {gpu_flag} \
  --threads "$threads" >> foldseek.log 2>&1

{COMMON_AWK}

ls -lh vir_struct_cluster* foldseek_clusters_summary.tsv foldseek.log foldseek_env_report.txt >> foldseek.log 2>&1
'''

def tool(gpu: bool):
    if gpu:
        tid="anton-gpu-xl-foldseek_prostt5_clustering"
        version="2.0.0"
        name="Foldseek ProstT5 Structural Clustering (GPU XL, new UDT schema)"
        desc="Run Foldseek easy-cluster with ProstT5-derived 3Di states, explicit --gpu 1, resource requirements, and routing diagnostics."
        variant="gpu-xl-new-schema"
        gpu_flag=1
        resources={"type":"resource","cores_min":32,"ram_min":8192,"cuda_device_count_min":1,"cuda_device_count_max":1,"gpu_memory_min":1}
        default_threads=32
    else:
        tid="anton-32-foldseek_prostt5_clustering"
        version="1.0.0"
        name="Foldseek ProstT5 Structural Clustering (32 Core CPU, new UDT schema)"
        desc="Run Foldseek easy-cluster with ProstT5-derived 3Di states, explicit --gpu 0, resource requirements, and routing diagnostics."
        variant="cpu-32-new-schema"
        gpu_flag=0
        resources={"type":"resource","cores_min":32,"ram_min":8192,"cuda_device_count_max":0}
        default_threads=32
    return {
        "class":"GalaxyUserTool",
        "id":tid,
        "version":version,
        "name":name,
        "description":desc,
        "container":"quay.io/biocontainers/foldseek:10.941cd33",
        "requirements":[resources],
        "shell_command":shell(gpu_flag, variant),
        "inputs":[
            {"name":"seqs","label":"Protein FASTA to cluster","type":"data","format":"fasta"},
            {"name":"prostt5_model","label":"ProstT5 GGUF model file","type":"data"},
            {"name":"coverage","label":"Coverage threshold (-c)","type":"float","value":0.8},
            {"name":"evalue","label":"E-value threshold (-e)","type":"float","value":0.001},
            {"name":"alignment_type","label":"Foldseek alignment type","type":"integer","value":2},
            {"name":"threads","label":"Threads passed to Foldseek","type":"integer","value":default_threads}
        ],
        "outputs":[
            {"name":"cluster_tsv","label":"Foldseek cluster assignments","type":"data","format":"tabular","from_work_dir":"vir_struct_cluster_cluster.tsv"},
            {"name":"representatives","label":"Foldseek representative sequences","type":"data","format":"fasta","from_work_dir":"vir_struct_cluster_rep_seq.fasta"},
            {"name":"all_sequences","label":"Foldseek all cluster sequences","type":"data","format":"fasta","from_work_dir":"vir_struct_cluster_all_seqs.fasta"},
            {"name":"cluster_summary","label":"Foldseek cluster summary","type":"data","format":"tabular","from_work_dir":"foldseek_clusters_summary.tsv"},
            {"name":"foldseek_log","label":"Foldseek run log","type":"data","format":"txt","from_work_dir":"foldseek.log"},
            {"name":"environment_report","label":"Galaxy routing and GPU environment report","type":"data","format":"txt","from_work_dir":"foldseek_env_report.txt"}
        ],
        "help":{
            "format":"markdown",
            "content":f"""Run Foldseek `easy-cluster` on a protein FASTA using a supplied ProstT5 GGUF model file. This new-style UDT uses `class: GalaxyUserTool`, `shell_command`, explicit `$(inputs.name.path)` data references, fixed work-directory outputs, and a resource requirement block.\n\n**Inputs**: protein FASTA, ProstT5 model file, coverage, E-value, alignment type, and thread count. The GPU version passes `--gpu 1`; the CPU version passes `--gpu 0`.\n\n**Outputs**: Foldseek cluster TSV, representative FASTA, all-sequences FASTA, cluster summary, Foldseek log, and an environment report recording `$GALAXY_SLOTS`, CUDA/NVIDIA visibility variables, Foldseek version, and `nvidia-smi` output if available. Use the environment report to test whether Galaxy honored CPU/GPU routing."""
        }
    }

out={"gpu":tool(True),"cpu":tool(False)}
Path('udt_defs/foldseek_gpu_newschema.json').write_text(json.dumps(out['gpu'],indent=2))
Path('udt_defs/foldseek_cpu_newschema.json').write_text(json.dumps(out['cpu'],indent=2))
print(json.dumps(out))
