# -*- UTF-8 -*-

"""
- author: Floriane Chiffoleau
- date: September 2022
- description: Cleaning ground truth to obtain a list of tokens and lemmas
- input: TXT file
- output: Python file
- usage :
    ======
    python name_of_this_script.py arg1 arg2
    arg1: file with all the groundtruth combined
    arg2: file with the lists of tokens and lemmas
"""

import re
import sys
#Importing the NLP tool and the language source we want to work with
import spacy
nlp = spacy.load('fr_core_news_lg')

def delete_punctuation(text):
    """ Deleting punctuation marks from the text
    
    :param text: Text to clean
    :type text: str
    :returns: Texte without punctuation
    :rtype: str
    """
    punctuation = "!:;()\",?'’.°"
    for marker in punctuation:
        text = text.replace(marker, " ")
    return text

with open(sys.argv[1], 'r') as file_in:
    print("reading from "+sys.argv[1])
    text = file_in.read()

    #Remove elements that can't be taken into account in the frequency list
    text = re.sub(r"- [0-9]{1,} -\n", "", text)
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"[0-9]", "", text)
    text = re.sub(r"X{3,}", "", text)
    text = re.sub("/", "", text)
    text = delete_punctuation(text)
    text = text.replace("££", "")
    text = text.replace("€", "")
    
    #Transform every uppercase letter in lowercase to avoid falsifying the count
    text = text.lower()
    
    token_list = []
    lemma_list = []
    doc = nlp(text)
    for token in doc:
        #Call the tokens and their lemma versions
        lemmas = token.lemma_ + " "
        tokens = str(token) + " "
        token_list.append(tokens)
        lemma_list.append(lemmas)
    tokens = "".join(token_list)
    lemmas = "".join(lemma_list)
with open(sys.argv[2], 'w') as file_out:
    print("writing to "+sys.argv[2])
    file_out.write("lemme = \"" + str(lemmas) + "\"\n\n")
    file_out.write("token = \"" + str(tokens) + '"')