#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: March 2023
- description: Creating a list of tokens
- input: TXT files
- output: TXT files
- usage :
    ======
    python name_of_this_script.py arg1 arg2
    arg1: folder with the texts from the test set
    arg2: folder with the token lists from the test set
"""

import os
import re
import sys
import spacy
nlp = spacy.load('fr_core_news_lg')
#Import the module used for the tokenization of our text

for root, dirs, files in os.walk(sys.argv[1]):
    for filename in sorted(files):
        with open(sys.argv[1] + filename, 'r') as file:
            print(f'Reading {sys.argv[1] + filename}')
            text = file.read()
            doc = nlp(text)
            token_list = []
            for token in doc:
                tokens = '"' + token.text + '"; '
                token_list.append(tokens)
                #Dividing the text into tokens, while keeping the punctuation, numbers, etc.
            tokens = "".join(token_list)
            tokens = re.sub('\n', " ", tokens)
            with open(sys.argv[2] + "token_" + filename, 'w') as file_out: 
                print(f'Writing to {sys.argv[1]}token_{filename}')
                file_out.write(filename.replace('.txt', '') + " = [" + tokens + "]")