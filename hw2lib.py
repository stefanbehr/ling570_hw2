#!/usr/bin/env python2.7
# hw2lib module

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
    return [(token.lower(), re.sub(r'\|.+', '', tag)) for token, tag in pairs]

def get_tag_bigrams(taglist):
    """Given a list of tags, return a list of tuples where each \
tuple contains a tag bigram."""
    return zip(taglist[:-1], taglist[1:])

def get_frequencies(data_list):
    """Takes a list of items and returns a dictionary representing \
a frequency list of those items."""
    result = {}
    for item in data_list:
        result[item] = result.get(item, 0) + 1
    return result

def get_top_n(frequencies, n):
    """Given a dictionary with items as keys and frequencies as values, \
return the top n item-frequency pairs."""
    return sorted_by_val_and_key(frequencies, val_reverse=True)[:n]

def print_top_n(frequencies, n):
    """Given a dictionary of item keys and frequency values, prints \
the n most frequent items with their frequencies, tab-separated."""
    top_n = get_top_n(frequencies, n)
    col_width = max_str_len([str(item) for item, freq in top_n])
    print '\n'.join("{0:{1:d}s}\t{2:d}".format(item, col_width, freq) for item, freq in top_n)

def sorted_by_val_and_key(d, key_reverse=False, val_reverse=False):
    """Given a dictionary, return a list of tuples containing \
the dictionary's keys and values, sorted first by values and \
then by keys."""
    reverse_map = {}
    result = []
    for key, val in d.items():
        reverse_map[val] = reverse_map.get(val, ()) + (key,)
    for val, key_list in sorted(reverse_map.items(), reverse=val_reverse):
        for key in sorted(key_list, reverse=key_reverse):
            result.append((key, val))
    return result

def max_str_len(alos):
    """Given a lost strings, finds the length of the longest one."""
    return max(map(len, alos))

EBOS_TAG = '<s>' # end/beginning of sentence tag
EOS_PUNC = '.' # tag associated with sentence-terminal punctuation
