# -*- coding: utf-8 -*-

"""
@author: Billy
@Date: 2020-02-13
@E-mail: liangbilin0324@163.com
@Description: The script is used for extracting nucleotide or amino acid sequences, with fasta format, by sequence name.
@Usage:
    python -h
    python3 extract_fasta_by_ID.py -f sequences.fasta -i idlist.txt -out output.fasta -m relaxed
"""
import argparse
import time


def read_config():
    parser = argparse.ArgumentParser(description='The script is used for extracting nucleotide or amino acid sequences, with fasta format, by sequence name.')
    parser.add_argument('--fasta', '-f', required=True, help='The argument represent the file name, which keep nucleotide or amino acid sequences with fasta.')
    parser.add_argument('--idlist', '-i', required=True, help='The file include sequence name that need to extract. Save one sequence name per line. ')
    parser.add_argument('--out', '-o', required=False, default='out.fasta', help='The output file name, the default is out.fasta.')
    parser.add_argument('--model', '-m', default='rigorous', choices=['rigorous', 'relaxed'], help='The extract model, default value is rigorous. rigorous model means the name in id list must be same with fasta file. relaxed model means the name in id list maybe part of fasta file name, such as "abc" vs. "1abcd".')
    arg = parser.parse_args()
    fa_ = arg.fasta
    id_ = arg.idlist
    out_ = arg.out
    model_ = arg.model
    return fa_, id_, out_, model_


def extract_rigorous(fa_, id_, out_):
    dict_ = {}
    with open(fa_, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                name_ = line[1:].strip()
                dict_[name_] = ''
            else:
                dict_[name_] += line.replace('\n', '')
    outfile = open(out_, 'w')
    outfile_err = open('outERR.txt', 'w')
    outfile_err.write('Failed to extract:' + '\n')
    with open(id_, 'r') as f:
        for line in f:
            line = line.strip()
            if line in dict_:
                outfile.write('>' + line + '\n')
                outfile.write(dict_[line] + '\n')
            else:
                outfile_err.write('>' + line + '\n')
    outfile.close()
    outfile_err.close()


def extract_relaxed(fa_, id_, out_):
    dict_ = {}
    with open(fa_, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                name_ = line[1:]
                dict_[name_] = ''
            else:
                dict_[name_] += line.replace('\n', '')
    outfile = open(out_, 'w')
    outfile_err = open('outERR.txt', 'w')
    outfile_err.write('Failed to extract:' + '\n')
    ex_name_list = list()
    with open(id_, 'r') as f:
        for line in f:
            line = line.strip()
            n = 0
            for key_ in dict_.keys():
                if line in key_:
                    ex_name_list.append(key_)
                    n = n + 1
            if n == 0:
                outfile_err.write('>' + line + '\n')
    new_name_list = list(set(ex_name_list))
    for na in new_name_list:
        outfile.write('>' + na + '\n')
        outfile.write(dict_[na] + '\n')
    outfile.close()
    outfile_err.close()


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ' starting running...')
    fa_, id_, out_, model_ = read_config()
    if model_ == 'rigorous':
        extract_rigorous(fa_, id_, out_)
    if model_ == 'relaxed':
        extract_relaxed(fa_, id_, out_)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ' program has finished.')
