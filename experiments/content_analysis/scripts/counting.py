#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def counting(words): 
    """ Counting the number of occurrences of each word in the text
    
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

source = ""
text = source.split(" ")
print(counting(text))