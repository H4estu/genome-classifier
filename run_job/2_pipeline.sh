#!/bin/bash
# pipeline.sh
#
# Run the parallel feature computation script.

# Ensure proper number of arguments given.
if [ $1 = ""] ; then
    echo "usage: ./pipline.sh <fasta_file>"
    exit 0
fi

export fasta_file_name=$1
#export merge_file_name=$2 

python3 run_job/scripts/fasta2seq.py $fasta_file_name

export feat_path="output/features/"
export seq_path="output/sequences/"

# ensure files aren't leftover from previous runs
 rm -f wallacez_run.log

export num=0
for i in $( ls $seq_path ) ; do
    num=$((num + 1))
done

echo "$num sequences"

# Compute features in parallel
./run_job/scripts/submit.sh
