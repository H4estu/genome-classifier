#!/usr/bin/env/python3

import os

def delete_old_features(header_path):
    ''' prevent old feature files from cluttering up the new ones.'''
    feature_path = header_path + 'features/'
    if not 'features' in os.listdir(header_path):
        os.mkdir(feature_path)
    else:
        feature_files = os.listdir(feature_path)
        print(feature_files)

        # clear features for clean run                                                              
        print('Removing files in', feature_path)
        for ffile in feature_files:
            os.remove(feature_path + ffile)


def delete_old_sequences(header_path):
    ''' prevent old sequence files from cluttering up the new ones.'''
    sequence_path = header_path + 'sequences/'
    if not 'sequences' in os.listdir(header_path):
        os.mkdir(sequence_path)
    else:
        sequence_files = os.listdir(sequence_path)
        print(sequence_files)

        # clear features for clean run                                                              
        print('Removing files in', sequence_path)
        for sfile in sequence_files:
            os.remove(sequence_path + sfile)


def main():
    path_header = 'output/'
    delete_old_sequences(path_header)
    delete_old_features(path_header)

if __name__ == '__main__':
    main()
