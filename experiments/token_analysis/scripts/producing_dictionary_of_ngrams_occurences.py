#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: March 2023
- description: Producing dictionaries of n-grams occurrences
- input: list from another file (called in the preamble)
- output: Python file
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: Python file with the produced dictionary
"""

import sys
from results_lists_and_dictionaries import gt as liste
from results_lists_and_dictionaries import gt_2_grams #as liste
from results_lists_and_dictionaries import gt_3_grams #as liste
from results_lists_and_dictionaries import gt_4_grams #as liste
from results_lists_and_dictionaries import war #as liste
from results_lists_and_dictionaries import war_2_grams #as liste
from results_lists_and_dictionaries import war_3_grams #as liste
from results_lists_and_dictionaries import war_4_grams #as liste
from results_lists_and_dictionaries import other #as liste
from results_lists_and_dictionaries import other_2_grams #as liste
from results_lists_and_dictionaries import other_3_grams #as liste
from results_lists_and_dictionaries import other_4_grams #as liste

def counting(words): 
    """ Counting the number of occurrences of each element in the list
    
    :param words: Content to count
    :type words: str
    :returns: frequency list
    :rtype: dict
    """
    calculation = {}
    for word in words:
        if word not in calculation:
            calculation[word] = words.count(word)
    return calculation

#Production of a dictionary created through the counting function
#The dictionary will be sorted by value, from the biggest to the smallest
with open(sys.argv[1], "w") as file_out:
    print(f'Writing to {sys.argv[1]}')
    file_out.write("dictionary = " + str(dict(sorted(counting(liste).items(), key=lambda item: item[1], reverse=True))))