#!/usr/bin/env python2.7
# hw2lib module

# Stefan Behr
# LING 570
# Homework 2
# 10/08/2012

def get_file_data(path):
    """Takes a filepath and returns a string containing the contents of 
the file at the path."""
    with open(path) as f:
        return f.read()

def get_token_tag_pairs(data):
    """Takes a string argument containing the contents of a file 
and returns a list of tuples containing only the token-tag pairs present 
in the file data which are of the form <token>/<TAG>."""
    import re
    pairs = re.findall(r'(\S+)/(\S+)', data)
    return [(token.lower(), re.sub(r'\|.+', '', tag)) for token, tag in pairs]

def get_tag_bigrams(taglist):
    """Given a list of tags, return a list of tuples where each 
tuple contains a tag bigram."""
    return zip(taglist[:-1], taglist[1:])

def get_frequencies(data_list):
    """Takes a list of items and returns a dictionary representing 
a frequency list of those items."""
    result = {}
    for item in data_list:
        result[item] = result.get(item, 0) + 1
    return result

def get_top(frequencies, n=0):
    """Given a dictionary with items as keys and frequencies as values, 
return the top n item-frequency pairs."""
    result = sorted_by_val_and_key(frequencies, val_reverse=True)
    if n:
        result = result[:n]
    return result

def print_top(frequencies, n=0):
    """Given a dictionary of item keys and frequency values, prints 
the n most frequent items with their frequencies, tab-separated."""
    top_n = get_top(frequencies, n)
    col_width = max_str_len([str(item) for item, freq in top_n])
    print '\n'.join("{0:{1:d}s}\t{2:d}".format(item, col_width, freq) for item, freq in top_n)

def sorted_by_val_and_key(d, key_reverse=False, val_reverse=False):
    """Given a dictionary, return a list of tuples containing 
the dictionary's keys and values, sorted first by values and 
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

def pprint_matrix(matrix, rows=0, cols=0):
    """Pretty print a matrix, passed to the function in the following form:

    [['', col1_label, ..., colm_label],
     [row1_label, cell_11, cell_12, ..., cell_1m],
     ...
     [rown_label, cell_n1, cell_n2, ..., cell_nm]]

     Print only the first <rows> rows and <cols> cols either is > 0,
     otherwise print the whole matrix.

     """
    import types
    if rows: #truncate rows
        matrix = matrix[:rows]
    if cols: #truncate columns
        matrix = [row[:cols] for row in matrix]
    matrix = [map((lambda cell: "{:.6f}".format(cell)
                   if type(cell) == types.FloatType else str(cell)), row)
              for row in matrix]
    # find width of widest element in matrix, set column width to that
    col_width = max(
        map(max,
            map((lambda lst: map(len, lst)),
                matrix)))
    for row in matrix:
        print ' '.join("{0:{1}s}".format(cell, col_width) for cell in row)

EBOS_TAG = '<s>' # end/beginning of sentence tag
EOS_PUNC = '.' # tag associated with sentence-terminal punctuation
