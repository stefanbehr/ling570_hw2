#!/usr/bin/env python2.7

# Stefan Behr
# LING 570
# Homework 2, part a
# 10/08/2012

if __name__ == "__main__":
    import sys
    from os import path
    from glob import glob
    import re

    from hw2lib import *

    try:
        corpus_dir = path.expanduser(path.sys.argv[1])
    except IndexError:
        sys.exit("Missing input directory argument.")

    corpus = []

    for pathname in glob(path.join(corpus_dir, '*')):
        corpus.extend(get_token_tag_pairs(get_file_data(pathname)))

    token_tag_frequencies = get_frequencies('/'.join(pair) for pair in corpus)

    try:
        print_top_n(token_tag_frequencies, 20)
    except IOError:
        sys.exit(0)
