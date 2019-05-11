#!/usr/bin/env/python3
# compute_features.py
#  
# Input: File of sequence data.
# Output: Computed feature of interest
#
# Last edit: 22 May 2018
#            31 May 2018 -> Compute %GC, %A, start codon features.
#             2 May 2018 -> Write features to file.

import os
import re
import sys
import numpy as np

def compute_features(sequence_file):
    '''Feature options.  These will be the columns in the table.
         feat1 = "GC_content"
         feat2 = "percent_A"
         feat3 = "AUG"  # start_codon
    '''
    outpath = 'output/features/'
    outdir = os.listdir(outpath)
    
    # initialize counters
    tally_GC = 0    # GC content
#    tally_G  = 0
#    tally_C  = 0 
    tally_A  = 0    # % A
#    tally_AT = 0
#    tally_T  = 0
    tally_SC = 0    # Total start codons
    total = 0.  # sequence length
    
    cnt = 0
    with open(sequence_file, 'r') as sf:
        seq = sf.readlines()
        for line in seq: 
            line = line.strip('\n')
            print ('Line',cnt)
            i = 0  # incrementer for codon stepping logic.
            for nt in line:  # break sequence into single nucleotides
                if nt == 'C' or nt == 'G':
                    tally_GC += 1
#                if nt == 'C':
#                    tally_C += 1
#                if nt == 'G':
#                    tally_G += 1
                if nt == 'A':
                    tally_A += 1
#                if nt == 'T':
#                    tally_T += 1
                # break sequence into codon triplets and see which ones
                # are equal to AUG DNA complement.
                codon = str(line[i:i+3])
                if codon == 'ATG':  # Methionine most common start codon in eukaryotes.
                    tally_SC += 1
                i += 1
                total += 1
            cnt += 1

            percent_GC = round(tally_GC/total,4)
            # percent_G = round(tally_G/total,4)
            # percent_C = round(tally_G/total,4)
            percent_A = round(tally_A/total,4)
            # percent_T = round(tally_T/total,4)
#            percent_AT = tally_AT/total
        
            print('Total Gs and Cs in sequence:', tally_GC)
            print(r'% GC: {0:.3}'.format(percent_GC*100))
            print('Total As in sequence:', tally_A)
#            print('Total As and Ts in sequence:', tally_AT)
#            print('% AT: {0:.3}'.format(percent_AT*100))
            print('Total start codons in sequence:', tally_SC)

            # grab task ID to attach proper sequence ID
            seq_num = int(re.search(r'\d+',sequence_file).group())
            seq_id  = 'Seq_' + str(seq_num) + '.' +str(cnt)

            # combine features into an entry and write to file
            entry = np.array([seq_id, percent_GC, percent_A, tally_SC])    
            # entry = np.array([seq_id, 
            #                   percent_G, percent_C, 
            #                   percent_A, percent_T, 
            #                   tally_SC])    
            
            # write feature to output file
            with open(outpath+'feature_'+str(seq_id), 'a') as f:
                f.write(str(entry).strip('[]')+'\n')
    
def main(sequence_file):
    compute_features(sequence_file)

if __name__ == '__main__':
    sfile = sys.argv[1]

    print('Using Sequence file: ', sfile)
    main(sfile)
