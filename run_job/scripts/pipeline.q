#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N WALLACEZ_RUN
#$ -cwd
#$ -o wallacez_run.log
#$ -j y
#$ -t 1-10:1

# compute parallel features
python3 run_job/scripts/compute_features.py output/sequences/seq_$SGE_TASK_ID
