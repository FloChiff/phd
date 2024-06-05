#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: February 2024
- description: Creating several lists of tokens
- output: Python files
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: file with the lists of unique and common tokens
"""

import sys
from results_lists_and_dictionaries import polish_2_grams_only_1
from results_lists_and_dictionaries import polish_3_grams_only_1
from results_lists_and_dictionaries import polish_4_grams_only_1
from results_lists_and_dictionaries import slovak_2_grams_only_1
from results_lists_and_dictionaries import slovak_3_grams_only_1
from results_lists_and_dictionaries import slovak_4_grams_only_1
from results_lists_and_dictionaries import english_2_grams_only_1
from results_lists_and_dictionaries import english_3_grams_only_1
from results_lists_and_dictionaries import english_4_grams_only_1
from results_lists_and_dictionaries import hungarian_2_grams_only_1
from results_lists_and_dictionaries import hungarian_3_grams_only_1
from results_lists_and_dictionaries import hungarian_4_grams_only_1
from results_lists_and_dictionaries import danish_2_grams_only_1
from results_lists_and_dictionaries import danish_3_grams_only_1
from results_lists_and_dictionaries import danish_4_grams_only_1
from results_lists_and_dictionaries import german_2_grams_only_1
from results_lists_and_dictionaries import german_3_grams_only_1
from results_lists_and_dictionaries import german_4_grams_only_1
from results_lists_and_dictionaries import czech_2_grams_only_1
from results_lists_and_dictionaries import czech_3_grams_only_1
from results_lists_and_dictionaries import czech_4_grams_only_1


#The difference() method will retrieve all the words found in the first argument but not in the second one 
#The intersection() method will retrieve all the common words between both lists
#The set() method is there to transform the list into an ensemble with unique token
common_2grams = set(hungarian_2_grams_only_1).intersection(set(slovak_2_grams_only_1)).intersection(set(polish_2_grams_only_1)).intersection(set(german_2_grams_only_1)).intersection(set(english_2_grams_only_1)).intersection(set(danish_2_grams_only_1)).intersection(set(czech_2_grams_only_1))
common_3grams = set(hungarian_3_grams_only_1).intersection(set(slovak_3_grams_only_1)).intersection(set(polish_3_grams_only_1)).intersection(set(german_3_grams_only_1)).intersection(set(english_3_grams_only_1)).intersection(set(danish_3_grams_only_1)).intersection(set(czech_3_grams_only_1))
common_4grams = set(hungarian_4_grams_only_1).intersection(set(slovak_4_grams_only_1)).intersection(set(polish_4_grams_only_1)).intersection(set(german_4_grams_only_1)).intersection(set(english_4_grams_only_1)).intersection(set(danish_4_grams_only_1)).intersection(set(czech_4_grams_only_1))


hungarian_slovak_2grams = set(hungarian_2_grams_only_1).intersection(set(slovak_2_grams_only_1))
hungarian_slovak_3grams = set(hungarian_3_grams_only_1).intersection(set(slovak_3_grams_only_1))
hungarian_slovak_4grams = set(hungarian_4_grams_only_1).intersection(set(slovak_4_grams_only_1))
hungarian_english_2grams = set(hungarian_2_grams_only_1).intersection(set(english_2_grams_only_1))
hungarian_english_3grams = set(hungarian_3_grams_only_1).intersection(set(english_3_grams_only_1))
hungarian_english_4grams = set(hungarian_4_grams_only_1).intersection(set(english_4_grams_only_1))
hungarian_polish_2grams = set(hungarian_2_grams_only_1).intersection(set(polish_2_grams_only_1))
hungarian_polish_3grams = set(hungarian_3_grams_only_1).intersection(set(polish_3_grams_only_1))
hungarian_polish_4grams = set(hungarian_4_grams_only_1).intersection(set(polish_4_grams_only_1))
hungarian_danish_2grams = set(hungarian_2_grams_only_1).intersection(set(danish_2_grams_only_1))
hungarian_danish_3grams = set(hungarian_3_grams_only_1).intersection(set(danish_3_grams_only_1))
hungarian_danish_4grams = set(hungarian_4_grams_only_1).intersection(set(danish_4_grams_only_1))
hungarian_german_2grams = set(hungarian_2_grams_only_1).intersection(set(german_2_grams_only_1))
hungarian_german_3grams = set(hungarian_3_grams_only_1).intersection(set(german_3_grams_only_1))
hungarian_german_4grams = set(hungarian_4_grams_only_1).intersection(set(german_4_grams_only_1))
hungarian_czech_2grams = set(hungarian_2_grams_only_1).intersection(set(czech_2_grams_only_1))
hungarian_czech_3grams = set(hungarian_3_grams_only_1).intersection(set(czech_3_grams_only_1))
hungarian_czech_4grams = set(hungarian_4_grams_only_1).intersection(set(czech_4_grams_only_1))

english_slovak_2grams = set(english_2_grams_only_1).intersection(set(slovak_2_grams_only_1))
english_slovak_3grams = set(english_3_grams_only_1).intersection(set(slovak_3_grams_only_1))
english_slovak_4grams = set(english_4_grams_only_1).intersection(set(slovak_4_grams_only_1))
english_polish_2grams = set(english_2_grams_only_1).intersection(set(polish_2_grams_only_1))
english_polish_3grams = set(english_3_grams_only_1).intersection(set(polish_3_grams_only_1))
english_polish_4grams = set(english_4_grams_only_1).intersection(set(polish_4_grams_only_1))
english_danish_2grams = set(english_2_grams_only_1).intersection(set(danish_2_grams_only_1))
english_danish_3grams = set(english_3_grams_only_1).intersection(set(danish_3_grams_only_1))
english_danish_4grams = set(english_4_grams_only_1).intersection(set(danish_4_grams_only_1))
english_german_2grams = set(english_2_grams_only_1).intersection(set(german_2_grams_only_1))
english_german_3grams = set(english_3_grams_only_1).intersection(set(german_3_grams_only_1))
english_german_4grams = set(english_4_grams_only_1).intersection(set(german_4_grams_only_1))
english_czech_2grams = set(english_2_grams_only_1).intersection(set(czech_2_grams_only_1))
english_czech_3grams = set(english_3_grams_only_1).intersection(set(czech_3_grams_only_1))
english_czech_4grams = set(english_4_grams_only_1).intersection(set(czech_4_grams_only_1))

slovak_polish_2grams = set(slovak_2_grams_only_1).intersection(set(polish_2_grams_only_1))
slovak_polish_3grams = set(slovak_3_grams_only_1).intersection(set(polish_3_grams_only_1))
slovak_polish_4grams = set(slovak_4_grams_only_1).intersection(set(polish_4_grams_only_1))
slovak_danish_2grams = set(slovak_2_grams_only_1).intersection(set(danish_2_grams_only_1))
slovak_danish_3grams = set(slovak_3_grams_only_1).intersection(set(danish_3_grams_only_1))
slovak_danish_4grams = set(slovak_4_grams_only_1).intersection(set(danish_4_grams_only_1))
slovak_german_2grams = set(slovak_2_grams_only_1).intersection(set(german_2_grams_only_1))
slovak_german_3grams = set(slovak_3_grams_only_1).intersection(set(german_3_grams_only_1))
slovak_german_4grams = set(slovak_4_grams_only_1).intersection(set(german_4_grams_only_1))
slovak_czech_2grams = set(slovak_2_grams_only_1).intersection(set(czech_2_grams_only_1))
slovak_czech_3grams = set(slovak_3_grams_only_1).intersection(set(czech_3_grams_only_1))
slovak_czech_4grams = set(slovak_4_grams_only_1).intersection(set(czech_4_grams_only_1))

polish_danish_2grams = set(polish_2_grams_only_1).intersection(set(danish_2_grams_only_1))
polish_danish_3grams = set(polish_3_grams_only_1).intersection(set(danish_3_grams_only_1))
polish_danish_4grams = set(polish_4_grams_only_1).intersection(set(danish_4_grams_only_1))
polish_german_2grams = set(polish_2_grams_only_1).intersection(set(german_2_grams_only_1))
polish_german_3grams = set(polish_3_grams_only_1).intersection(set(german_3_grams_only_1))
polish_german_4grams = set(polish_4_grams_only_1).intersection(set(german_4_grams_only_1))
polish_czech_2grams = set(polish_2_grams_only_1).intersection(set(czech_2_grams_only_1))
polish_czech_3grams = set(polish_3_grams_only_1).intersection(set(czech_3_grams_only_1))
polish_czech_4grams = set(polish_4_grams_only_1).intersection(set(czech_4_grams_only_1))

danish_german_2grams = set(danish_2_grams_only_1).intersection(set(german_2_grams_only_1))
danish_german_3grams = set(danish_3_grams_only_1).intersection(set(german_3_grams_only_1))
danish_german_4grams = set(danish_4_grams_only_1).intersection(set(german_4_grams_only_1))
danish_czech_2grams = set(danish_2_grams_only_1).intersection(set(czech_2_grams_only_1))
danish_czech_3grams = set(danish_3_grams_only_1).intersection(set(czech_3_grams_only_1))
danish_czech_4grams = set(danish_4_grams_only_1).intersection(set(czech_4_grams_only_1))

german_czech_2grams = set(german_2_grams_only_1).intersection(set(czech_2_grams_only_1))
german_czech_3grams = set(german_3_grams_only_1).intersection(set(czech_3_grams_only_1))
german_czech_4grams = set(german_4_grams_only_1).intersection(set(czech_4_grams_only_1))

with open(sys.argv[1],"w", encoding='UTF-8') as file_out:
    print("writing to " + sys.argv[1])
    file_out.write("#Number of occurrences: " + str(len(common_2grams)) + "\ncommon_2grams  = " + str(sorted(common_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(common_3grams)) + "\ncommon_3grams  = " + str(sorted(common_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(common_4grams)) + "\ncommon_4grams  = " + str(sorted(common_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_slovak_2grams)) + "\nhungarian_slovak_2grams  = " + str(sorted(hungarian_slovak_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_slovak_3grams)) + "\nhungarian_slovak_3grams  = " + str(sorted(hungarian_slovak_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_slovak_4grams)) + "\nhungarian_slovak_4grams  = " + str(sorted(hungarian_slovak_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_english_2grams)) + "\nhungarian_english_2grams  = " + str(sorted(hungarian_english_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_english_3grams)) + "\nhungarian_english_3grams  = " + str(sorted(hungarian_english_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_english_4grams)) + "\nhungarian_english_4grams  = " + str(sorted(hungarian_english_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_polish_2grams)) + "\nhungarian_polish_2grams  = " + str(sorted(hungarian_polish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_polish_3grams)) + "\nhungarian_polish_3grams  = " + str(sorted(hungarian_polish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_polish_4grams)) + "\nhungarian_polish_4grams  = " + str(sorted(hungarian_polish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_danish_2grams)) + "\nhungarian_danish_2grams  = " + str(sorted(hungarian_danish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_danish_3grams)) + "\nhungarian_danish_3grams  = " + str(sorted(hungarian_danish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_danish_4grams)) + "\nhungarian_danish_4grams  = " + str(sorted(hungarian_danish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_german_2grams)) + "\nhungarian_german_2grams  = " + str(sorted(hungarian_german_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_german_3grams)) + "\nhungarian_german_3grams  = " + str(sorted(hungarian_german_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_german_4grams)) + "\nhungarian_german_4grams  = " + str(sorted(hungarian_german_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_czech_2grams)) + "\nhungarian_czech_2grams  = " + str(sorted(hungarian_czech_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_czech_3grams)) + "\nhungarian_czech_3grams  = " + str(sorted(hungarian_czech_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(hungarian_czech_4grams)) + "\nhungarian_czech_4grams  = " + str(sorted(hungarian_czech_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_slovak_2grams)) + "\nenglish_slovak_2grams  = " + str(sorted(english_slovak_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_slovak_3grams)) + "\nenglish_slovak_3grams  = " + str(sorted(english_slovak_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_slovak_4grams)) + "\nenglish_slovak_4grams  = " + str(sorted(english_slovak_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_polish_2grams)) + "\nenglish_polish_2grams  = " + str(sorted(english_polish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_polish_3grams)) + "\nenglish_polish_3grams  = " + str(sorted(english_polish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_polish_4grams)) + "\nenglish_polish_4grams  = " + str(sorted(english_polish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_danish_2grams)) + "\nenglish_danish_2grams  = " + str(sorted(english_danish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_danish_3grams)) + "\nenglish_danish_3grams  = " + str(sorted(english_danish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_danish_4grams)) + "\nenglish_danish_4grams  = " + str(sorted(english_danish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_german_2grams)) + "\nenglish_german_2grams  = " + str(sorted(english_german_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_german_3grams)) + "\nenglish_german_3grams  = " + str(sorted(english_german_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_german_4grams)) + "\nenglish_german_4grams  = " + str(sorted(english_german_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_czech_2grams)) + "\nenglish_czech_2grams  = " + str(sorted(english_czech_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_czech_3grams)) + "\nenglish_czech_3grams  = " + str(sorted(english_czech_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(english_czech_4grams)) + "\nenglish_czech_4grams  = " + str(sorted(english_czech_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_polish_2grams)) + "\nslovak_polish_2grams  = " + str(sorted(slovak_polish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_polish_3grams)) + "\nslovak_polish_3grams  = " + str(sorted(slovak_polish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_polish_4grams)) + "\nslovak_polish_4grams  = " + str(sorted(slovak_polish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_danish_2grams)) + "\nslovak_danish_2grams  = " + str(sorted(slovak_danish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_danish_3grams)) + "\nslovak_danish_3grams  = " + str(sorted(slovak_danish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_danish_4grams)) + "\nslovak_danish_4grams  = " + str(sorted(slovak_danish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_german_2grams)) + "\nslovak_german_2grams  = " + str(sorted(slovak_german_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_german_3grams)) + "\nslovak_german_3grams  = " + str(sorted(slovak_german_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_german_4grams)) + "\nslovak_german_4grams  = " + str(sorted(slovak_german_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_czech_2grams)) + "\nslovak_czech_2grams  = " + str(sorted(slovak_czech_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_czech_3grams)) + "\nslovak_czech_3grams  = " + str(sorted(slovak_czech_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(slovak_czech_4grams)) + "\nslovak_czech_4grams  = " + str(sorted(slovak_czech_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_danish_2grams)) + "\npolish_danish_2grams  = " + str(sorted(polish_danish_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_danish_3grams)) + "\npolish_danish_3grams  = " + str(sorted(polish_danish_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_danish_4grams)) + "\npolish_danish_4grams  = " + str(sorted(polish_danish_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_german_2grams)) + "\npolish_german_2grams  = " + str(sorted(polish_german_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_german_3grams)) + "\npolish_german_3grams  = " + str(sorted(polish_german_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_german_4grams)) + "\npolish_german_4grams  = " + str(sorted(polish_german_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_czech_2grams)) + "\npolish_czech_2grams  = " + str(sorted(polish_czech_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_czech_3grams)) + "\npolish_czech_3grams  = " + str(sorted(polish_czech_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(polish_czech_4grams)) + "\npolish_czech_4grams  = " + str(sorted(polish_czech_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(danish_german_2grams)) + "\ndanish_german_2grams  = " + str(sorted(danish_german_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(danish_german_3grams)) + "\ndanish_german_3grams  = " + str(sorted(danish_german_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(danish_german_4grams)) + "\ndanish_german_4grams  = " + str(sorted(danish_german_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(danish_czech_2grams)) + "\ndanish_czech_2grams  = " + str(sorted(danish_czech_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(danish_czech_3grams)) + "\ndanish_czech_3grams  = " + str(sorted(danish_czech_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(danish_czech_4grams)) + "\ndanish_czech_4grams  = " + str(sorted(danish_czech_4grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(german_czech_2grams)) + "\ngerman_czech_2grams  = " + str(sorted(german_czech_2grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(german_czech_3grams)) + "\ngerman_czech_3grams  = " + str(sorted(german_czech_3grams)) + "\n\n")
    file_out.write("#Number of occurrences: " + str(len(german_czech_4grams)) + "\ngerman_czech_4grams  = " + str(sorted(german_czech_4grams)) + "\n\n")