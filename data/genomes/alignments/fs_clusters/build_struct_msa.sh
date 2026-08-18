#!/bin/bash
# Build a structure-aware MSA for a single cluster using Foldseek result2msa,
# then extract just the representative-anchored entry as a FASTA file.
set -e

CLUSTER=$1
REP=$2
FOLDSEEK=/Users/anton/.loom/analyses/phist2/.loom/env/bin/foldseek
PROSTT5=/Users/anton/.loom/analyses/phist2/data/genomes/alignments/prostt5_weights

cd /Users/anton/.loom/analyses/phist2/data/genomes/alignments/fs_clusters

# 1. Create db (uses ProstT5 to encode sequences -> 3Di)
$FOLDSEEK createdb "${CLUSTER}_unaligned.fasta" "struct_msa/${CLUSTER}_db" \
    --prostt5-model "$PROSTT5" --threads 1 > /dev/null 2>&1

# 2. All-vs-all structural search
$FOLDSEEK search "struct_msa/${CLUSTER}_db" "struct_msa/${CLUSTER}_db" \
    "struct_msa/${CLUSTER}_result" "struct_msa/tmp_${CLUSTER}" \
    -a -e 0.001 -c 0.5 --alignment-type 2 --threads 1 > /dev/null 2>&1

# 3. Build MSA db
$FOLDSEEK result2msa "struct_msa/${CLUSTER}_db" "struct_msa/${CLUSTER}_db" \
    "struct_msa/${CLUSTER}_result" "struct_msa/${CLUSTER}_msa" \
    --msa-format-mode 2 --threads 1 > /dev/null 2>&1

# 4. Find DB key of the rep
KEY=$(awk -v rep="$REP" '$2 == rep {print $1}' "struct_msa/${CLUSTER}_db.lookup")
if [ -z "$KEY" ]; then
    echo "$CLUSTER FAILED: rep $REP not found in lookup"
    exit 1
fi

# 5. Extract rep's MSA entry and write as plain FASTA
python3 << PYEOF
import re
with open("struct_msa/${CLUSTER}_msa.index") as f:
    for line in f:
        k, off, length = line.strip().split("\t")
        if int(k) == ${KEY}:
            with open("struct_msa/${CLUSTER}_msa","rb") as g:
                g.seek(int(off))
                raw = g.read(int(length)).decode("utf-8", errors="replace").rstrip("\x00")
            with open("${CLUSTER}_struct.aln","w") as h:
                h.write(raw)
            break
PYEOF

# Clean up large intermediate files but keep the db
rm -rf "struct_msa/tmp_${CLUSTER}"
rm -f "struct_msa/${CLUSTER}_msa" "struct_msa/${CLUSTER}_msa.index" "struct_msa/${CLUSTER}_msa.dbtype"
rm -f "struct_msa/${CLUSTER}_result"* 

N_SEQ=$(grep -c "^>" "${CLUSTER}_struct.aln" || echo 0)
echo "$CLUSTER OK: $N_SEQ sequences in rep-anchored structural MSA"
