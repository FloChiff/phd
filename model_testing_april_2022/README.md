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


|  | Levensthein Distance (Char.) | Levensthein Distance (Char.)* | Levensthein Distance (Words) | Levensthein Distance (Words)* | WER (%) | WER (%)* | CER (%) | CER (%)* | Word Accuracy (%) | Word Accuracy (%)* |
|--|--|--|--|--|--|--|--|--|--|--|
| **Letter 617** | 115 | 73 | 94 | 49 | 15,93 | 8,57 | 3,32 | 2,24 | 84,1 | 91,43 |
| **Letter 678** | 46 | 36 | 44 | 23 | 17,05 | 9,16 | 2,85 | 2,33 | 82,95 | 90,84 |
| Letter 722 |  |  |  |  |  |  |  |  |  |  |
| Letter 753 |  |  |  |  |  |  |  |  |  |  |
| Letter 846 |  |  |  |  |  |  |  |  |  |  |
| **Letter 948** |  |  |  |  |  |  |  |  |  |  |
| **Letter 957** |  |  |  |  |  |  |  |  |  |  |
| **Letter 1000** |  |  |  |  |  |  |  |  |  |  |
| Letter 1029 |  |  |  |  |  |  |  |  |  |  |
| Letter 1103 |  |  |  |  |  |  |  |  |  |  |
| Letter 1170 |  |  |  |  |  |  |  |  |  |  |
| Letter 1217 |  |  |  |  |  |  |  |  |  |  |
| **Letter 1364** |  |  |  |  |  |  |  |  |  |  |
| **Letter 1367** |  |  |  |  |  |  |  |  |  |  |

\*Diacritics, digits, cases and punctuation have been ignored.
