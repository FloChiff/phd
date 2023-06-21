---
layout: page
title: "Dataset"
date: 2023-06-21
---

1. [A bit of context](https://flochiff.github.io/phd/dataset/dataset.html#a-bit-of-context)
2. [Description of the source](https://flochiff.github.io/phd/dataset/dataset.html#description-of-the-source)
3. [Presentation of the dataset](https://flochiff.github.io/phd/dataset/dataset.html#presentation-of-the-dataset)
    1. [The set "Ground truth"](https://flochiff.github.io/phd/dataset/dataset.html#the-set-ground-truth)
    2. [The sets "War" and "Other"](https://flochiff.github.io/phd/dataset/dataset.html#the-sets-war-and-other)

### A bit of context
In 1914, at the start of World War I, Paul d'Estournelles de Constant, a French diplomat and Senator, begans a regular correspondence with Nicholas Murray Butler, an American diplomat and University President, that would be pursued all through the war, and the following years, and this until 1924, the year of d'Estournelles' death. Some decades after his death, his daughter donated his papers, and everything he produced during his long life as a politician and a diplomat, to the Departmental Archives of his district, with a free access to it. Recently, this correspondence became a subject of interest for some historians, with the goal to make it available to a large audience by transcribing, encoding and publishing it. This became a reality with the DAHN project, that dedicated a huge part of its tasks to do just that. 

### Description of the source
This correspondence is made of 1500 letters, with a variation of pages, from 1 to 50 sometimes. It is written in French and with a typewriter, which means the letters are made of straight and regular lines with characters always written the same way, except for minor instances of handwritten notes or corrections. The letters also follows a pattern in its structure, since the first page always starts with a letter numbering, a letterhead, a dateline, a title and a salute, as well as an address at the end of the page. For the last page, it sometimes differs but usually, there are a salute (goodbye), a signature and an address again.  
As of now, the letters 1 to 9bis and 101 to 1050 have been digitized and are available on a IIIF server, more precisely on Nakala, in this [collection](https://nakala.fr/collection/10.34847/nkl.adeb801d). The letters 1 to 9bis and 101 to 605 have been transcribed, encoded and published online and are available on a website, in this [collection](https://discholed.huma-num.fr/exist/apps/discholed/index.html?collection=pec%2Fcorpus).

### Presentation of the dataset
This corpus is quite large but my dataset is only a portion of it. The dataset can be break down in three: the set "War", the set "Other" and the set "Ground Truth". The first two have been methodically chosen for their content but the third one is more a question of quantity than "quality". 

#### The set "Ground truth"
For the set "Ground truth", the choice was made with the idea of quantity and not much the content, as well as sometimes few specifics typographical elements. Therefore, when collecting documents for this set, I simply choose among the letters from the correspondence that I already transcribed and so were available as data for experiment. As I work in different stages to create and gather those ground truths, it is made of several group of documents, with sometimes some duplicates, as I will explain afterwards. I added documents more and more to obtain a highly accurate model, which was achieved with about 500 pages. Those documents can be found, grouped by folders as reusable ground truth in HTR-United under the name [dahncorpus](https://github.com/HTR-United/dahncorpus/tree/main).  
The three main folders of those groundtruth contains files that are all from letters written between 1914 and 1919, fully segmented and transcribed, and have pretty much the same characteristics: long letters, many lignes per page and mostly straight lines but also narrow tight lines. It also present sometimes specificities such as lists, tables, capital letter words or various writing colours or quality. The last folder and its content were meant to bring more recognition of specificities to the model: it contains only chunk of texts or unique words that have capital letters, numbers, titles, recurring elements, handwritten elements or narrow tight part of texts. This explains why there are some duplicates between this folder and the other three, as I tried to get more representation of rare parts of text. It is the case for six pages: 

- letter 473 page 1;
- letter 559 page 7;
- letter 562 page 11;
- letter 571 page 1;
- letter 573 annex page 1;
- letter 585 page 1.

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.2cf0gw32/d58d6dc3b09180adf63c5c65226724fe056fd342" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.2cf0gw32/d58d6dc3b09180adf63c5c65226724fe056fd342" width="210" justify="center" title="Letter 6 page 6" style="padding: 0.2em;"></a><a href="https://api.nakala.fr/data/10.34847/nkl.a4f1o06d/967a06596543d489f45ea6505670f07c69610713" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.a4f1o06d/967a06596543d489f45ea6505670f07c69610713" width="210" justify="center" title="Letter 396 annex page 2" style="padding: 0.2em;"></a><a href="https://api.nakala.fr/data/10.34847/nkl.357bln78/626bb013249feb117287c7a2ec2d244d35c9515b" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.357bln78/626bb013249feb117287c7a2ec2d244d35c9515b" width="210" justify="center" title="Letter 473 page 1" style="padding: 0.2em;"></a><figcaption>Examples from left to right: letter page with straight and regular lines (letter 6 page 6), letter page with many narrow lines and some capital letters (letter 396 annex page 2), and double use of a letter page, as it contains a signicant number of capital letters while also being the first page of a letter from the ground truth (letter 473 page 1)</figcaption></figure>

#### The sets "War" and "Other"
If the set "Ground Truth" was made primarly to help transcribe the rest of the collection and then, was used for some of the experiments, which explains the fact that its content is pretty random, the sets "War" and "Other" were built exclusively for the experiments I planned to further my research on my subject thesis. As my first experiments were centered on lexical analysis, I chose to select content-oriented letters from the collection, divided in two themes: war and "other". Another important difference between the previously presented set and those ones is the fact that they are not coming from the same time of writing at all. The set "Ground Truth" contains letters written between 1914 and 1919, so mainly during the heat of the war, while the new sets contains letters written afterwards, between 1920 and 1924, when the war is over and France and the rest of the world are going back to normal. Therefore, when choosing among those letters, the goal was to have a set of documents where the main subject was affairs of war, so that it would contain a specific vocabulary and another set where war would not be mentioned at all, or barely, to provide other vocabularies. This set is called "Other" to differentiate it from "War" and also because the content of the documents is very diversified, going from affairs of politics to stories about his family, as well as life in post-WWI France.  

Both sets contain the same amount of letters (9) but not the same number of pages: the set "Other" contains 76 pages, while the set "War" only has 31, which could be explained by the fact that the war is not a main topic anymore and even though it is still mentioned in letters, it is usually only a few lines but not a dedicated letter to the subject. Therefore, finding documents where the main subject is affairs of war was a struggle and I only managed to get short letters.  

Now, here is a table summing up important information about the content of the two sets

| Document | Set | Number of pages | Date | Topics |
|--|--|--|--|--|
| Letter 607 | Other | 38 | 1920-01-12/13 | Elections |
| Letter 617 | War | 3 | 1920-02-04 | Treaties and war actions |
| Letter 678 | War | 2 | 1920-06-03 | Trials and war |
| Letter 722 | Other | 2 | 1920-11-18 | Colleague life |
| Letter 753 | Other | 3 | 1920-12-23 | Family mariage |
| Letter 844 | War | 5 | 1921-06-18 | War memorials and ceremonies |
| Letter 846 | Other | 3 | 1921-06-20 | Diplomacy and theater |
| Letter 927 | War | 4 | 1921-12-09 | Military occupation |
| Letter 948 | War | 4 | 1921-12-20 | War memorials and ceremonies |
| Letter 957 | War | 4 | 1921-12-25 | Armaments of war |
| Letter 1000 | War | 5 | 1922-01-23 | Summary of the war correspondence |
| Letter 1029 | Other | 3 | 1922-02-20 | Carnegie project |
| Letter 1103 | Other | 2 | 1922-06-12 | Family relations |
| Letter 1170 | Other | 4 | 1922-10-21 | Religion and populations |
| Letter 1217 | Other | 4 | 1922-12-14 | Cost of post-war life |
| Letter 1358 | Other | 17 | 1923-07-18 | Work obligations |
| Letter 1364 | War | 2 | 1923-07-30 | German sentiment |
| Letter 1367 | War | 2 | 1922-08-03 | Post-war Germany |

For most of my experiments, I am using the sets in their entirety, by studying their composition, their words, etc. However, for some results, I also want to be more precise and to present concrete evidence of what I am defending. For those cases, I choose five pages from each sets to provide visual proof. Similarly to what I did for the set "Ground truth" some are standard letter pages with regular line of texts while others also contains specificities to see results of models in case of peculiar pages.

For the set "War", the specific study is made on:

- Letter 678 Page 1;
- Letter 844 Page 1;
- Letter 948 Page 1;
- Letter 1000 Page 3;
- Letter 1367 Page 1.

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.a3692c2y/a345f2cdf6d9367ebc1d1a7b02ce458605164ff7" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.a3692c2y/a345f2cdf6d9367ebc1d1a7b02ce458605164ff7" width="300" justify="center" title="Letter 1000 page 3" style="padding: 0.2em;"></a><a href="https://api.nakala.fr/data/10.34847/nkl.b7dfjchh/c92a343cc47b94e651498dfc3e3366e2f48c6ec8" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.b7dfjchh/c92a343cc47b94e651498dfc3e3366e2f48c6ec8" width="300" justify="center" title="Letter 1367 page 1" style="padding: 0.2em;"></a><figcaption>Examples from left to right: standard page with regular lines of text (letter 1000 page 3), page with a long paragraph of narrow and crowded lines (letter 1367 page 1).</figcaption></figure>

For the set "Other", the specific study is made on:

- Letter 607 Page 3;
- Letter 607 Page 17;
- Letter 722 Page 1;
- Letter 1170 Page 3;
- Letter 1358 Page 4.

<figure><a href="https://api.nakala.fr/data/10.34847/nkl.8991xkm4/72b5373146096b82d2279f0d6ba56a8e3736f918" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.8991xkm4/72b5373146096b82d2279f0d6ba56a8e3736f918" width="300" justify="center" title="Letter 607 page 3" style="padding: 0.2em;"></a><a href="https://api.nakala.fr/data/10.34847/nkl.bbd715g8/fe7ca9dd778be186ccae7b88f6b22937855c8473" target="_blank"><img src="https://api.nakala.fr/data/10.34847/nkl.bbd715g8/fe7ca9dd778be186ccae7b88f6b22937855c8473" width="300" justify="center" title="Letter 1358 page 4" style="padding: 0.2em;"></a><figcaption>Examples from left to right: standard page with regular lines of text (letter 607 page 3), page full of capital letters (letter 1358 page 4).</figcaption></figure>