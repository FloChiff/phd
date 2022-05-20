# Model testing April 2022

First batch of test to see if my hypothesis that the vocabulary plays a part on the efficiency of the transcription model can be verified.

The test sample is composed of 18 letters, spanning from 1920 to 1923, and that makes 110 pages in total.  
It is divided between letters that talks about the events of the war or something related to it and letters that talks about literally anything else, like family life or politics.


| War | Other subjects |
|--|--|
| Letter 617 | Letter 607 |
| Letter 678 | Letter 722 |
| Letter 844 | Letter 753 |
| Letter 927 | Letter 846 |
| Letter 948 | Letter 1029 |
| Letter 957 | Letter 1103 |
| Letter 1000 | Letter 1170 |
| Letter 1364 | Letter 1217 |
| Letter 1367 | Letter 1358 |

----------

## Results from the KaMi App

The automatic transcription has been done with a model trained on more than 300 pages of ground truth from the PEC corpus with an accuracy of 93,78%.

|  | Number of pages | Number of lines | Levensthein Distance (Char.) | Levensthein Distance (Char.)* | Levensthein Distance (Words) | Levensthein Distance (Words)* | WER (%) | WER (%)* | CER (%) | CER (%)* | Word Accuracy (%) | Word Accuracy (%)* |
|--|--|--|--|--|--|--|--|--|--|--|--|--|
| Letter 607 |--|--|--|--|--|--|--|--|--|--|--|--|
| ***Letter 617*** | 3 | 65 | 115 | 73 | 94 | 49 | 15,93 | 8,57 | 3,32 | 2,24 | 84,1 | 91,43 |
| ***Letter 678*** | 2 | 36 | 46 | 36 | 44 | 23 | 17,05 | 9,16 | 2,85 | 2,33 | 82,95 | 90,84 |
| Letter 722 | 2 | 35 | 53 | 41 | 36 | 29 | 14,06 | 11,65 | 3,41 | 2,75 | 85,94 | 88,35 |
| Letter 753 | 3 | 53 | 107 | 81 | 87 | 65 | 18,12 | 13,8 | 3,7 | 2,92 | 81,88 | 86,2 |
| ***Letter 844*** |--|--|--|--|--|--|--|--|--|--|--|--|
| Letter 846 | 3 | 57 | 98 | 69 | 76 | 50 | 15,32 | 10,18 | 3,21 | 2,36 | 84,68 | 89,82 |
| ***Letter 927*** |--|--|--|--|--|--|--|--|--|--|--|--|
| ***Letter 948*** | 4 | 76 | 184 | 157 | 131 | 103 | 20,5 | 16,35 | 4,76 | 4,23 | 79,5 | 83,65 |
| ***Letter 957*** | 4 | 107 | 171 | 131 | 140 | 89 | 15,01 | 9,75 | 2,92 | 2,35 | 84,99 | 90,25 |
| ***Letter 1000*** | 5 | 127 | 122 | 77 | 119 | 56 | 10,24 | 4,93 | 1,74 | 1,16 | 89,76 | 95,07 |
| Letter 1029 | 3 | 62 | 78 | 58 | 60 | 42 | 11,65 | 8,32 | 2,41 | 1,86 | 88,35 | 91,68 |
| Letter 1103 | 2 | 39 | 69 | 54 | 55 | 41 | 16,77 | 12,81 | 3,47 | 2,87 | 83,23 | 87,19 |
| Letter 1170 | 4 | 97 | 131 | 112 | 123 | 85 | 14,32 | 10,04 | 2,44 | 2,19 | 85,69 | 89,97 |
| Letter 1217 | 4 | 102 | 173 | 124 | 140 | 81 | 15,52 | 9,35 | 3,13 | 2,39 | 84,48 | 90,65 |
| Letter 1358 |--|--|--|--|--|--|--|--|--|--|--|--|
| ***Letter 1364*** | 2 | 45 | 50 | 40 | 44 | 31 | 11,83 | 8,61 | 2,22 | 1,87 | 88,17 | 91,39 |
| ***Letter 1367*** | 2 | 54 | 161 | 138 | 84 | 72 | 18,97 | 16,67 | 5,97 | 5,39 | 81,04 | 83,33 |

\*Diacritics, digits, cases and punctuation have been ignored.


----------

## Results of the experiments

First of all, two letters seem to not be suited for the test as they have different and bad results compared to the rest of the sample. After observing the versus text and the pages on eScriptorium, it seems that it is due to the quality of the images and their segmentation, which were messy and prevent a good text recognition. This is why, even though their topic is war, those letter will not be taken into consideration for the study as they would be a mislead for the results.
The best example of a good transcription and great results is the letter 1000. It is the longest one from the sample and yet, it has the best WER and CER, with or without the diacritics, punctuation, cases and digits.
We can observe that generally, the CER is way better than the WER with almost ten points of difference from one another. The CER percentage are usually around 2-3% which indicates pretty good results and seems to say that our model have an almost exhaustive databank of characters, which ensures that it is unlikely for it to misrecognize a character.

Here are the results:
#### Best WER
- **Letter 1000 (5 pages)**
- Letter 1029 (3 pages)
- **Letter 1364 (2 pages)**
- Letter 722 (2 pages)
- Letter 1170 (4 pages)

#### Best WER with no diacritics, digits, cases and punctuation
- **Letter 1000 (5 pages)**
- Letter 1029 (3 pages)
- **Letter 617 (3 pages)**
- **Letter 1364 (2 pages)**
- **Letter 678 (2 pages)**

#### Best CER
- **Letter 1000 (5 pages)**
- **Letter 1364 (2 pages)**
- Letter 1029 (3 pages)
- Letter 1170 (4 pages)
- **Letter 678 (2 pages)**

#### Best CER with no diacritics, digits, cases and punctuation
- **Letter 1000 (5 pages)**
- Letter 1029 (3 pages)
- **Letter 1364 (2 pages)**
- Letter 1170 (4 pages)
- **Letter 617 (3 pages)**

