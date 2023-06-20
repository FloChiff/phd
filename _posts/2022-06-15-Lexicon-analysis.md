---
layout: post
title: "Lexicon analysis"
date: 2022-06-15
---

1. [Why a lexicon analysis ?](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#why-a-lexicon-analysis-)
2. [Few steps for the analysis](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#few-steps-for-the-analysis)
	1. [First step: Retrieving the texts to do the analysis](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#first-step-retrieving-the-texts-to-do-the-analysis)
	2. [Second step: Finding the perfect way to analyse the lexicon](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#second-step-finding-the-perfect-way-to-analyse-the-lexicon)
	3. [Third step: Providing a visualization for the output](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#third-step-providing-a-visualization-for-the-output)
3. [The analysis](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#the-analysis)
	1. [My source test](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#my-source-test)
	2. [My results](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#my-results)
		1. [Frequency list](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#frequency-list)
		2. [Wordcloud](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#wordcloud)
	3. [My conclusions](https://flochiff.github.io/phd/2022/06/15/Lexicon-analysis.html#my-conclusions)

## Why a lexicon analysis ?
I am currently working on a thesis in digital humanities. My research is centred around optical character recognition (OCR) and, most precisely, the ground truth used to produce a model for the transcription. The hypothesis I am trying to demonstrate is that the lexicon contained in the ground truth used for the production of a transcription model will ultimately impact the efficiency of the model on the corpus it is applied on. Consequently, if a corpus' main lexicon is the same as the one the model was trained on, the error rate of the transcription will be way lower than if it has an opposite lexicon.  

Therefore, as the lexicon represents a huge part in my research, I decided that I couldn't only test the efficiency of the text recognition model with comparative analysis; I also had to put my attention into the composition of the ground truth themselves, in order to get a baseline for the results. If I want to prove that the lexicon has an effect on the accuracy of the model, I need to know, when I am doing my test, that the ground truth and the source test have the same vocabulary; this would mean that the transcription should be pretty good, or the opposite (different lexicon, bad result). Thus, I decided to develop few techniques to analyse the lexicon of my texts.

## Few steps for the analysis
### First step: Retrieving the texts to do the analysis
To start my analysis, I need to get my hand on the text, in its raw form. My idea was to retrieve, from all the files exported from eScriptorium, the content of the tag or attribute containing the text of the transcription. As I had a lot of files in different folders, I created two scripts, one in Python and one in Bash, to do that rapidly. The [Python script](https://github.com/FloChiff/phd/blob/main/experiments/lexicon_analysis/word_frequency/groundtruth/scripts/groundtruth.py) works with BeautifulSoup because the exported files are in XML (Page or Alto) and it provides two options of text retrieving, depending on the XML export chosen. The output is in the 'a' mode as I need to add all the transcriptions in the same file. The [Bash script](https://github.com/FloChiff/phd/blob/main/experiments/lexicon_analysis/word_frequency/groundtruth/scripts/generate_groundtruth.sh) is just a way to gather in one go the content of the various folders.  
Once those two scripts have been executed, I have in a single file the full content I will use for the subsequent lexicon analysis.

### Second step: Finding the perfect way to analyse the lexicon
After retrieving my texts, I could start the analysis of the lexicon. To do so, I decided that the best choice was a frequency list:  
> In computational linguistics, a __frequency list__ is a sorted list of words (word types) together with their frequency, where frequency here usually means the number of occurrences in a given corpus, from which the rank can be derived as the position in the list. ^[[https://en.wikipedia.org/wiki/Word_list](https://en.wikipedia.org/wiki/Word_list)]

In order to generate that frequency list, I needed to create a [new script](https://github.com/FloChiff/phd/blob/main/experiments/lexicon_analysis/word_frequency/groundtruth/scripts/clean_groundtruth.py) that would clean the retrieved texts, count the words and render the occurrences.  
The cleaning of the files looked like this:  

- Delete all the numbers
- Remove all the line breaks
- Delete all the elements relating to the transcriptions (sign for handwriting, erased words, etc.)
- Remove all signs of punctuation
- Lowercase all words (to not have two words considered different just because one of them has its initial uppercased)

When this cleaning has been done, the text is separated word by word with the _split()_ method. Before generating the list, one more action need to be done : removing the stop words. A stop word is considered usually as a word that has no signification in itself and that is so common that indexing it is pointless, i.e., “the”, “is”, “at”, “which”, or “on”. The list of stop words can also be subjective, as anyone can decide the words they want to add in that list. For my analysis, the list is in French, as it is the language of my text and that list contains determiners, pronouns, common verbs and other kind of words ^[The list was downloaded from a [website](https://countwordsfree.com/stopwords) providing stop word lists].

Finally, the end of the script is the creation of this frequency list, as a dictionary is created with the word as the key and the number of occurrences as the value; the dictionary is also sorted from the largest number of occurrences to the smallest. This dictionary is then transformed to have the output in the CSV format (one column for the words and one for the occurrences).

### Third step: Providing a visualization for the output
This frequency list is exactly what I was looking for in my analysis, and it provides all the results that I need. However, I decided that I wanted to also have a proper visualization for this, in order to really highlight the words contained in the list. To do so, I choose to produce a word cloud, as a frequency list is exactly the input required for that, and it represents a good way to properly see most of the content in the frequency list.  
I used a [website](https://www.wordclouds.com/) designed solely for the generation of word clouds. To avoid having a word cloud way too complicated and overloaded, I removed from the frequency list all the words that had five occurrences or fewer; I considered that it is not frequent enough to be regarded as part of the lexicon.

## The analysis
### My source test
For this analysis, I have two set of texts. Both are extracted from the [Paul d'Estournelles de Constant's corpus](https://discholed.huma-num.fr/exist/apps/discholed/index.html?collection=pec%2Fcorpus), on which I have been working on since I started as an engineer at Inria in 2020.  
My first analysis covers the ground truths that were used for the training of the transcription model made for d'Estournelles corpus. This is a very large source, as I had almost 500 pages of transcription. About 400 were regular ground truths, with straight lines segmented and every one of them transcribed; the remaining one only had few words chosen on it, as a way to train the model to recognize numbers and uppercases (the parts that were removed from the frequency list). Between the regular ground truths and the specific one, they were some duplicates, as some letters used for the “normal” training also contains a lot of peculiar signs; therefore, they were used again when I did the training for special signs. The letters were chosen randomly, with no inside look of its content, which, as I will demonstrate later, will become a problem.  
Now, the ground truth were easily selected for the test because they were previously created for the training and production of the model. The other part of the source test were picked firstly for another reason. In parallel to this analysis, I am using the texts to do a comparative analysis of the quality of the model (which I will present in another logbook entry). In order to correctly conduct this analysis, I have chosen to select two types of letters from the new batch of letters that I have collected for the Paul d'Estournelles de Constant's corpus: letters about war and letters about anything else. This selection has been made after a thorough reading of the letters by me. As it is a personal appreciation, this lexicon analysis is a must-do afterwards, as it will be able to 1) verify my assessment and 2) check the possible variation of lexicon between the two kinds of style. The source test was created in two stages. I first selected fourteen letters, made of one to five pages, which gave me in total 43 pages of test. However, after doing the analysis, and notably with the scission between war letters and other, I realized that I needed more content to have a more accurate result. I then selected four additional letters: two were about the war and counted four/five pages; the other two were not about the war and were much longer, i.e., 17 and 41 pages. This means 64 pages (not 67 because three were removed because they were too complicated for the segmentation) for the new content and, in total, 107 pages for the source test, which should be much better for the test.

### My results
My lists and word clouds are now generated, and each document can be found in the following folders:  

- [Frequency list for the groundtruth](https://github.com/FloChiff/phd/blob/main/experiments/lexicon_analysis/word_frequency/groundtruth/)
- [Frequency lists for the source test (43 pages)](https://github.com/FloChiff/phd/blob/main/experiments/lexicon_analysis/word_frequency/test_43_pages/)
- [Frequency lists for the source test (107 pages)](https://github.com/FloChiff/phd/blob/main/experiments/lexicon_analysis/word_frequency/test_107_pages/)
- [Wordclouds for the grountruth and for the source test of 43 and 107 pages](https://flochiff.github.io/phd/experiments/lexicon_analysis/wordclouds_lexicon_analysis.html)

Here are the various observations that I gathered when looking at the files and comparing them:  

#### Frequency list

- The first four most occurrences in the text, no matter which analysis, are pretty much always the same ("guerre", "butler", "président", "paris"), the word "paix" is not far in any list either and the first ten most occurrences are also pretty similar.
- Adding longer letters in the source test provokes the disappearance at the top of the list of repetitive words from d'Estournelles formula at the end of his letters ("affectueusement", "dévoué)
- No specific lexicon can really be highlighted from the ground truth, there is just a lot of vocabulary about military or society stuff
- For the source test of 43 pages war/other --> the number of the top occurrences is very low (24 and 22 are the max for each category), it is not very revealing; more words in the _war_ section, more terms about military and war stuff in the source test
- For the source test of 107 pages war/other --> there are way more words in the _other_ section (3523 vs 1635); the top occurrences are a little higher than previously (42 and 38); the number of occurrences for the word "guerre" in one section or the other is pretty much the same (38 in the _war_ section for 37 in the _other_ section). However, I can observe a difference in the lexicon that seems to be used in either, contrary to the shorter source test. The _other_ section seems to have top words about political and societal stuff, while the _war_ section have more words about combat and diplomacy.

#### Wordcloud

- As previously stated, "guerre", "butler", "président" and "paris" are the words which stand out the most in the word cloud
- There are a lot of little inconsequential words present in every analysis
- Many words from d'Estournelles formula (address, salute, etc.) stand out a lot
- The word cloud for the source test of 107 pages seems to have many political terms that appear clearly in it
- Although the setting is the same for the 43 and 107 pages, the former has way more visible little words that stand out words, while the latter has more stand out words, especially in the _war_ section.


### My conclusions
With those various observations, I can draw some conclusions on what I can do next to improve my experiments and obtain possibly better results.  
Firstly, I think that I need to add some elements to my list of stop words. As I observed it multiple times, the content of d'Estournelles formula, such as "à Monsieur le Président Nicholas Murray Butler" or "Affectueusement dévoué", seems to have a significant place in the list of occurrences; whether it is because the letters are short, so their presence is almost systematic, or because it has been purposefully highlighted a lot in the ground truth, in order for the model to always recognize it. However, it adds no value to our analysis, just like the stop words, because it is not part of the lexicon used in the letters, but simply put in the letter, just like a pre-printed headers or signs could have been added. Hence, all of those elements could be added in the list of stop words so that they are not counted in the lexicon analysis, and it is more revealing.  
Secondly, I realized, while observing the content of the list, that it might be useful to create a referential for the type of lexicon that is supposed to be present in the ground truth and therefore, in the transcription model. Without a referential, the analysis of the words could be too subjective, and a source could be considered not fitted for the model when it in fact is. Those texts, and specifically the ground truth, should contain lexicon relating to war or peace and if "guerre", "paix", or "morts" are an easy example of what can be considered pertinent, others can be more tricky. Hence, for every theme chosen for the experiment, it should come with a referential of the expected vocabulary.
Finally, with regard to this previous observation and to what I was able to see when studying my ground truth, I think it might be better to change them, or at least redo the selection and ultimately the model, to better fit what I am trying to prove here. The transcription model is supposed to be about war, peace and diplomacy, but there is so much scattered content in it that it doesn't seem to be the case. Moreover, when I gathered those texts, I didn't really look at the content of the pages, what was the topic so, even though the letters date back to the war, it is possible that some of them weren't talking much about it and that it doesn't add to the wanted lexicon. Thus, it might be necessary to redo a ground truth selection where I pay more attention to my selection, like I did with my source test, and to produce a new model from there.
