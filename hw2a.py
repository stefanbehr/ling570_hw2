#!/usr/bin/env python2.7
# hw2lib module

# Stefan Behr
# LING 570
# Homework 2
# 10/08/2012

if __name__ == "__main__":
    import sys
    from os import path
    from glob import glob
    import re

    from hw2lib import *

    EBOS_TAG = '<s>' # end/beginning of sentence tag
    EOS_PUNC = '.' # tag associated with sentence-terminal punctuation

    try:
        corpus_dir = path.sys.argv[1]
    except IndexError:
        sys.exit("Missing input directory argument.")

    corpus = []
    tags = []
    tags.append(EBOS_TAG)

    corpus_dir = path.expanduser(corpus_dir)

    for pathname in glob(path.join(corpus_dir, '*')):
        for pair in get_token_tag_pairs(get_file_data(pathname)):
            tag = pair[1]
            corpus.append(pair)
            tags.append(tag)
            if tag == EOS_PUNC:
                tags.append(EBOS_TAG)

    token_tag_frequencies = get_frequencies('/'.join(pair) for pair in corpus)

    try:
        print_top_n(token_tag_frequencies, 20)
    except IOError:
        sys.exit(0)
