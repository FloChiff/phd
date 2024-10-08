#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: February 2024
- description: Producing dictionaries of n-grams occurrences
- input: list from another file (called in the preamble)
- output: Python file
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: Python file with the produced dictionary
"""

import sys
from results_lists_and_dictionaries import czech 
from results_lists_and_dictionaries import czech_2_grams 
from results_lists_and_dictionaries import czech_3_grams 
from results_lists_and_dictionaries import czech_4_grams
from results_lists_and_dictionaries import danish 
from results_lists_and_dictionaries import danish_2_grams 
from results_lists_and_dictionaries import danish_3_grams 
from results_lists_and_dictionaries import danish_4_grams 
from results_lists_and_dictionaries import polish 
from results_lists_and_dictionaries import polish_2_grams 
from results_lists_and_dictionaries import polish_3_grams 
from results_lists_and_dictionaries import polish_4_grams 
from results_lists_and_dictionaries import english 
from results_lists_and_dictionaries import english_2_grams 
from results_lists_and_dictionaries import english_3_grams 
from results_lists_and_dictionaries import english_4_grams 
from results_lists_and_dictionaries import german 
from results_lists_and_dictionaries import german_2_grams 
from results_lists_and_dictionaries import german_3_grams 
from results_lists_and_dictionaries import german_4_grams 
from results_lists_and_dictionaries import slovak 
from results_lists_and_dictionaries import slovak_2_grams 
from results_lists_and_dictionaries import slovak_3_grams 
from results_lists_and_dictionaries import slovak_4_grams 
from results_lists_and_dictionaries import hungarian 
from results_lists_and_dictionaries import hungarian_2_grams 
from results_lists_and_dictionaries import hungarian_3_grams 
from results_lists_and_dictionaries import hungarian_4_grams 
from results_lists_and_dictionaries import ehri 
from results_lists_and_dictionaries import ehri_2_grams 
from results_lists_and_dictionaries import ehri_3_grams 
from results_lists_and_dictionaries import ehri_4_grams 

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
    """
    file_out.write("czech = " + str(dict(sorted(counting(czech).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("czech_2_grams = " + str(dict(sorted(counting(czech_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("czech_3_grams = " + str(dict(sorted(counting(czech_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("czech_4_grams = " + str(dict(sorted(counting(czech_4_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("danish = " + str(dict(sorted(counting(danish).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("danish_2_grams = " + str(dict(sorted(counting(danish_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("danish_3_grams = " + str(dict(sorted(counting(danish_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("danish_4_grams = " + str(dict(sorted(counting(danish_4_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("polish = " + str(dict(sorted(counting(polish).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("polish_2_grams = " + str(dict(sorted(counting(polish_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("polish_3_grams = " + str(dict(sorted(counting(polish_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("polish_4_grams = " + str(dict(sorted(counting(polish_4_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("english = " + str(dict(sorted(counting(english).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("english_2_grams = " + str(dict(sorted(counting(english_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("english_3_grams = " + str(dict(sorted(counting(english_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("english_4_grams = " + str(dict(sorted(counting(english_4_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("german = " + str(dict(sorted(counting(german).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("german_2_grams = " + str(dict(sorted(counting(german_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("german_3_grams = " + str(dict(sorted(counting(german_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("german_4_grams = " + str(dict(sorted(counting(german_4_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("slovak = " + str(dict(sorted(counting(slovak).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("slovak_2_grams = " + str(dict(sorted(counting(slovak_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("slovak_3_grams = " + str(dict(sorted(counting(slovak_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("slovak_4_grams = " + str(dict(sorted(counting(slovak_4_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("hungarian = " + str(dict(sorted(counting(hungarian).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("hungarian_2_grams = " + str(dict(sorted(counting(hungarian_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("hungarian_3_grams = " + str(dict(sorted(counting(hungarian_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("hungarian_4_grams = " + str(dict(sorted(counting(hungarian_4_grams).items(), key=lambda item: item[1], reverse=True))))
"""
    file_out.write("ehri = " + str(dict(sorted(counting(ehri).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("ehri_2_grams = " + str(dict(sorted(counting(ehri_2_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("ehri_3_grams = " + str(dict(sorted(counting(ehri_3_grams).items(), key=lambda item: item[1], reverse=True))))
    file_out.write("ehri_4_grams = " + str(dict(sorted(counting(ehri_4_grams).items(), key=lambda item: item[1], reverse=True))))
