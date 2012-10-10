#!/usr/bin/env python2.7

# Stefan Behr
# LING 570
# Homework 2, part b
# 10/08/2012

if __name__ == "__main__":
    import re, sys
    from os import path
    from glob import glob
    from math import log
    from hw2lib import *

    try:
        corpus_dir = path.sys.argv[1]
    except IndexError:
        sys.exit("Missing input directory argument.")

    corpus = []
    tags = []
    tags.append(EBOS_TAG)

    corpus_dir = path.expanduser(corpus_dir)

    for pathname in glob(path.join(corpus_dir, '*')):
        for token, tag in get_token_tag_pairs(get_file_data(pathname)):
            corpus.append((token, tag))
            tags.append(tag)
            if tag == EOS_PUNC:
                tags.append(EBOS_TAG)

    # part 2b, item 1
    tag_bigrams = get_tag_bigrams(tags)
    tag_bigram_frequencies = get_frequencies(' '.join(bigram) for bigram in tag_bigrams)
    print "(1) List the 20 most frequent tag-tag sequences." + "\n"
    print_top_n(tag_bigram_frequencies, 20)

    # part 2b, item 2
    tag_frequencies = get_frequencies(tags)
    tag_frequencies_top_ten = get_top_n(tag_frequencies, 10)
    top_ten_tags = [tag for tag, freq in tag_frequencies_top_ten]
    tag_frequencies_top_ten = {tag: freq for tag, freq in tag_frequencies_top_ten}

    t_matrix = []
    t_matrix.append(['']+top_ten_tags)
    
    for row_tag in top_ten_tags:
        row = [row_tag]
        for col_tag in top_ten_tags:
            t_prob = float(tag_bigram_frequencies.get(' '.join((row_tag, col_tag)), 0)) / \
                sum(freq for bigram, freq in tag_bigram_frequencies.items()
                        if row_tag == bigram.split(' ')[0])
            t_prob = '-Inf' if t_prob == 0 else log(t_prob, 2)
            row.append(t_prob)
        t_matrix.append(row)

    print "\n" + \
        "(2) Produce a Markov transition matrix for the 10 most frequently occurring tags." + \
        "\n"

    pprint_matrix(t_matrix)

    print "\n" + \
        "(3) Produce an emission probability matrix for the 20 most frequently occurring types and their associated tags." + \
        "\n"
