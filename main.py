#!/usr/bin/env python

# Stefan Behr
# LING 570
# Homework 2
# 10/08/2012

def file_data(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    import sys
    from os import path
    from glob import glob

    typetags = []

    try:
        corpus_dir = path.sys.argv[1]
    except IndexError:
        sys.exit("Missing input directory argument.")
    
    corpus_dir = path.expanduser(corpus_dir)

    for pathname in glob(path.join(corpus_dir, '*')):
        typetags.append(
