#!/bin/bash

# Run the merging script after parallel computation.
# class<x>.txt is name of the file that either the class 1 or class 2 
# features will be merged into.

if [ $1 = "" ] ; then
    echo "usage: ./merge_files.sh class<x>.txt"
    exit 0
fi

echo "Waiting for SGE parallel job to finish..."
sleep 3

echo "Merging features into $1"
python3 run_job/scripts/merge_files.py $1
