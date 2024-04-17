---
layout: post
title: "Comparative analysis"
date: 2022-10-21
---

1. [Introduction](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#introduction)
2. [How to do a comparative analysis of transcription?](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#how-to-do-a-comparative-analysis-of-transcription)
	1. [Some definitions](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#some-definitions)
	2. [The tool: KaMi](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#the-tool-kami)
3. [Table of results](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#table-of-results)
	1. [General results](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#general-results)
	2. [Results by page](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#results-by-page)
		1. [Set Other](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#set-other)
			1. [Letter 1358 Page 4](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-1358-page-4)
			2. [Letter 607 Page 3](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-607-page-3)
			3. [Letter 607 Page 17](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-607-page-17)
			4. [Letter 722 Page 1](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-722-page-1)
			5. [Letter 1170 Page 3](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-1170-page-3)
			6. [Conclusion/General observations](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#conclusiongeneral-observations)
		2. [Set War](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#set-war)
			1. [Letter 678 Page 1](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-678-page-1)
			2. [Letter 1000 Page 3](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-1000-page-3)
			3. [Letter 1367 Page 1](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-1367-page-1)
			4. [Letter 844 Page 1](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-844-page-1)
			5. [Letter 948 Page 1](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#letter-948-page-1)
			6. [Conclusion/General observations](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#conclusiongeneral-observations-1)
	3. [New results: Model War Retrained](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#new-results-model-war-retrained)
		1. [General](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#general)
		2. [Results by letters](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#results-by-letters)
4. [Conclusion](https://flochiff.github.io/phd/2022/10/21/Comparative-analysis.html#conclusion)

## Introduction
As I previously mentioned, my thesis aims to determine if the lexicon of the ground truth has an impact on the efficiency of the model, especially if it is specific. To prove or refute this theory, I need to do different kind of tests.
In the last entry of my logbook, I presented the content analysis I did on two tests sets I developed from the corpus of Paul d'Estournelles de Constant. The idea was to obtain a thoroughly knowledge of the content of those tests sets.  
Those tests sets have been selected by reading the letters and each is supposed to have their own specific subject: one is about the war and the other is not about war but about "everything else" (For more information about the dataset, see [here](https://flochiff.github.io/phd/dataset/dataset.html)). After analysing the content and notably the unique tokens from each set, the theme selection appears more clearly. The war set is full of military terms, while the 'other' test set seems to be more about politics and administrative business. This seems logical, as war and politics are the two main topics of discussion between d'Estournelles and Butler.  
Now that I know more about my sets, I will try to demonstrate my theory by using them for transcription. With each set, I did a training on [eScriptorium](https://escriptorium.inria.fr/) and produced a model. Then, I apply to each set the model developed from the opposite set, but also the model developed from their respective set. The idea is to see how good the transcription can be, if the model has some problems recognizing some parts of the text, because it is not in the vocabulary it was trained with; moreover, we know, thanks to the word clouds the kind of words it should have problems with.  
Right from the start, I must point out that the efficiency of one of the models might be instantly better than the other, due to the quantity of data given for the training. Indeed, the "war" set is made of about 30 pages, while the "other" has double or even more pages, so it gave the trainer the opportunity to recognize characters and words with more occurrences, which will be a bonus.

## How to do a comparative analysis of transcription?
Before starting to check the transcriptions, it is important to ask how will we be able to evaluate the quality of the transcription and to determine how and why did it or did it not work. This is achievable with the help of some metrics created to evaluate exactly this sort of results and luckily, a specific tool have been developed to do that for us, by simply providing a text reference and a prediction.

### Some definitions
There are some metrics to know in order to understand how to evaluate the quality of a transcription.
First of all, the evaluation will be made by calculating the Levenshtein distance, which is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. For example, the Levenshtein distance between "complete" and "complet" will be 1, because there was one deletion ('e'), but, between "extraordinary" and "ektraodinnary", it will be 3 because there was one insertion ('n'), one deletion ('r') and one substitution ('x'-->'k').
Then, from that, the Word Error Rate (WER) and Character Error Rate (CER) will be calculated. The WER is a way to evaluate the quantity of words correctly transcribe by a model. It will be obtained as such: 

> Word substitution(s) + Word insertion(s) + Word deletion(s) / Number of words in the reference

From this WER, we can also deduce the word accuracy (Wacc) of the transcription, because we only need to do the following calculus:

> Word Accuracy = 1 - WER

The CER operates pretty much the same but we will be at the level of the characters (counting the spaces, punctuations, etc.):

> Substitution(s) + Insertion(s) + Deletion(s) / Number of characters in the reference

A high CER doesn't particularly mean a high WER, because the character errors could be centralised on some words and in the contrary, the CER could be quite low but with a WER that seems high, which would mean that the errors were spread on the transcription. However, this second case is usually the one most encountered, the CER being lower than the WER most times.

For the subsequent analysis that we will do, our metrics will be:

* Levenshtein distance, in characters and in words
* WER, CER and Wacc
* Hits (number of characters correctly guesses)
* Substitutions/Insertions/Deletions
* Length of the reference and of the prediction

### The tool: KaMI
For my comparative analysis, I want to obtain some of the metrics I mentioned above. In order to do so, I will use KaMi, which stands for Kraken Model Inspector, a tool built for the evaluation of models and based on the Kraken transcription system.

#### Functionalities
This tool evaluates the success of a transcription task on an image or several, comparing a correct transcription - the reference - and a prediction, produced by transcribing with a chosen model. The results will be a series of metrics, with notably the Levenshtein distance between the reference and the transcription, the Word Error Rate (WER) and the Character Error Rate (CER), the Word Accuracy (Wacc), as well as some others statistics taken from the Speech Recognition domain. With the results, the length of the reference and the prediction are also available, which is an already quick way to determine a difference.  
With the web application, it is also possible to have access to a 'versus text', which will show where are the differences between the reference and the prediction. This is a good way to determine more easily where the model had a problem, which could then be helpful to know how to better train and improve it. However, the web application is limited on the number of characters that can be submitted in the reference/prediction (7000 characters), so it will only be possible to test little bit of the transcription.

#### How to have access to KaMI
- [Web Application](https://huggingface.co/spaces/lterriel/kami-app)
- [GitHub](https://github.com/KaMI-tools-project/KaMi-lib)

## Table of results
### General results
#### Results

|  | Set War/Model War | Set War/Model Other | Set Other/Model Other | Set Other/Model War |
|--|--|--|--|--|
| Levenshtein distance (char) | 372 | 770 | 451 | 4090 |
| Levenshtein distance (words) | 322 | 540 | 346 | 2734 |
| WER | 4,92% | 8,25% | 2,08% | 16,48% |
| CER | 0,95% | 1,97% | 0,45% | 4,08% |
| Word Accuracy | 95,08% | 91,74% | 97,91% | 83,51% |
| Hits | 38658 | 38299 | 99797 | 96425 |
| Substitutions | 279 | 557 | 274 | 3301 |
| Deletions | 67 | 148 | 118 | 463 |
| Insertions | 26 | 65 | 59 | 327 |
| Length (reference) | 39004 | 39004 | 100189 | 100189 |
| Length (prediction) | 38963 | 38921 | 100130 | 100053 |

#### Observations
First of all, the most striking thing we can observe is the Levenshtein distance in characters where the gap between the model with the set it trained on and the model trained with the other set is really high. For the war set, the number has more than doubled and for the other set, the number has been multiplied by almost 10. Then, we can see with the length of the reference and the prediction that all predictions are missing characters compared to the reference (41 SW/MW; 83 SW/MO; 59 SO/MO; 136 SO/MW). This can be partly explained by the fact that there is a lot of deletions in every model application but at the same time, the insertions aren't that high. We can also observe that the substitutions are really high, the smallest number being 274 for the SO/MO, while the SO/MO is at more than ten times that with 3301. Overall, the word accuracy percentage are not that bad: for the model applied to the set it trained on, we have 95% (SW) and 97% (SO) which is pretty good; for the model applied to the opposite set, we have 91% (SW) and 83% (SO). With those number, we can see that the MO did really well on its own set but it wasn't so bad either on the other set. On the other end, the MW did pretty bad on the SO but it wasn't as high as it could have been on its own set. This tends to prove the idea that the SW should had had the same number of pages on its training set as the SO, because the problem of the model come from the lack of content rather than the content itself.

### Results by page
#### Set Other
##### Letter 1358 Page 4

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.bbd715g8/fe7ca9dd778be186ccae7b88f6b22937855c8473" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.bbd715g8/fe7ca9dd778be186ccae7b88f6b22937855c8473" width="150" title="Letter 1358 page 4"></a></figure>

###### Results

|  | Model Other | Model War |
|--|--|--|
| Levenshtein Distance (Char.) | 7 | 127 |
| Levenshtein Distance (Words) | 6 | 50 |
| Word Error Rate (WER in %) | 8.955 | 74.626 |
| Char. Error Rate (CER in %) | 1.369 | 24.853 |
| Word Accuracy (Wacc in %) | 91.044 | 25.373 |
| Hits | 504 | 386 |
| Substitutions | 4 | 116 |
| Deletions | 3 | 9 |
| Insertions | 0 | 2 |
| Total char. in reference | 511 | 511 |
| Total char. in prediction | 508 | 504 |

###### Observations
The length difference is not that high between the predictions and the reference, but the metrics are not so good. For the MO, there are few substitutions and deletions, which cause an accuracy of only 91%. On the other end, the MW is really bad, with a WER of 75% and a CER of 25%, due mostly to a high number of substitutions. When we look at the versus text, we can see that this page is mostly uppercases, which can explain the bad transcription. The MO had some problems with few similar looking letters and the MW struggle with most of them, rendering the transcription unintelligible.

##### Letter 607 Page 3

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.8991xkm4/72b5373146096b82d2279f0d6ba56a8e3736f918" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.8991xkm4/72b5373146096b82d2279f0d6ba56a8e3736f918" width="150" title="Letter 607 page 3"></a></figure>

###### Results

|  | Model Other | Model War |
|--|--|--|
| Levenshtein Distance (Char.) | 1 | 21 |
| Levenshtein Distance (Words) | 1 | 21 |
| Word Error Rate (WER in %) | 0.403 | 8.467 |
| Char. Error Rate (CER in %) | 0.063 | 1.331 |
| Word Accuracy (Wacc in %) | 99.596 | 91.532 |
| Hits | 1576 | 1557 |
| Substitutions | 1 | 19 |
| Deletions | 0 | 1 |
| Insertions | 0 | 1 |
| Total char. in reference | 1577 | 1577 |
| Total char. in prediction | 1577 | 1577 |

###### Observations
The number of characters in the prediction is the same for both models, but also with the reference. Only one substitution has been made on the transcription with the MO while a lot has been made with the other (19). The MO is almost perfect (more than 99%) while the MW is pretty accurate, even though it is not perfect (about 91%). With the versus, we can see that the MO replace an 'l' by a 'm' inside a word, which can be understandable because there was a substitution in the text itself, with a character behind the 'l'. The MW had the same problem with this weird letter and also had few problems with uppercase, numbers and some similarly shaped letters (p/b, m/n, o/e). Overall, we can say that the MW did rather well on this image from the SO.

##### Letter 607 Page 17

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.8991xkm4/b081dc81c084b83a3db96580306556bf6a24f10e" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.8991xkm4/b081dc81c084b83a3db96580306556bf6a24f10e" width="150" title="Letter 607 page 17"></a></figure>

###### Results

|  | Model Other | Model War |
|--|--|--|
| Levenshtein Distance (Char.) | 6 | 86 |
| Levenshtein Distance (Words) | 6 | 69 |
| Word Error Rate (WER in %) | 1.452 | 16.707 |
| Char. Error Rate (CER in %) | 0.247 | 3.549 |
| Word Accuracy (Wacc in %) | 98.547 | 83.292 |
| Hits | 2418 | 2335 |
| Substitutions | 3 | 66 |
| Deletions | 2 | 19 |
| Insertions | 1 | 1 |
| Total char. in reference | 2423 | 2423 |
| Total char. in prediction | 2422 | 2405 |

###### Observations
The MO did pretty well and was different from the reference by only one more character. It has a pretty good accuracy and a rather low CER. The MW, on the other end, is pretty bad: there is a lot of deletions and even more substitutions and it seemed to have impacted a lot of words because the WER is pretty high for this model (17%). The MO has had problems with the punctuations, confusing exclamation points or commas with characters. The MW has had a lot of difficulties at the beginning of the page, managing to transcribe incorrectly half of the first two sentences. Then, it had a lot of difficulties with recognizing correctly the uppercases and finally, it did a lot of substitutions that did not really make any sense, because the before and after characters have no resemblance at all. Overall, the MW was a big miss on that page.

##### Letter 722 Page 1

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.da8cb4yl/0413edfec4c21790bc4baa803a5c2aae24690c3e" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.da8cb4yl/0413edfec4c21790bc4baa803a5c2aae24690c3e" width="150" title="Letter 722 page 1"></a></figure>

###### Results

|  | Model Other | Model War |
|--|--|--|
| Levenshtein Distance (Char.) | 9 | 65 |
| Levenshtein Distance (Words) | 6 | 37 |
| Word Error Rate (WER in %) | 3.947 | 24.342 |
| Char. Error Rate (CER in %) | 1.032 | 7.454 |
| Word Accuracy (Wacc in %) | 96.052 | 75.657 |
| Hits | 866 | 811 |
| Substitutions | 5 | 61 |
| Deletions | 1 | 0 |
| Insertions | 3 | 4 |
| Total char. in reference | 872 | 872 |
| Total char. in prediction | 874 | 876 |

###### Observations
The MO is wrong by two more characters in its prediction and four more for the MW. The deletions and insertions are pretty low for both. However, the difference in substitutions is high (5 for MO and 61 for MW). Therefore, the MO has a good word accuracy (96%) and a low CER (1%), while the MW doesn't have a CER too high (7,5%) but this is not the case for the WER, which is at 24%. With the versus, we can see that the MO had some difficulties with the uppercase of the title and on the number of the letter (it forgot one), while the MW got all the title wrong and had a lot of difficulties on diverse words from the letter, without any pattern appearing (i.e., specific words or characters).

##### Letter 1170 Page 3

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.e691hsj0/88a93a7b84203e7df9249ca3dca9e551a61d3103" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.e691hsj0/88a93a7b84203e7df9249ca3dca9e551a61d3103" width="150" title="Letter 1170 page 3"></a></figure>

###### Results

|  | Model Other | Model War |
|--|--|--|
| Levenshtein Distance (Char.) | 11 | 56 |
| Levenshtein Distance (Words) | 7 | 44 |
| Word Error Rate (WER in %) | 2.661 | 16.73 |
| Char. Error Rate (CER in %) | 0.684 | 3.484 |
| Word Accuracy (Wacc in %) | 97.338 | 83.269 |
| Hits | 1597 | 1553 |
| Substitutions | 7 | 43 |
| Deletions | 3 | 11 |
| Insertions | 1 | 2 |
| Total char. in reference | 1607 | 1607 |
| Total char. in prediction | 1605 | 1598 |

###### Observations
While the MO only had two characters missing in the prediction, the MW had almost 10. The CER is not too high on the MW but this still impact a lot of words, because the WER is at 16%. The MO did pretty well, with an accuracy of 97%. The problem from the MO transcription seems to come from the facsimile in itself, because there were some characters that were pretty difficult to transcribe because there were in themselves hard to decrypt in the image. The MW struggle at the same places but also on some random characters with no real patterns.

##### Conclusion/General observations
In conclusion, for this test set, we can say that the MO rather did well on the transcription that it was trained on. On the other end, the MW, which was trained on a different text and with less content, did pretty well on only one of the letters: the only one that was almost all 'normal' text, without any specific characters. However, when we go on more 'complicated' letters with uppercases or other, it seems to struggle more and even with characters that it had no difficulties prior.

#### Set War
##### Letter 678 Page 1

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.cc374i0g/6ea6739856ae6fc8156d2749f126354aa6aff3e2" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.cc374i0g/6ea6739856ae6fc8156d2749f126354aa6aff3e2" width="150" title="Letter 678 page 1"></a></figure>

###### Results

|  | Model War | Model Other |
|--|--|--|
| Levenshtein Distance (Char.) | 11 | 33 |
| Levenshtein Distance (Words) | 9 | 23 |
| Word Error Rate (WER in %) | 5.202 | 13.294 |
| Char. Error Rate (CER in %) | 1.038 | 3.116 |
| Word Accuracy (Wacc in %) | 94.797 | 86.705 |
| Hits | 1048 | 1028 |
| Substitutions | 10 | 24 |
| Deletions | 1 | 7 |
| Insertions | 0 | 2 |
| Total char. in reference | 1059 | 1059 |
| Total char. in prediction | 1058 | 1054 |

###### Observations
The MW only miss the reference by one, while the MO did it by five less characters. The MW has few substitutions which cause a WER of 5%. The MO's is higher, with 13%, due to more substitutions, but also deletions and insertions that were not here in the result of the MW. The errors of the MO come from the uppercase at the beginning of the page, as well as few others present in the rest of the page. The MW also struggled with the uppercases of the beginning of the letters, as well as some double letters where it got one of them correctly but not the other.

##### Letter 1000 Page 3

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.a3692c2y/a345f2cdf6d9367ebc1d1a7b02ce458605164ff7" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.a3692c2y/a345f2cdf6d9367ebc1d1a7b02ce458605164ff7" width="150" title="Letter 1000 page 3"></a></figure>

###### Results

|  | Model War | Model Other |
|--|--|--|
| Levenshtein Distance (Char.) | 8 | 6 |
| Levenshtein Distance (Words) | 8 | 4 |
| Word Error Rate (WER in %) | 2.807 | 1.403 |
| Char. Error Rate (CER in %) | 0.477 | 0.357 |
| Word Accuracy (Wacc in %) | 97.192 | 98.596 |
| Hits | 1669 | 1671 |
| Substitutions | 7 | 6 |
| Deletions | 1 | 0 |
| Insertions | 0 | 0 |
| Total char. in reference | 1677 | 1677 |
| Total char. in prediction | 1676 | 1677 |

###### Observations
The MW and MO did both very well on this transcription and here, the MO was better than the MW, even though the latter was trained on this image. The CER is pretty low for both and the WER doesn't go above 3% for the MW and 2% for the MO. The problem comes mostly from substitutions. For the MW, it completely messed up the various 'v' at the beginning of words at the start of the letter, as well as some uppercases. For the MO, it put the wrong number of page and then messed up the 'interior' characters of two words. 

##### Letter 1367 Page 1

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.b7dfjchh/c92a343cc47b94e651498dfc3e3366e2f48c6ec8" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.b7dfjchh/c92a343cc47b94e651498dfc3e3366e2f48c6ec8" width="150" title="Letter 1367 page 1"></a></figure>

###### Results

|  | Model War | Model Other |
|--|--|--|
| Levenshtein Distance (Char.) | 19 | 50 |
| Levenshtein Distance (Words) | 18 | 38 |
| Word Error Rate (WER in %) | 6.545 | 13.818 |
| Char. Error Rate (CER in %) | 1.172 | 3.086 |
| Word Accuracy (Wacc in %) | 93.454 | 86.181 |
| Hits | 1603 | 1574 |
| Substitutions | 14 | 41 |
| Deletions | 3 | 5 |
| Insertions | 2 | 4 |
| Total char. in reference | 1620 | 1620 |
| Total char. in prediction | 1619 | 1619 |

###### Observations
The MO and MW were rather close in their predictions to the reference (by one) but then, they both did a lot of substitutions and few deletions and insertions. The CER is not too high but the errors must have been pretty widespread because the WER is at 6.5% and 14% which is pretty high for those models. The versus indeed shows that almost every character error, whether it is on the MO or the MW, are on a different word. For the MW, the errors came from uppercases but also from pretty random characters, where the substitutions don’t really make any senses. The MO had big trouble in the opener (header, dateline, title and salute) and it completely missed the air quotes at the beginning of some lines, which had not been a problem for the MW. It also struggled with some uppercases. 

##### Letter 844 Page 1

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.bf9ejv49/ff8489bf07604f5fe2727d24b326789ed660428b" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.bf9ejv49/ff8489bf07604f5fe2727d24b326789ed660428b" width="150" title="Letter 844 page 1"></a></figure>

###### Results

|  | Model War | Model Other |
|--|--|--|
| Levenshtein Distance (Char.) | 21 | 40 |
| Levenshtein Distance (Words) | 20 | 32 |
| Word Error Rate (WER in %) | 6.734 | 10.774 |
| Char. Error Rate (CER in %) | 1.213 | 2.312 |
| Word Accuracy (Wacc in %) | 93.265 | 89.225 |
| Hits | 1709 | 1700 |
| Substitutions | 17 | 25 |
| Deletions | 4 | 5 |
| Insertions | 0 | 10 |
| Total char. in reference | 1730 | 1730 |
| Total char. in prediction | 1726 | 1735 |

###### Observations
Both transcriptions are pretty off for their usual results, with a WER of 6 and 10%. However, the prediction length shows that while the MW predicted less characters (minus 4), the MO predicted more (plus 5). Indeed, they both have almost the same number of deletions (4/5) but the MO had 10 insertions while the MW had 0. The MW had trouble with uppercases and similar looking characters (b/p, n/u, c/o). The MO had trouble again in the opener (header, letterhead, dateline and title), it mixed up some similar looking characters and also added some ghost punctuation (commas or hyphen) randomly.

##### Letter 948 Page 1

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.ccb7m46q/b3b5af4d1b0431acb90a27a079c85f99bcea3d97" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.ccb7m46q/b3b5af4d1b0431acb90a27a079c85f99bcea3d97" width="150" title="Letter 948 page 1"></a></figure>

###### Results

|  | Model War | Model Other |
|--|--|--|
| Levenshtein Distance (Char.) | 27 | 59 |
| Levenshtein Distance (Words) | 20 | 35 |
| Word Error Rate (WER in %) | 10.928 | 19.125 |
| Char. Error Rate (CER in %) | 2.423 | 5.296 |
| Word Accuracy (Wacc in %) | 89.071 | 80.874 |
| Hits | 1089 | 1059 |
| Substitutions | 16 | 45 |
| Deletions | 9 | 10 |
| Insertions | 2 | 4 |
| Total char. in reference | 1114 | 1114 |
| Total char. in prediction | 1107 | 1108 |

###### Observations
The prediction of MW is not really good (less than 90% of accuracy) and the prediction of MO is pretty bad (only 80% of accuracy). The CER of the MO is also one of the highest of all prediction (5%; third highest). It has a lot of substitutions (45) and few deletions and insertions. The MW also have some big number for a model trained on its own set, with 16 substitutions and 9 deletions. This seems to be due to the title of the opener, which is pretty long and made of a lot of uppercases, with which both models struggled with, the MO more than the MW, since the MW is comprehensible except for the last names and the MO is just gibberish. The MW deleted some characters and punctuations and struggled with few uppercases. The MO mixed up some similar characters and completely missed the 'K' present in the page.

##### Conclusion/General observations
In conclusion, with this test set, we can observe that the problem of the MW is not limited to the other set. This can reinforce the idea that the problem come from the quantity gap of both sets. Trained with more content, the MW might be more effective, in its own set or with others. The MO wasn't too bad considering that it was trained on a different set with a different lexicon. The main observation is that the training might lack openers and other kind of content where there are specific characters such as uppercases and numbers.

### New results: Model War Retrained
The MW has been retrained on its own data, in order to double the input and to see if it becomes more effective or if it will just be overfitted on the SW and doesn't improve on the SO.

#### General
###### Results

|  | Set Other/Model War Retrained | Set War/Model War Retrained  |
|--|--|--|
| Levenshtein Distance (Char.) | 3768 | 197 |
| Levenshtein Distance (Words) | 2512 | 174 |
| Word Error Rate (WER in %) | 15.15 | 2.66 |
| Char. Error Rate (CER in %) | 3.76 |0.51 |
| Word Accuracy (Wacc in %) | 84.85 | 97.34 |
| Hits | 96697 | 38819 |
| Substitutions | 3031 | 144 |
| Deletions | 461 | 41 |
| Insertions | 276 | 12 |
| Total char. in reference | 100189 | 39004 |
| Total char. in prediction | 100004 | 38975 |

###### Observations
In the matter of the prediction, the MWR did a little better on its own set, by a dozen characters, but it diminished for the SO by fifty characters. For the SO, there were a lot more hits (+200) and less substitutions (-230). The deletions did not really vary but there were less insertions (-50) which explains the difference in the prediction. The accuracy only improves by one point which is not really impacting. For the SW, there were more hits (+161) and less substitutions (-135), deletions (-26) and insertions (-14), which correlates with the length of the prediction. The accuracy improved by two points and the CER is very low. 

#### Results by letters
###### Results

|  | 1358_4 | 607_3 | 607_17 | 722_1 | 1170_3 | 678_1 | 1000_3 | 1367_1 | 844_1 | 948_1 |
|--|--|--|--|--|--|--|--|--|--|--|
| Levenshtein Distance (Char.) | 121 | 19 | 84 | 61 | 55 | 8 | 9 | 13 | 6 | 9 |
| Levenshtein Distance (Words) | 43 | 16 | 62 | 37 | 46 | 7 | 8 | 13 | 7 | 8 |
| Word Error Rate (WER in %) | 64.179 | 6.451 | 15.012 | 24.342 | 17.49 | 4.046 | 2.807 | 4.727 | 2.356 | 4.371 |
| Char. Error Rate (CER in %) | 23.679 | 1.204 | 3.466 | 6.995 | 3.422 | 0.755 | 0.536 | 0.802 | 0.346 | 0.807 |
| Word Accuracy (Wacc in %) | 35.82 | 93.548 | 84.987 | 75.657 | 82.509 | 95.953 | 97.192 | 95.272 | 97.643 | 95.628 |
| Hits | 393 | 1558 | 2344 | 814 | 1553 | 1051 | 1668 | 1607 | 1724 | 1105 |
| Substitutions | 109 | 18 | 63 | 54 | 43 | 7 | 9 | 11 | 4 | 7 |
| Deletions | 9 | 1 | 16 | 4 | 11 | 1 | 0 | 2 | 2 | 2 |
| Insertions | 3 | 0 | 5 | 3 | 1 | 0 | 0 | 0 | 0 | 0 |
| Total char. in reference | 511 | 1577 | 2423 | 872 | 1607 | 1059 | 1677 | 1620 | 1730 | 1114 |
| Total char. in prediction | 505 | 1576 | 2412 | 871 | 1597 | 1058 | 1677 | 1618 | 1728 | 1112 |

###### Observations
* Set Other: For the letter 1358, the MWR has less substitutions and insertions, which lowered the WER by 10 points, but still keeps it below 50% of accuracy. The versus shows that while it still didn't manage to get any surname correctly, it did manage to correctly transcribe more 'Professeur' than before, which would explain the better metrics. For the two pages from the letter 607, the accuracy improved by two points for both of them and the CER barely moved. With the versus, we can see that it usually struggled with the same part of the pages that it did with the MW (uppercases, numbers, specific signs, similar looking letters). For the page 722, the CER lowered a little but there were no changed at all on the WER. It didn't improve on the opener, still had problems with some characters, but sometimes did different substitutions than prior. Finally, the letter 1170 have a slightly lower CER than the MW, which can be explained by the fact that all the hits/substitutions/deletions have the same number but there is one less insertion in the transcription of the MWR, but a higher WER, which could be explain by the fact that one or two more words were changed with the transcription of the MWR.
* Set War: For the letter 678, there was less substitutions (-3) which improved the CER and WER. It notably did better with the opener which is perfectly good this time. For the letter 1000, the WER didn't move, even though there was no deletion this time and more substitutions than with MW. The model still struggles with the uppercase 'V' even though it was not at the same words than before and it got different words than prior wrong. For the letter 1367, the results are better, with a lower CER and WER, less substitutions/insertions/deletions. With the versus, we see that the model has recurring problems (same errors than prior) but also created new errors (with numbers for example) that it did not have last time. For the letter 844, the result is way better than with MW, the CER went from 1,2% to 0,3% and the WER from 6,7% to 2,4%, due mostly to the substitutions going from 17 to 4. It recognizes more words and had less problems in the opener, even though it got the letterhead wrong, which did not with the MW. Finally, the results were also better for the letter 948, which greatly improve, with an accuracy going from 89% to 95,6% and a CER going from 2,4% to 0,8%, due also to less substitutions(-9)/deletions(-7)/insertions(-2). The model still struggles with some elements in the opener but got more rights than prior. It corrected all the errors in the text that it made before, except for two words where it did the same errors than with the MW.

## Conclusion
In conclusion, we can say that the difficulties met by the models trained were due to lack of some content more than a specific vocabulary. There was no pattern of errors links to the absence of some words on the transcription. In the case where the models were wrong, it was mostly due to the absence of enough uppercases in the training (which is a problem I already encountered with my ground truth). In the recognition of the MO or the MW, the unique words of politics or war from the other set were not particularly badly recognized. In my observation, I realize that the errors, other than those from special characters, were coming mostly from similar looking characters (b/p, n/u, c/o, etc.). Since those characters aren't always misrecognized, it might be due to the context, i.e., the characters next to them. In view of that, it might be interested to do an analysis of n-grams and see if we can find a correlation between the misrecognition and the lack of certain series of n-grams.