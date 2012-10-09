#!/usr/bin/env python

# Stefan Behr
# LING 570
# Homework 2
# 10/08/2012

def get_file_data(path):
    """Takes a filepath and returns a string containing the contents of \
the file at the path."""
    with open(path) as f:
        return f.read()

def get_token_tag_pairs(data):
    """Takes a string argument containing the contents of a file \
and returns a list of tuples containing only the token-tag pairs present \
in the file data which are of the form <token>/<TAG>."""
    import re
    pairs = re.findall(r'(\S+)/(\S+)', data)
    return [(token.lower(), tag) for token, tag in pairs]

def print_top_n(frequencies, n):
    """Given a dictionary of item keys and frequency values, prints \
the n most frequent items with their frequencies, tab-separated."""
    freq_ranking = [(item, freq) for freq, item in 
                    sorted(((freq, item) for item, freq in frequencies.items()), reverse=True)]
    top_n = freq_ranking[:n] if len(freq_ranking) > n else freq_ranking
    col_width = longest_string([str(item) for item, freq in top_n])
    print '\n'.join("{0:{1:d}s}\t{2:d}".format(item, col_width, freq) for item, freq in top_n)

def longest_string(alos):
    """Given a lost strings, finds the length of the longest one."""
    return max(map(len, alos))

if __name__ == "__main__":
    import sys
    from os import path
    from glob import glob
    import re

    token_tag_frequencies = {}

    try:
        corpus_dir = path.sys.argv[1]
    except IndexError:
        sys.exit("Missing input directory argument.")
    
    corpus_dir = path.expanduser(corpus_dir)

    for pathname in glob(path.join(corpus_dir, '*')):
        for pair in get_token_tag_pairs(get_file_data(pathname)):
            pair_string = '/'.join(pair)
            token_tag_frequencies[pair_string] = 1 + token_tag_frequencies.get(pair_string, 0)
    try:
        print_top_n(token_tag_frequencies, 30)
    except IOError:
        sys.exit(0)
