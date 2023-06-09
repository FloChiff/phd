#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: March 2023
- description: Creating several lists of tokens
- output: Python files
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: file with the lists of unique and common tokens
"""

"""

#Least popular tokens

import sys
from results_lists_and_dictionaries import war_2_grams_only_1
from results_lists_and_dictionaries import war_3_grams_only_1
from results_lists_and_dictionaries import war_4_grams_only_1
from results_lists_and_dictionaries import other_2_grams_only_1
from results_lists_and_dictionaries import other_3_grams_only_1
from results_lists_and_dictionaries import other_4_grams_only_1

#The difference() method will retrieve all the words found in the first argument but not in the second one 
#The intersection() method will retrieve all the common words between both lists
#The set() method is there to transform the list into an ensemble with unique token
war_unique_2grams = set(war_2_grams_only_1).difference(set(other_2_grams_only_1))
other_unique_2grams = set(other_2_grams_only_1).difference(set(war_2_grams_only_1))
common_2grams = set(war_2_grams_only_1).intersection(set(other_2_grams_only_1))
war_unique_3grams = set(war_3_grams_only_1).difference(set(other_3_grams_only_1))
other_unique_3grams = set(other_3_grams_only_1).difference(set(war_3_grams_only_1))
common_3grams = set(war_3_grams_only_1).intersection(set(other_3_grams_only_1))
war_unique_4grams = set(war_4_grams_only_1).difference(set(other_4_grams_only_1))
other_unique_4grams = set(other_4_grams_only_1).difference(set(war_4_grams_only_1))
common_4grams = set(war_4_grams_only_1).intersection(set(other_4_grams_only_1))
"""

#Most popular tokens

import sys
from results_lists_and_dictionaries import war_2_grams_11_and_more
from results_lists_and_dictionaries import war_3_grams_11_and_more
from results_lists_and_dictionaries import war_4_grams_11_and_more
from results_lists_and_dictionaries import other_2_grams_11_and_more
from results_lists_and_dictionaries import other_3_grams_11_and_more
from results_lists_and_dictionaries import other_4_grams_11_and_more

#The difference() method will retrieve all the words found in the first argument but not in the second one 
#The intersection() method will retrieve all the common words between both lists
#The set() method is there to transform the list into an ensemble with unique token
war_unique_2grams = set(war_2_grams_11_and_more).difference(set(other_2_grams_11_and_more))
other_unique_2grams = set(other_2_grams_11_and_more).difference(set(war_2_grams_11_and_more))
common_2grams = set(war_2_grams_11_and_more).intersection(set(other_2_grams_11_and_more))
war_unique_3grams = set(war_3_grams_11_and_more).difference(set(other_3_grams_11_and_more))
other_unique_3grams = set(other_3_grams_11_and_more).difference(set(war_3_grams_11_and_more))
common_3grams = set(war_3_grams_11_and_more).intersection(set(other_3_grams_11_and_more))
war_unique_4grams = set(war_4_grams_11_and_more).difference(set(other_4_grams_11_and_more))
other_unique_4grams = set(other_4_grams_11_and_more).difference(set(war_4_grams_11_and_more))
common_4grams = set(war_4_grams_11_and_more).intersection(set(other_4_grams_11_and_more))

with open(sys.argv[1],"w", encoding='UTF-8') as file_out:
    print("writing to " + sys.argv[1])
    file_out.write("war_unique_2grams = " + str(sorted(war_unique_2grams)) + "\n\n")
    file_out.write("other_unique_2grams = " + str(sorted(other_unique_2grams)) + "\n\n")
    file_out.write("common_2grams = " + str(sorted(common_2grams)) + "\n\n")
    file_out.write("war_unique_3grams = " + str(sorted(war_unique_3grams)) + "\n\n")
    file_out.write("other_unique_3grams = " + str(sorted(other_unique_3grams)) + "\n\n")
    file_out.write("common_3grams = " + str(sorted(common_3grams)) + "\n\n")
    file_out.write("war_unique_4grams = " + str(sorted(war_unique_4grams)) + "\n\n")
    file_out.write("other_unique_4grams = " + str(sorted(other_unique_4grams)) + "\n\n")
    file_out.write("common_4grams = " + str(sorted(common_4grams)) + "\n\n")