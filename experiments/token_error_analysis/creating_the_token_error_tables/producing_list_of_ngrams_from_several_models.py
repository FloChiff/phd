#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: June 2023
- description: Producing lists of n-grams
- output: Python files
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: file with the lists of n-grams
"""

import sys
#Python method that transform a paragraph of text into lines of maximum width of characters
from textwrap import wrap

correct_transcription = []
model_war = []
model_other = []
model_gt = []

#Create lists for each n-grams
list_4grams = []
list_3grams = []
list_2grams = []
#Choose the list to call
for element in correct_transcription:
    ngrams = wrap(element, 4)
    ngrams = str(ngrams)
    list_4grams.append(ngrams)
    ngrams = wrap(element, 3)
    ngrams = str(ngrams)
    list_3grams.append(ngrams)
    ngrams = wrap(element, 2)
    ngrams = str(ngrams)
    list_2grams.append(ngrams)
tetragrams_correct_transcription = "".join(list_4grams)
trigrams_correct_transcription = "".join(list_3grams)
bigrams_correct_transcription = "".join(list_2grams)
list_4grams = []
list_3grams = []
list_2grams = []
for element in model_other:
    ngrams = wrap(element, 4)
    ngrams = str(ngrams)
    list_4grams.append(ngrams)
    ngrams = wrap(element, 3)
    ngrams = str(ngrams)
    list_3grams.append(ngrams)
    ngrams = wrap(element, 2)
    ngrams = str(ngrams)
    list_2grams.append(ngrams)
tetragrams_model_other = "".join(list_4grams)
trigrams_model_other = "".join(list_3grams)
bigrams_model_other = "".join(list_2grams)
list_4grams = []
list_3grams = []
list_2grams = []
for element in model_war:
    ngrams = wrap(element, 4)
    ngrams = str(ngrams)
    list_4grams.append(ngrams)
    ngrams = wrap(element, 3)
    ngrams = str(ngrams)
    list_3grams.append(ngrams)
    ngrams = wrap(element, 2)
    ngrams = str(ngrams)
    list_2grams.append(ngrams)
tetragrams_model_war = "".join(list_4grams)
trigrams_model_war = "".join(list_3grams)
bigrams_model_war = "".join(list_2grams)
list_4grams = []
list_3grams = []
list_2grams = []
for element in model_gt:
    ngrams = wrap(element, 4)
    ngrams = str(ngrams)
    list_4grams.append(ngrams)
    ngrams = wrap(element, 3)
    ngrams = str(ngrams)
    list_3grams.append(ngrams)
    ngrams = wrap(element, 2)
    ngrams = str(ngrams)
    list_2grams.append(ngrams)
tetragrams_model_gt = "".join(list_4grams)
trigrams_model_gt = "".join(list_3grams)
bigrams_model_gt = "".join(list_2grams)
with open(sys.argv[1], "w") as file_out:
    print(f'Writing to {sys.argv[1]}')
    file_out.write("tetragrams_correct_transcription = " + tetragrams_correct_transcription + "\n")
    file_out.write("trigrams_correct_transcription = " + trigrams_correct_transcription + "\n")
    file_out.write("bigrams_correct_transcription = " + bigrams_correct_transcription + "\n")
    file_out.write("tetragrams_model_other = " + tetragrams_model_other + "\n")
    file_out.write("trigrams_model_other = " + trigrams_model_other + "\n")
    file_out.write("bigrams_model_other = " + bigrams_model_other + "\n")
    file_out.write("tetragrams_model_war = " + tetragrams_model_war + "\n")
    file_out.write("trigrams_model_war = " + trigrams_model_war + "\n")
    file_out.write("bigrams_model_war = " + bigrams_model_war + "\n")
    file_out.write("tetragrams_model_gt = " + tetragrams_model_gt + "\n")
    file_out.write("trigrams_model_gt = " + trigrams_model_gt + "\n")
    file_out.write("bigrams_model_gt = " + bigrams_model_gt)