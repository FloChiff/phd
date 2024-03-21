---
layout: page
title: "Dataset (EHRI)"
date: 2024-03-21
---

1. [A bit of context](https://flochiff.github.io/phd/dataset/ehri/dataset.html#a-bit-of-context)
2. [Description of the source](https://flochiff.github.io/phd/dataset/ehri/dataset.html#description-of-the-source)
3. [Presentation of the dataset](https://flochiff.github.io/phd/dataset/ehri/dataset.html#presentation-of-the-dataset)
    1. [General dataset](https://flochiff.github.io/phd/dataset/ehri/dataset.html#general-dataset)
    2. [Specific pages for analysis](https://flochiff.github.io/phd/dataset/ehri/dataset.html#specific-pages-for-analysis)

## A bit of context
The European Holocaust Research Infrastructure (EHRI) is working on Holocaust archives and how to promote it more to increase researches on the topic. The project consists of 27 partners from across Europe, Israel and the United States, working on one or several work packages dedicated to various stages of the integration of Holocaust archives. As part of my work at Inria, I have been involved in several work packages and I mostly work with their digital editions, in order to help them improve how they are working on or with it, whether they have already been published or are meant to be. 

## Description of the source
When I started working on the editions, there were four available:  

- "[Early Holocaust Testimonies](https://early-testimony.ehri-project.eu/)" (EHT): Written or transcribed oral testimonies on the persecution of the Jews in Nazi Germany;
- "[Von Wien ins Nirgendwo: Die Nisko-Deportationen 1939](https://nisko-transports.ehri-project.eu/)" (Nisko): Testimonies and letters documenting the Nisko Plan, which aimed at creating a Jewish reservation, built by the Jews themselves, in Nisko and Lublin (Poland);
- "[BeGrentze Flucht](https://begrenzte-flucht.ehri-project.eu/)" (BF): Testimonies on the forced emigration of the Jewish population of Austria after its annexation in March 1938, focusing mostly on the situation at the Czechoslovakian border;
- "[Diplomatic Reports](https://diplomatic-reports.ehri-project.eu/)" (DR): Reports written by foreign diplomats stationed in Nazi Germany to their respective Ministry of Foreign Affairs.

Those editions are made of all types of written documents (printed, handwritten and typescripted) but the majority is typescripted documents, which made it ideal for a model, as the writing will be homogeneous. The documents of the editions are also written in various languages, such as English, French, German, Japanese, Polish, Yiddish, etc., which made it ideal as a dataset for a multilingual model. 

## Presentation of the dataset
### General dataset
For my production of a good multilingual model, I selected only languages with the same basic alphabet, with the exception of several diacritics, which are unique to some languages. The collected dataset includes 252 documents, divided into seven languages which are German, English, Danish, Hungarian, Polish, Slovak and Czech. 

The images and transcriptions were retrieved from the websites of each of the editions. The scans were downloaded from the website and uploaded on eScriptorium. They were then segmented automatically, as no segmentation previously existed. Then, the aligned transcription was added in two ways: 

- First case, the text version was available and it was then added, using the ["Text" panel of eScriptorium](https://escriptorium.readthedocs.io/en/latest/transcribe/#editing-with-the-text-panel), with some tweaking to be sure that the transcription aligned with the segmentation;
- Second case, the only transcription available was a translated version so the transcription had to be made manually.  

The first case happened with German, Hungarian and Polish, which had full transcriptions every time. The second case happened with Danish, which only had translations available, so all 36 images had to be manually transcribed (I was helped in that case by a colleague, Sarah Benière). The rest of the languages was a mix of both: English had some complete and some partial transcriptions; Slovak had some transcriptions which are only partially available; Czech had two unavailable transcriptions.

Here is how the dataset is constituted:

| Language | Collection | Documents | Lines | ATR model accuracy |
| :---: | :---: | :---: | :---: | :---: |
| German | BF; Nisko; EHT | 56 | 2287 | 97.9% |
| English | BF; EHT; DR | 54 | 1989 | 97.5% |
| Czech | BF; EHT | 46 | 1713 | 96.7% |
| Danish | DR | 36 | 1007 | 97.8% |
| Hungarian | EHT | 30 | 1334 | 95.7% |
| Polish | EHT | 15 | 468 | 93.1% |
| Slovak | BF | 15 | 395 | 93.7% |
| Multilingual | BF; Nisko; DR; EHT | 252 | 9193 | 97.2% |

In this table, I mentioned each language of the dataset, the collections from which the documents came from, the number of documents and lines, as well as the accuracy that I obtained for the models I developed. As can be observed, there are two truly dominant languages (German and English). It is mostly due to the fact that they are found in the majority of collections. Then, there are three more or less important languages (Danish, Hungarian and Czech) and, finally, two rather limited languages in terms of quantity (Polish and Slovak).

The extent of this dataset can be found in a dedicated repository, containing the training data, as well as the various models that were trained with it: [https://github.com/FloChiff/ehri-dataset](https://github.com/FloChiff/ehri-dataset)


### Specific pages for analysis
As previously said, the dataset was used to generate a multilingual model. To test this model and its efficacy, I choose to select some documents, from the editions mentioned above but not always from the general dataset.  

Here are the ten documents I selected:

<figure style="text-align: center;">
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/danish_1_EHRI-DR-19430528-DK.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/danish_1_EHRI-DR-19430528-DK.jpg" width="120" title="Danish 1"/></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/danish_2_EHRI-DR-19420615-DK_04.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/danish_2_EHRI-DR-19420615-DK_04.jpg" width="120" title="Danish 2" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/english_1_EHRI-BF-19380805.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/english_1_EHRI-BF-19380805.jpg" width="120" title="English 1" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/english_2_EHRI-BF-19380509b_EN_02.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/english_2_EHRI-BF-19380509b_EN_02.jpg" width="120" title="English 2" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/french_1_EHRI-ET-WL16560633.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/french_1_EHRI-ET-WL16560633.jpg" width="120" title="French 1" /></a></figure>
<figcaption style="text-align: center;">From left to right: Danish 1 (DR) and 2 (DR), English 1 (BF) and 2 (BF), French 1 (EHT).</figcaption>

<figure style="text-align: center;"><a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/french_2_EHRI-ET-WL16560633.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/french_2_EHRI-ET-WL16560633.jpg" width="120" title="French 2" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/italian_1_EHRI-DR-19430316-IT.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/italian_1_EHRI-DR-19430316-IT.jpg" width="120" title="Italian 1" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/italian_2_EHRI-DR-19411007-IT.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/italian_2_EHRI-DR-19411007-IT.jpg" width="120" title="Italian 2" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/slovak_1_EHRI-BF-19380906.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/slovak_1_EHRI-BF-19380906.jpg" width="120" title="Slovak 1" /></a>
<a href="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/slovak_2_EHRI-BF-19380421e_SK_05.jpg" target="_blank"><img src="https://raw.githubusercontent.com/FloChiff/phd/main/dataset/ehri/images/slovak_2_EHRI-BF-19380421e_SK_05.jpg" width="120" title="Slovak 2" /></a></figure>
<figcaption style="text-align: center;">From left to right: French 2 (EHT), Italian 1 (DR) and 2 (DR), Slovak 1 (BF) and 2 (BF).</figcaption>  


There are ten documents, all are typescripted but in five different languages: Danish, English, French, Italian and Slovak. I wanted to have languages that were represented in the dataset, with more or less content - English has the most documents, Slovak has the least and Danish is in between -, as well as two unknown languages, to see how well the model do in such cases. I also thought about compatibility when choosing the language. I saw, in a result from one experiment, that English and Slovak were less compatible, in terms of tokens, than English and Polish. As my goal is to test as much as I can the model, I choose Slovak rather than Polish as the less represented languages.  
I also selected two pages of each, to have more ground for my analysis but also, again, to better test my model. For English and Danish, I selected an image from the dataset, but also one not from it, so that the model can be tested on languages that it knows but not only data that it has already seen. I wanted to do it for all known languages but the content on Slovak is limited in EHRI and the fifteen pages from the dataset were all that existed. For French and Italian, the images are evidently both unknown, as the model was never trained on such languages.  

Those specific pages in their images, text and xml formats can be found [here](https://github.com/FloChiff/phd/tree/main/dataset/ehri).