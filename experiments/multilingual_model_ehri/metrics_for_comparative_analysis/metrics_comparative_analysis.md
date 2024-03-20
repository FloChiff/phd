---
layout: post
title: "Metrics for comparative analysis (Multilingual model EHRI)"
date: 2024-03-20
---

## Comparative results for the EHRI NFC model (normal)

|  | English 1 | English 2 | Danish 1 | Danish 2 | Slovak 1 | Slovak 2 | French 1 | French 2 | Italian 1 | Italian 2  |
|--|--|--|--|--|--|--|--|--|--|--|
| Levensthein Distance (Char.) | 48 | 10 | 106 | 14 | 11 | 11 | 67 | 94 | 98 | 21 |
| Levensthein Distance (Words) | 33 | 9 | 73 | 19 | 14 | 13 | 62 | 94 | 75 | 21 |
| Word Error Rate (WER in %) | 9.85 | 2.325 | 39.673 | 8.636 | 10.37 | 6.046 | 13.596 | 20.042 | 20.215 | 11.351 |
| Char. Error Rate (CER in %) | 2.51 | 0.421 | 8.811 | 0.893 | 1.199 | 0.812 | 2.433 | 3.196 | 4.224 | 1.76 |
| Word Accuracy (Wacc in %) | 90.149 | 97.674 | 60.326 | 91.363 | 86.629 | 93.953 | 86.403 | 79.957 | 79.784 | 88.648 |
| Hits | 1867 | 2363 | 1107 | 1557 | 906 | 1343 | 2689 | 2850 | 2226 | 1173 |
| Substitutions | 44 | 7 | 86 | 8 | 7 | 7 | 57 | 83 | 77 | 19 |
| Deletions | 1 | 2 | 10 | 2 | 4 | 4 | 7 | 8 | 17 | 1 |
| Insertions | 3 | 1 | 10 | 4 | 0 | 0 | 3 | 3 | 4 | 1 |
| Total char. in reference | 1912 | 2372 | 1203 | 1567 | 917 | 1354 | 2753 | 2941 | 2320 | 1193 |
| Total char. in prediction | 1914 | 2371 | 1203 | 1569 | 913 | 1350 | 2749 | 2936 | 2307 | 1193 |

## Comparative results for the EHRI NFC model (no punctuation)

|  | English 1 | English 2 | Danish 1 | Danish 2 | Slovak 1 | Slovak 2 | French 1 | French 2 | Italian 1 | Italian 2 |
|--|--|--|--|--|--|--|--|--|--|--|
| Levensthein Distance (Char.) | 39 | 9 | 106 | 11 | 10 | 10 | 62 | 90 | 90 | 18 |
| Levensthein Distance (Words) | 24 | 9 | 73 | 16 | 11 | 13 | 58 | 90 | 68 | 19 |
| Word Error Rate (WER in %) | 7.185 | 2.362 | 39.673 | 7.339 | 8.208 | 6.103 | 12.803 | 19.313 | 18.428 | 10.439 |
| Char. Error Rate (CER in %) | 2.108 | 0.389 | 9.298 | 0.726 | 1.129 | 0.759 | 2.307 | 3.132 | 3.956 | 1.534 |
| Word Accuracy (Wacc in %) | 92.814 | 97.637 | 60.326 | 92.66 | 91.791 | 93.896 | 87.196 | 80.686 | 81.571 | 89.56 |
| Hits | 1814 | 2308 | 1946 | 1509 | 875 | 1307 | 2629 | 2785 | 2190 | 1160 |
| Substitutions | 31 | 3 | 84 | 5 | 6 | 7 | 46 | 61 | 69 | 12 |
| Deletions | 5 | 2 | 10 | 1 | 4 | 3 | 12 | 27 | 16 | 1 |
| Insertions | 3 | 4 | 12 | 5 | 0 | 0 | 4 | 2 | 5 | 5 |
| Total char. in reference | 1850 | 2313 | 1140 | 1515 | 885 | 1317 | 2687 | 2873 | 2275 | 1173 |
| Total char. in prediction | 1848 | 2315 | 1142 | 1519 | 881 | 1314 | 2679 | 2848 | 2264 | 1177 |

