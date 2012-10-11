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
    typs = []
    tags = []

    tags.append(EBOS_TAG)

    corpus_dir = path.expanduser(corpus_dir)

    for pathname in glob(path.join(corpus_dir, '*')):
        for token, tag in get_token_tag_pairs(get_file_data(pathname)):
            corpus.append((token, tag))
            typs.append(token)
            tags.append(tag)
            if tag == EOS_PUNC:
                tags.append(EBOS_TAG)

    # part 2b, item 1
    tag_bigrams = get_tag_bigrams(tags)
    tag_bigram_frequencies = get_frequencies(' '.join(bigram) for bigram in tag_bigrams)

    print_top(tag_bigram_frequencies, 20)

    # part 2b, item 2
    
    # list, ordered in descending order of frequency
    tag_unigram_frequencies = get_frequencies(tags)
    tagset_descending = [tag for tag, freq in get_top(tag_unigram_frequencies)]

    t_matrix = []
    t_matrix.append([''] + tagset_descending)
    
    for row_tag in tagset_descending:
        row = [row_tag]
        row_tag_bigram_total = sum(freq for bigram, freq in tag_bigram_frequencies.items()
                                   if row_tag == bigram.split(' ')[0])
        for col_tag in tagset_descending:
            row_col_bigram_total = tag_bigram_frequencies.get(' '.join((row_tag, col_tag)), 0)
            t_prob = float(row_col_bigram_total)/row_tag_bigram_total
            t_prob = '-Inf' if t_prob == 0 else log(t_prob, 2)
            row.append(t_prob)
        t_matrix.append(row)

    print
    pprint_matrix(t_matrix, rows=11, cols=11) # 11 x 11 matrix due to labels for row/columns

    # part 2b, item 3
    tagset_alphabeta = sorted(tag for tag in tagset_descending if tag is not EBOS_TAG)
    typeset_descending = [typ for typ, freq in get_top(get_frequencies(typs))]
    type_tag_frequencies = get_frequencies(corpus)

    # we don't want the '<s>' tag in our emission matrix, since it
    # has no corresponding type
    del tag_unigram_frequencies[EBOS_TAG]

    e_matrix = []
    e_matrix.append([''] + tagset_alphabeta)

    for typ in typeset_descending:
        row = [typ]
        for tag in tagset_alphabeta:
            type_tag_frequency = type_tag_frequencies.get((typ, tag), 0)
            tag_frequency = tag_unigram_frequencies[tag]
            e_prob = float(type_tag_frequency)/tag_frequency
            e_prob = "-Inf" if e_prob == 0 else log(e_prob, 2)
            row.append(e_prob)
        e_matrix.append(row)

    print
    pprint_matrix(e_matrix, rows=21) # 21 x n matrix due to labels for rows/columns

    with open('test.out', 'w') as t_out:
        t_out.write('\n'.join(str(pair)for pair in get_top(tag_unigram_frequencies)))
