# Model testing April 2022

First batch of test to see if my hypothesis that the vocabulary plays a part on the efficiency of the transcription model can be verified.

The test sample is composed of 14 letters, spanning from 1920 to 1923, and that makes 43 pages in total.  
It is equally divided between letters that talks about the events of the war or something related to it and letters that talks about literally anything else, like family life or politics.


| War | Other subjects |
|--|--|
| Letter 617 | Letter 722 |
| Letter 678 | Letter 753 |
| Letter 948 | Letter 846 |
| Letter 957 | Letter 1029 |
| Letter 1000 | Letter 1103 |
| Letter 1364 | Letter 1170 |
| Letter 1367 | Letter 1217 |


## Results from the KaMi App

The automatic transcription has been done with a model trained on more than 300 pages of ground truth from the PEC corpus with an accuracy of 93,78%.

|  | Levensthein Distance (Char.) | Levensthein Distance (Char.)* | Levensthein Distance (Words) | Levensthein Distance (Words)* | WER (%) | WER (%)* | CER (%) | CER (%)* | Word Accuracy (%) | Word Accuracy (%)* |
|--|--|--|--|--|--|--|--|--|--|--|
| ***Letter 617*** (3 pages) | 115 | 73 | 94 | 49 | 15,93 | 8,57 | 3,32 | 2,24 | 84,1 | 91,43 |
| ***Letter 678*** (2 pages) | 46 | 36 | 44 | 23 | 17,05 | 9,16 | 2,85 | 2,33 | 82,95 | 90,84 |
| Letter 722 (2 pages) | 53 | 41 | 36 | 29 | 14,06 | 11,65 | 3,41 | 2,75 | 85,94 | 88,35 |
| Letter 753 (3 pages) | 107 | 81 | 87 | 65 | 18,12 | 13,8 | 3,7 | 2,92 | 81,88 | 86,2 |
| Letter 846 (3 pages) | 98 | 69 | 76 | 50 | 15,32 | 10,18 | 3,21 | 2,36 | 84,68 | 89,82 |
| ***Letter 948*** (4 pages) | 184 | 157 | 131 | 103 | 20,5 | 16,35 | 4,76 | 4,23 | 79,5 | 83,65 |
| ***Letter 957*** (4 pages) | 171 | 131 | 140 | 89 | 15,01 | 9,75 | 2,92 | 2,35 | 84,99 | 90,25 |
| ***Letter 1000*** (5 pages) | 122 | 77 | 119 | 56 | 10,24 | 4,93 | 1,74 | 1,16 | 89,76 | 95,07 |
| Letter 1029 (3 pages) | 78 | 58 | 60 | 42 | 11,65 | 8,32 | 2,41 | 1,86 | 88,35 | 91,68 |
| Letter 1103 (2 pages) | 69 | 54 | 55 | 41 | 16,77 | 12,81 | 3,47 | 2,87 | 83,23 | 87,19 |
| Letter 1170 (4 pages) | 131 | 112 | 123 | 85 | 14,32 | 10,04 | 2,44 | 2,19 | 85,69 | 89,97 |
| Letter 1217 (4 pages) | 173 | 124 | 140 | 81 | 15,52 | 9,35 | 3,13 | 2,39 | 84,48 | 90,65 |
| ***Letter 1364*** (2 pages) | 50 | 40 | 44 | 31 | 11,83 | 8,61 | 2,22 | 1,87 | 88,17 | 91,39 |
| ***Letter 1367*** (2 pages) | 161 | 138 | 84 | 72 | 18,97 | 16,67 | 5,97 | 5,39 | 81,04 | 83,33 |

\*Diacritics, digits, cases and punctuation have been ignored.
