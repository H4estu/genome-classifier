#!/usr/bin/env/python3
# merge_files.py
#  
# Input: N files of sequence data.
# Output: N x M table of N sequences and M features.

import os
import sys

from subprocess import call

def main(header_path, feature_path, merge_path, merge_file_name):

    if not 'merge' in os.listdir(header_path):
        # if output directory doesn't exist, create one.
        os.mkdir(merge_path)
    else:
        print('Creating', merge_file_name)

    feature_files = os.listdir(feature_path)
    merge_files   = os.listdir(merge_path)

    # create header row in feature table file.
    merged_feature_file = merge_path + merge_file_name

    with open(merged_feature_file,'w') as ft:
        header = [r'Sequence_ID', r'GC_Content', r'A_Content', r'Start_Codons']
#        header = ['Sequence_ID', 'percent_GC', 'percent_A', 'percent_T']
        # header = ['Sequence_ID', 
        #           'percent_G','percent_C', 
        #           'percent_A', 'percent_T',
        #           'Start_Codons']
        ft.write('\t'.join(header) + '\n')

    # merge and write feature data to tab-delimited file.
    for ffile in feature_files:
        with open(feature_path+ffile, 'r') as f:
            lines = f.readlines()
            for row in lines:
                row = row.strip()
                row = row.split(' ')
                with open(merged_feature_file, 'a') as m:
                    m.write('\t'.join(row) + '\n')

if __name__ == '__main__':  
    merge_file_name = sys.argv[1]  
    path_head  = 'output/'
    path_feat  = path_head + 'features/'
    path_merge = path_head + 'merge/'

    main(path_head, path_feat, path_merge, merge_file_name)
