---
layout: post
title: "Token analysis"
date: 2023-05-09
---

1. [Introduction](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#introduction)
2. [A few definitions to start with](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#a-few-definitions-to-start-with)
3. [Obtaining data about our *n-grams*](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#obtaining-data-about-our-n-grams)
    1. [First step: Retrieving tokens from the test sets](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#first-step-retrieving-tokens-from-the-test-sets)
    2. [Second step: Obtaining lists of *n-grams* from the tokens](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#second-step-obtaining-lists-of-n-grams-from-the-tokens)
    3. [Third step: Producing dictionaries of occurrences from the *n-grams*](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#third-step-producing-dictionaries-of-occurrences-from-the-n-grams)
    4. [Fourth step: Cleaning the dictionaries](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#fourth-step-cleaning-the-dictionaries)
    5. [Fifth (and last) step: Obtaining more specific data](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#fifth-and-last-step-obtaining-more-specific-data)
    6. [A new variable added: the ground truth of the collection studied](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#a-new-variable-added-the-ground-truth-of-the-collection-studied)
4. [Results](https://flochiff.github.io/phd/2023/05/09/Token-analysis.html#results)

## Introduction
As I presented it previously, I already did a lexicon analysis with my test corpus (the sets of War corpus and Other (subjects) corpus) and it wasn't very conclusive, since the lexicon didn't seem to be involved in the bad results of the models. Given this result, I decided to go a little deeper in the source of my test as I decided to go at a sublexical level and to study tokens. Following along my research on what is recognized by the text recognition software, I want to know if the patterns recognized in handwritten text recognition are those of recurring tokens, i.e. recurrent combinations of characters. This would also mean that the mistakes in the transcription would be caused by less known patterns from the ground truth.

## A few definitions to start with
During this experiment, I will use some terms that it is important to define prior to any mention, in order to easily understand what I am about to present. So, I work here with tokens and *n-grams*.  
A token, as it is used here, can be defined as a string of characters. I mostly use this word to present my experiment because it starts with a tokenization, which is a process where long characters sequences will be split into much smaller units.  
The term that will be used to call those smaller units is *n-gram*. An *n-gram* is a “contiguous sequence of n items from a given sample of text or speech” ([https://en.wikipedia.org/wiki/N-gram](https://en.wikipedia.org/wiki/N-gram)).  
As *n* is meant to not specify a length for the sequence, I will use it when I want to remain general, but during the experiments I will also use the terms created to name sequences of two characters (*2-grams* or bigrams), three characters (*3-grams* or trigrams) and four characters (*4-grams* or tetragrams). 

## Obtaining data about our *n-grams*
Before I can observe and deduce anything, it is essential that I obtain not only my *n-grams*, but also information on their composition, their occurrences, the similarities between the two test sets (War and Other), etc. This will be done in several steps.

### First step: Retrieving tokens from the test sets
This is a pretty simple step, mostly because it is really close to what I have already done in a [script](https://github.com/FloChiff/phd/blob/main/experiments/content_analysis/scripts/producing_tokens_and_lemmas.py) from the content analysis' experiment to create my list of tokens. However, this is not the same script because I am not cleaning the file beforehand as much as I did, because this time, some punctuations are important for the tokenization.  
With [creating_list_of_tokens_from_texts.py](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/creating_list_of_tokens_from_texts.py), I am using spaCy again, with its French model, to produce tokens. The tokenization is done as such: spaCy's [tokenizer](https://spacy.io/usage/linguistic-features#tokenization) separates at every space in the text, but also according to some punctuations. In French, when a word is link to its pronoun with an apostrophe, the apostrophe is kept and put with the pronoun as the ensemble of the token. Once all the tokens from the called file have been retrieved, they are placed in a Python list written in an output file. Those two lists of tokens (War and Other) can be found in the [file of results](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_lists_and_dictionaries.py) at the lines 12 and 55.

### Second step: Obtaining lists of *n-grams* from the tokens
The goal, now that I have the lists of tokens, is to produce different *n-grams* from those lists. To proceed, I use the Python module [`textwrap`](https://docs.python.org/3/library/textwrap.html#module-textwrap) and its method called _wrap()_. It works with two arguments: a string text and a max width of characters. The string will then be divided into the width given, and it will render a list of the new output lines. In my script [producing_list_of_ngrams.py](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/producing_list_of_ngrams.py), it is used as such:

- Empty lists for each *n-gram* (bigrams, trigrams and tetragrams) are created
- A _for_ loop is created ; it will iterate on every element of the list of tokens called (War or Other), so each token will be considered individually
- In the loop, the _wrap()_ method is called, its first argument will call individually the items from the list and the second argument will be either 2, 3 or 4. The idea here is that, if one of the element from the list of token contains more than 2, 3 or 4 characters, it will be divided into an even smaller unit of characters to fit the *n-gram* called at the time. Then, I transform the list of outputs into a string, in order to add it into the lists of *n-gram* created earlier.
- Once the outputs have been collected for each *n-gram*, it is joined in *n-gram* dedicated lists (with some “cleaning” done to delete the punctuation from the _wrap()_ list created before and transform into a string), then written in an output file.

From this script, I obtain six lists, with three for each set, which can be found in the [file of results](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_lists_and_dictionaries.py) at the lines 18 (*4-grams*), 30 (*3-grams*) and 42 (*2-grams*) for the set 'Other', and the lines 61 (*4-grams*), 73 (*3-grams*) and 85 (*2-grams*) for the set 'War'.

### Third step: Producing dictionaries of occurrences from the *n-grams*
Even though obtaining the lists of *n-grams* is a good step in itself, it does not teach me anything as it is. To really start my study and understand the patterns in the recognition, it is essential to add a new step, which will be to count the occurrences of each *n-gram* to find those that appears in numerous occasions and those that are only there once.  
To proceed to this step, I used a function created for the content analysis' experiment, which is [counting.py](https://github.com/FloChiff/phd/blob/main/experiments/content_analysis/scripts/counting.py). The function in itself was used as such ; the only changing elements were the input and output.  
The script [producing_dictionary_of_ngrams_occurences.py](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/producing_dictionary_of_ngrams_occurences.py) has a lot of lines, but the last one is the one that really matters. After creating an output file, the script reads the input, which is one of the lists from the [file of results](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_lists_and_dictionaries.py). The _counting()_ function will read the list, count the number of occurrences for the elements present in it, and produce a dictionary. Moreover, I added some specificities to the output of this dictionary, so, according to the arguments I added, the dictionary will be sorted by the number of occurrences (values), from the most present to the least.
From this script, I obtain eight dictionaries, with four for each set, which can be found in the [file of results](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_lists_and_dictionaries.py) at the lines 15 (tokens), 21 (*4-grams*), 33 (*3-grams*) and 45 (*2-grams*) for the set 'Other', and the lines 58 (tokens), 64 (*4-grams*), 76 (*3-grams*) and 88 (*2-grams*) for the set 'War'.

### Fourth step: Cleaning the dictionaries
I now have all the dictionaries that I need for my experiment and my observations, but when I look at them, I realize that they contain a lot of irrelevant data. Indeed, as I presented it previously, the _wrap()_ method created smaller units of 2, 3 or 4 characters when the string was longer than that, but there were a lot of elements where the token was smaller than that, where punctuation is involved or even cases where, for example, a token was 4 characters and the wrapping with 3 created a unit of 3 characters and one of 1 character for that token. In that case, the first unit is interesting for us but not the second. Therefore, the goal in this step is to get rid of all this useless data and only keep the string of 2 characters for bigrams, 3 characters for trigrams and 4 characters for tetragrams.  
This cleaning can be done with a text editor and regular expressions ; here is an example for a dictionary of *3-grams*:

- In a text editor, copy/paste the chosen list
- Do a find/replace with `, ` (a comma then a space) in "Find" and `\n` (a newline) in "Replace"
- Once each key from the dictionary is on its own line, I will search for the trigrams: `^('|").{3}('|"):.+`
- Then, I click on "Find all" which will select all the lines corresponding to the regular expression
- I copy it and paste it on another file
- I do some manual cleaning by also deleting trigrams where one of the characters is punctuation such as a dash, a quotation mark, a dot, etc. ; for that, I use the following regex `.+(-|"|\.|,|€|/|£).+\n` in "Find" and do a "Replace All" with nothing it to delete those lines. I can also delete trigrams where there are numbers, because I only want letters : `'[0-9]{3}':.+\n` in "Find" and do a "Replace All" with nothing in it to delete those lines.
- From there, there are two options:
	1. I transform it back into a list, by reversing the above command (`\n` in "Find" and `, ` in "Replace") and adding again the brackets and title of the dictionary
    2. I transform my file into a CSV by using the following commands : `^'` --> `"`; `$` --> `"`; `': ` --> `","` and then adding a header in the first line (`"tokens","occurrences"`)
 
 Here is a detailed explanation on the regular expressions I used:
 
 - `^('|").{3}('|"):.+` --> This means that I search lines with a single or double quotation marks `('|")` at the begining of the line `^`, then 3 characters `.{3}` immediatly followed by the closing quotation marks `('|")` then the colon and the number of occurrences `:.+`. This regex ensures to dismiss all non-trigrams lines. This can also be easily adapted to bigrams or tetragrams, by changing the number in the curly brackets: `.{2}` for bigrams and `.{4}` for tetragrams.
 - `.+(-|"|\.|,|€|/|£).+\n` --> This means that I searched, in the line, cases where one of the characters mentioned in the parenthesis is presented between the opening of the line and the occurrences number. The newline \n is there to be sure that the whole line disappear after I clicked on the empty "Replace All".
 - `'[0-9]{3}':.+\n` --> This means that I searched, in the line, cases where between the quotation marks there are only numbers. This can be adapted to other *n-grams* by changing the number in the curly brackets, like above.
 
The cleaned versions of my dictionaries of *n-grams* can be found in CSV files in a [folder](https://github.com/FloChiff/phd/tree/main/experiments/token_analysis/clean_lists_of_tokens) on the repository. The file contains six columns, because I choose to separate the results in three: all capitals, initials and lowercases. Otherwise, the table is ranking as such: most to least popular occurrences and when there is several tokens with the same number of occurrences, it is sorted alphabetically, from A to Z.

### Fifth (and last) step: Obtaining more specific data
The dictionaries are now cleaned, which means that I will be able to properly conduct my observations. However, even though the data that I currently have can be enough for me to do my work, I also wanted to have some more precise elements and results so I decided to do a few more transformations and to gather specific data from what I already had.  

To be more precise in my observations, I decided to add two other types of lists: the most and least popular tokens based on the number of occurrences. Considering the results I got, I choose to go with 11 occurrences or more for the most popular and only one occurrence for the least popular. I collected it from every *n-gram* and added them in the [file of results](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_lists_and_dictionaries.py): 

- The lists for the most popular tokens can be found at the lines 24 (*4-grams*), 36 (*3-grams*) and 48 (*2-grams*) for the set 'Other', and the lines 67 (*4-grams*), 79 (*3-grams*) and 91 (*2-grams*) for the set 'War'. 
- The lists for the least popular tokens can be found at the lines 27 (*4-grams*), 39 (*3-grams*) and 51 (*2-grams*) for the set 'Other', and the lines 70 (*4-grams*), 82 (*3-grams*) and 94 (*2-grams*) for the set 'War'. 

From those lists, I went again deeper, to search for the common and unique elements between the sets. For that, I used two methods that were already proven effective when used during the content analysis' experiment: _[difference()](https://www.w3schools.com/python/ref_set_difference.asp)_ and _[intersection()](https://www.w3schools.com/python/ref_set_intersection.asp)_. This is done in the script [creating_list_of_tokens_from_ngrams.py](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/creating_list_of_tokens_from_ngrams.py). This script operates in three steps:

1. In the preamble, the lists that will be exploited are imported from the file of results mentioned many times in this document;
2. New lists of common and unique tokens are created and stored in variables;
3. An ouput file is created and in it, each new lists are written, with their variable name as their list name.  

There are two versions of this script, which can be chosen by putting in triple quoting marks the one not wanted. One will input and output lists about the [most popular tokens](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_unique_and_common_most_popular.py) and the other will be about the [least popular tokens](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_unique_and_common_least_popular.py.py).

Then, I extracted the information from the lists of the most popular tokens, to give a concrete idea of what was most popular in terms of tokens. Those popular tokens can be found in the [following document](https://flochiff.github.io/phd/experiments/token_analysis/popular_tokens_token_analysis.html). In it, there are tables with the alphabetically-sorted list of popular tokens, with three columns, one for each *n-grams*. There are also two versions of thoses tables: a plain one with the lists and one where the stopwords were highlighted in each lists.

Now, I have an important number of lists (38) and dictionaries (8) and I thought this might be easier to convert some of that data into tables of numbers, to get statistics about my results. Thus, I created a [table of results](https://flochiff.github.io/phd/experiments/token_analysis/table_results_token_analysis.html), divided in three parts: set Other, set War and comparison. For the comparison, I used the results from the lists I obtained with the [script](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/creating_list_of_tokens_from_ngrams.py) mentioned a few paragraphs before. There are six tables, three that gives the length of each list (all tokens and most and least popular tokens), one that gives the percentages of all caps, initials and lowercases for each *n-gram* and two that gives the percentages of unique tokens from each set compared to all the tokens.  
For each set, there are six tables. Three present the quantity and percentage of most and least popular tokens, with also the presence of the stopwords for the popular tokens. The other separates the results of occurrences in three formats: tokens in all caps, with uppercases initials and all lowercases. The table themselves contain several rows, that corresponds to range of occurrences: only 1, 2 to 5, 6 to 10, 11 to 50. When it happened in the result, I also added 51 to 100 and 101 to 500. In one table, the range "501 to 1000" and "more than 1000" were also added.

Finally, with those tables, I also decided to add a graphical representation of the data, in the form of bar charts. The graphics can be found [here](https://flochiff.github.io/phd/experiments/token_analysis/bar_charts_token_analysis.html). The vertical axis represents the quantity of tokens. The horizontal axis is divided into parts, one for each range of occurrences. In each range, there are three bars, one for each *n-gram* to compare them more clearly: the bigrams in green, the trigrams in blue and the tetragrams in yellow.

### A new variable added: the ground truth of the collection studied
The collection that is studied here with test sets was already used to produce an efficient text recognition model, after the training of about 250 transcribed pages, which gave a model of 97,98% of accuracy. This model and its ground truth represents a huge gap in terms of numbers and I though that it would be interesting to add it to the study, for comparison and to see if that can help answer the initial question of the token effect on the recognition.  
Therefore, all of the results files that I mentioned earlier and that I am summarizing below also contains data about those ground truth.

## Results
Here is a summary of the different results produced from the whole experiment.

- [Alphabetical list of the most popular tokens](https://flochiff.github.io/phd/experiments/token_analysis/popular_tokens_token_analysis.html)
- [Bar charts of *n-grams* by occurrences](https://flochiff.github.io/phd/experiments/token_analysis/bar_charts_token_analysis.html)
- [Clean list of *n-grams* and their occurrences](https://github.com/FloChiff/phd/tree/main/experiments/token_analysis/clean_lists_of_tokens)
- [Lists of the unique and common tokens from the most popular tokens](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_unique_and_common_most_popular.py)
- [Lists of the unique and common tokens from the least popular tokens](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_unique_and_common_least_popular.py)
- [Table of results of *n-grams* and their occurrences](https://flochiff.github.io/phd/experiments/token_analysis/table_results_token_analysis.html)
- [Various lists and dictionaries of *n-grams* and their occurrences](https://github.com/FloChiff/phd/blob/main/experiments/token_analysis/scripts/results_lists_and_dictionaries.py)

