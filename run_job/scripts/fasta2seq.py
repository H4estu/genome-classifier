#!/usr/bin/env/python3
# fasta2seq.py
# Transform a fasta file of sequences into an array of sequences
#
# Input: FASTA file.
# Output: Array of sequences

import numpy as np
import os
import sys
import re

def split_sequences(fasta_file):
    seq_list = list()  # initialize empty sequence list.

    pattern_head = re.compile('>')  # Find angle bracket at beginning of Fasta seq
    pattern_seq = re.compile('[ACTG]')  # Match any A,T,C or G at beginning
    seq = ''

    # parse sequences from FASTA file into a list with each sequence as an entry.
    # with open('FASTA/exonseq_upstream100_MT.txt','r') as f:
    with open(fasta_file,'r') as f:
        fasta_lines = f.readlines()
        for line in fasta_lines:
            line = line.strip('\n')
            if pattern_seq.match(line):
                seq += line
            elif pattern_head.match(line):
                if seq:  # prevent empty string at beginning of list.
                    seq_list.append(seq)
                    seq = ''
            else:
                print('Unknown Sequence at', len(seq_list))
        seq_list.append(seq)  # Push final sequence to list, since it was ignored by the parser.
    
    return seq_list

def split_to_lines(sequence_list, num_files):
    # remove existing directory to prevent accidental inclusion of 
    # sequences from previous runs.
    outpath = 'output/sequences/'
    outdir = os.listdir(outpath)
    for ffile in outdir:
        os.remove(outpath + ffile)

    nlines = len(sequence_list)
#    line_chunks = np.round(nlines / num_files)
    line_chunks = np.round(nlines / num_files)
    print('lines per file:', line_chunks)

    line_cnt = 0
    file_num = 0

    for nt in range(nlines):
        if line_cnt % line_chunks == 0:
            file_num += 1
            if file_num > num_files:  # if file num exceeds max no. of files, append to existing files
                file_num = 1
                for j in range(nt, nlines):
                    with open(outpath+'seq_'+str(file_num), 'a') as f:
                        f.write(sequence_list[j]+'\n')
                    file_num += 1
                break

        with open(outpath+'seq_'+str(file_num), 'a') as f:
            f.write(sequence_list[nt]+'\n')
        
        if line_cnt % line_chunks == line_chunks:
            break
        
        line_cnt += 1
        if line_cnt % line_chunks == 0:
            line_cnt = 0



def seqs_to_files(split_lines):
    # remove existing directory to prevent accidental inclusion of 
    # sequences from previous runs.
    outpath = 'output/sequences/'
    outdir = os.listdir(outpath)

    for ffile in outdir:
        os.remove(outpath + ffile)

    # write n sequences to n files
    seq_num = 1
    for elem in split_lines:
        with open('output/sequences/seq_'+str(seq_num), 'w') as f:
            f.write(str(elem))
        seq_num += 1

def main(fasta_file, num_files):
    seq_list = split_sequences(fasta_file)
    split_to_lines(seq_list, num_files)
    #seqs_to_files(split_lines)

if __name__ == '__main__':
    ffile = sys.argv[1]
    nfiles = 10
    print('Using FASTA file: ', ffile)
    main(ffile, nfiles)
