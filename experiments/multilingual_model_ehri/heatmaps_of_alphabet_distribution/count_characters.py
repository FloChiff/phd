#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def count_characters(text):
    # Create an empty dictionary to store character occurrences
    char_count = {}

    # Iterate through each character in the text
    for char in text:
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it is, increment the count
            char_count[char] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            char_count[char] = 1

    # Print the character occurrences
    for char, count in char_count.items():
        print(f"'{char}' = {count}")

text_to_read = #Content of the text from which characters will be counted
count_characters(text_to_read)