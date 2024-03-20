---
layout: page
title: "Glossary"
---

**Allographétique**: Various ways of writing the same letter from the Latin script, i.e. long s and curve s.

**Allography**: Variant grapheme of a letter or a word.

**Character Error Rate (CER)**: Count of the minimum number of character-level operations required to transform the ground truth text into the OCR output. \\
Formula: CER = Substitution(s) + Insertion(s) + Deletion(s) / Number of characters in the GT \\
The lower the CER value (with 0 being a perfect score), the better the performance of the OCR model.

**Convolutional Neural Network (CNN)**: CNNs are deep learning models used for processing and analysing visual data. They leverage filters and layers to recognise patterns and features within images.  

**Dropout**: Method to counter the overfitting. At each epoch, some neurons in the network will be deactivated aleatory (so that it is not the same each time), which means that the model will be trained with a different neuron configuration each time, which will produce slightly different models each time.

**"Gold" corpus**: Data exclusively created and verified by humans, to obtain a perfect transcription.

**Ground Truth (GT)**: (Perfect) transcription of a text (usually human-made), that will later be used to train model(s) fitted for the automatic transcription of a corpus/corpora.

**Handwritten Text Recognition (HTR)**: Ability of a computer or device to take as input handwriting from sources such as printed physical documents, pictures and other devices, or to use handwriting as a direct input to a touchscreen and then interpret this as text.

**Levenshtein distance**: Metric for measuring the difference between two sequences. The Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

**Online/Offline Handwriting recognition**: Both functions pretty much the same, as it follows the definition for HTR given above, with the difference, for the Online HR that, by writing on a PDA of digitize, the recognition is helped by a sensor that picks up the pen-tip movements as well as pen-up/pen-down switching.

**Optical Character Recognition (OCR)**: Electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document or a scene-photo.

**Overfitting**: Situation, during model training, where the model is trying too much to fit the training data. Instead of trying to become a model with general data, it will try to match at best the training data, including all the noise it contains, which will, afterwards, mess with its predicting quality and make itself an unsuited model for other corpus.

**"Silver" corpus**: Data acquired by the prediction of the model made from the gold corpus.

**Token**: Any contiguous sequence of alphanumeric characters, beginning with a letter and occurring between spaces, slashes, brackets, braces, parentheses, quotation marks, and punctuation marks.

**Word Error Rate (WER)**: Count of the minimum number of word-level operations required to transform the ground truth text into the OCR output. \\
Formula: WER = Word substitution(s) + Word insertion(s) + Word deletion(s) / Number of words in the GT \\
The value of the WER is usually higher than the CER value
