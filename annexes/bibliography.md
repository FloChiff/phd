---
layout: page
title: "Bibliography"
---

**Assefi, Mehdi. (2016). *OCR as a Service: An Experimental Evaluation of Google Docs OCR, Tesseract, ABBYY FineReader, and Transym*. ISCV. ⟨[Link](https://www.researchgate.net/publication/310645810_OCR_as_a_Service_An_Experimental_Evaluation_of_Google_Docs_OCR_Tesseract_ABBYY_FineReader_and_Transym)⟩**  

In this paper, the authors present different ways to do OCR by doing an evaluation of several systems created for OCR which are Google Docs OCR, Tesseract, ABBYY FineReader and Transym. After explaining quickly what is the point of OCR, they do a rapid presentation of every system chosen and how they operate. They then applied those systems in documents related to healthcare, to see how it would worked and helped in this particular domain. Finally, they experiment on an established dataset of various documents, from noisy images to barcodes to evaluate the efficiency of the systems. In the end, they provide the statistics from this experiment, with the different options tested and the conclusion drawn from it.

----------

**Alix Chagué, Thibault Clérice, Laurent Romary. *HTR-United : Mutualisons la vérité de terrain !*. DHNord2021 - Publier, partager, réutiliser les données de la recherche : les data papers et leurs enjeux, MESHS, Nov 2021, Lille, France. ⟨[hal-03398740](https://hal.archives-ouvertes.fr/hal-03398740)⟩**  

In this paper, the authors present a new way to exploit the ground truth created for the training of text recognition model. After a quick history of OCR, the authors explain the operation of text recognition and the difficulties that can be encountered, helped with illustrations. They then explain the perks of working more with ground truth, without just using it for training but also sharing and documenting them so that they can be reused for other projects. The authors consequently introduce HTR-United, the project they developed from that which is a repository to store those ground trut for reuse purpose. They expose the composition of the repository and the tools developed alongside it to obtain more information from the ground truth (like metrics).

----------

**Balci B., Saadati D., Shiferaw D., *Handwritten Text Recognition using Deep Learning* [http://vision.stanford.edu/teaching/cs231n/reports/2017/pdfs/810.pdf](http://vision.stanford.edu/teaching/cs231n/reports/2017/pdfs/810.pdf)**

In this article, the authors present the work they have done to execute a handwritten text recognition with deep learning, or more exactly a handwritten character recognition as they are using a method of segmentation and recognition where the model learns the character individually and not the word. After a little SOTA about the evolution of automatic recognition, they present the preprocessing thy choose to do as well as the methods they used for vocabulary size, classification, training and segmentation. After giving the results of their experiments, they mention the issue that is handwritten for character recognition and hypothesis that a larger corpus might help them get better results.

----------

**Boschetti, Federico, Matteo Romanello, Alison Babeu, David Bamman, et Gregory Crane. 2009. *Improving OCR Accuracy for Classical Critical Editions*. In Research and Advanced Technology for Digital Libraries, édité par Maristella Agosti, José Borbinha, Sarantos Kapidakis, Christos Papatheodorou, et Giannis Tsakonas, 5714:156‑67. Berlin, Heidelberg: Springer Berlin Heidelberg. [https://doi.org/10.1007/978-3-642-04346-8_17](https://doi.org/10.1007/978-3-642-04346-8_17).**  
In this paper, the authors compared different software used for their classical editions, in Greek and Latin, and the results they obtain. They use equations, regex and outputs to check the accuracy of the OCR software and search which is the best and how to improve everything.

----------

**Eikvil, Line. “*Optical Character Recognition.*” (1993). ⟨[Link](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.25.3684)⟩**  
This work is a complete presentation of OCR. After an introduction to present largely the concept of OCR and an history of the OCR from the moment it was developed to the time of the article production, the author breaks down the operation of OCR, step by step, using schemas to illustrate it. Then, it presents different cases of use of OCR, as well as the systems that are doing OCR and the way to evaluate it. Finally, the author explores the future of OCR, i.e. how to expand it.

----------

**Simon Gabay, Thibault Clérice, Christian Reul. *OCR17: Ground Truth and Models for 17th c. French Prints (and hopefully more).* 2020. ⟨[hal-02577236](https://hal.archives-ouvertes.fr/hal-02577236)⟩**  

In this paper, the authors explore the idea of building a model for a generation of texts : the 17th century prints. They present how they build their corpus, with information about the categories taken into account, the writing periods of different texts and their genre. They also give some precision about the quality of the images that they want, all of this being supported by illustrations and statistics. Then, they explain the rules they established for transcription, i.e. the signs that they consider and did not consider, etc. Finally, they describe their experiments and what resulted from it, which was pretty good. They present the difficulties that they will need to fix to improve the results and the future works that will be done from there.


----------

**B. Gatos et al., "Ground-Truth Production in the Transcriptorium Project," 2014 11th IAPR International Workshop on Document Analysis Systems, 2014, pp. 237-241, doi: [10.1109/DAS.2014.23](https://doi.org/10.1109/DAS.2014.23)**  

In this paper, the author present various ways established to create ground truth fro their project. After introducing HTR and the importance of ground truth, they present the Bentham dataset, their corpus. Then, they explain the methods used to produce text line images and transcripts ground truth, supported by various illustrations. Finally, they expose their first results, the remarks that stem from it and what need to be improved.

----------

**Heliński, Marcin, Milosz Kmieciak and Tomasz Parkola. “Report on the comparison of Tesseract and ABBYY FineReader OCR engines.” (2012). ⟨[Link](https://www.semanticscholar.org/paper/Report-on-the-comparison-of-Tesseract-and-ABBYY-OCR-Heli%C5%84ski-Kmieciak/9d17d059bbc877df1e3921ff39b9b72442dd3458)⟩**  

In this paper, the authors conduct experiments on Tesseract and FineReader OCR engines with a chosen corpus and various sizes of dataset for test ad training. After presenting each tool and their training process, they expose the results of their tests with tables and diagrams. Finally, they conclude with their results, demonstrating that they are not one tool above the other and that the results depends on the pre-processing, noise, glyphs, etc.

----------

**David Juckett, *A method for determining the number of documents needed for a gold standard corpus*, Journal of Biomedical Informatics, Volume 45, Issue 3, 2012, Pages 460-470, ISSN 1532-0464, [https://doi.org/10.1016/j.jbi.2011.12.010](https://doi.org/10.1016/j.jbi.2011.12.010)**  

In this paper, the authors ponder the idea of developing a method to determine the number of documents needed to create a gold corpus, by relying on biomedical documents. After presenting the NLP interest in this procedure, the authors present the corpora, which are dictation letters from pain consultants but also documents from other fields and from English litterature, to broaden the vocabulary. They then present the tools and methods they are going to use and their different results, all of those elements being supported by graphs and equations. In the results, they present the elements that need be more looked at to hope for a proper result. Finally, they discuss the different options used to build the gold corpus and what need to be improve.

----------

**P. Kahle, S. Colutto, G. Hackl and G. Mühlberger, "Transkribus - A Service Platform for Transcription, Recognition and Retrieval of Historical Documents," *2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR)*, 2017, pp. 19-24, doi: [10.1109/ICDAR.2017.307](https://doi.org/10.1109/ICDAR.2017.307)**  

In this paper, the authors are presenting their service platform. After introducing a bit of history behind the creation of the platform, they present the service, that works as a desktop application that needs to be downloaded and installed. Helped by illustrations and diagrams, they expose the options and tools offered by the application. They provide information about the backend, the API and the availability of the source code.

----------

**Kiessling, Benjamin, 2019, "*Kraken - a Universal Text Recognizer for the Humanities*", [https://doi.org/10.34894/Z9G2EX](https://doi.org/10.34894/Z9G2EX), DataverseNL, V2**  

In this paper, the author presents Kraken, the OCR system he developed from OCRopus. The article breaks down the operation of the system. After presenting the interest it holds for humanities, the author explains how it works for recognition, layout analysis and script detection for different languages, with each their own specificities. This demonstration is also supported by illustrations, schemas and statistics.

----------

**B. Kiessling, R. Tissot, P. Stokes and D. Stökl Ben Ezra, "eScriptorium: An Open Source Platform for Historical Document Analysis," *2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)*, 2019, pp. 19-19, doi: [10.1109/ICDARW.2019.10032](https://doi.org/10.1109/ICDARW.2019.10032)**  

In this article, the authors are presenting their platform. After exposing the reasons why they decide to launch this platform (no open source version yet and no interface that works on transcription of manuscripts), they are describing the platform: frontend and backend. They mention the options offered by eScriptorium, illustrated by examples and explain how is it working behind. They underline the fact that it is open source and finally, they present what they hope to do it the future to expand this interface.

----------

**Kim, G., Govindaraju, V. & Srihari, S. An architecture for handwritten text recognition systems. IJDAR 2, 37–44 (1999). [https://doi.org/10.1007/s100320050035](https://doi.org/10.1007/s100320050035)**  

In this paper, the authors expose the system they established to do HTR. After introducing the interest of HTR, they present their steps: image conversion, line separation, normalization, word segmentation, word recognition and linguistic post processing, supported by graphs and schemas. After presenting their results, they ponder on what they can do next to improve this work.

----------

**Lin, Junxia, Ledolter, Johannes. (2021). *A Simple and Practical Approach to Improve Misspellings in OCR Text.* [https://arxiv.org/abs/2106.12030](https://arxiv.org/abs/2106.12030)** 

In this article, the authors work on the identification and correction of non-word errors in OCR text. They start by presenting the various types of OCR errors that can be found, detailing them one after the other and explaining what they are made of. Then, they do the state-of-the-art in OCR misspellings corrections, followed by a presentation of the dataset used for their work and an explaination on the kind of words included in their work. The big part of their article talks about their proposed method, which they detailed in different steps, and the results it shows, which are pretty good according to the authors. 

----------

**U. -. Marti and H. Bunke, "On the influence of vocabulary size and language models in unconstrained handwritten text recognition," Proceedings of Sixth International Conference on Document Analysis and Recognition, 2001, pp. 260-265, doi: [10.1109/ICDAR.2001.953795](https://doi.org/10.1109/ICDAR.2001.953795)**  

In this paper, the authors present an experiment of text recognition on handwritten text that takes into account the size of the vocabulary given to recognize the text. After introducing the steps done to the images and the text to help process it, they present the perplexity results of their experiments. They present the difference between using language models or not and the efficiency of recognition with the vocabulary size. They conclude by insisting on the importance of language models and ways needed to improve it.

----------

**J. Memon, M. Sami, R. A. Khan and M. Uddin, "Handwritten Optical Character Recognition (OCR): A Comprehensive Systematic Literature Review (SLR)," in *IEEE Access*, vol. 8, pp. 142642-142668, 2020, doi: [10.1109/ACCESS.2020.3012542](https://doi.org/10.1109/ACCESS.2020.3012542)**  

First OCR system = 1940 ; the number of publication for HTR/OCR increased in 2002, 2007 and 2009 ; increase in the last two years ; 55 new studies between 2010 and 2017 and 55 between 2017 and 2019. Multiple languages for the studies ; 53 in English, 44 in Arabic ; 37 in Indian, etc. ; for their own works, researchers developed algorithms and techniques at smaller scales.

----------

**T. -T. -H. Nguyen, A. Jatowt, M. Coustaty, N. -V. Nguyen and A. Doucet, "Deep Statistical Analysis of OCR Errors for Effective Post-OCR Processing," *2019 ACM/IEEE Joint Conference on Digital Libraries (JCDL)*, Champaign, IL, USA, 2019, pp. 29-38, doi: [10.1109/JCDL.2019.00015](https://doi.org/10.1109/JCDL.2019.00015).**

In this paper, the authors dig deeper into OCR errors, by presenting the common type of errors, comparing them with common misspelling and analyzing how much they appear within their test sets. They detail five main types of analyses: edit operations, length effects, erroneous characters positions, real-words vs non-words, and word boundary. After presenting it all, they also mix one with another when it occurs in the test sets to push the analysis. The objective is to thorougly observe and search the sets to retrieve the easily and quickly fixable mistakes for an effective post-OCR processing.

----------

**Nguyen, Thi Tuyet Hai, Adam Jatowt, Mickael Coustaty, et Antoine Doucet. 2022. *Survey of Post-OCR Processing Approaches*. ACM Computing Surveys 54 (6):1‑37. [https://doi.org/10.1145/3453476](https://doi.org/10.1145/3453476).**

In this article, the authors mentions the various post-OCR processing approaches that can exist. First, they are doing a little history on OCR and digitization, and the problem that arised with the poor OCR results provided for most of the digitized texts at the time and the consequences it had on tasks such as information retrieval or natural language processing. They reflect on what can be observed and modified in order to fix those issues. The author then explain mathematically what is post-OCR processing problem. The authors started by presenting some projects that used full manual post-OCR processing. Then, the authors mentions semi-automatic approaches, divided in type of approaches. They develop a lot about lexical approaches and error models, which are isolated-word approaches, which mainly is made of error detection and error correction, with list of candidates for correction. They then present other types of models such as feature-based machine learning, string-to-string transformation, and neural machine translation (NMT). Finally, they present the last type of post-ocr processing which focuses on neural networks and language models. In the next part, there are introducing important resources for post-ocr processing that are freely accessible, such as the metrics, that they are explaining thoroughly, the datasets that are used to test and approve the post-ocr tools, which they present in details and the languages resources that can help, which they detailed by language. They end their article by talking about the various evolutions of the methods mentioned all along the paper.

----------

**Plamondon, Réjean, Sargur N. Srihari. *“On-Line and Off-Line Handwriting Recognition: A Comprehensive Survey.”* IEEE Trans. Pattern Anal. Mach. Intell. 22 (2000): 63-84. [https://ieeexplore.ieee.org/document/824821](https://ieeexplore.ieee.org/document/824821)**

This article presents various information about online and offline handwritten recognition. It begins by presenting the various elements of handwritten text recognition, what to look for, how can that work, mostly with the online version. It then presents what constitutes online hanwritten text recognition and the various uses of it. In a second part, it focuses on offline HTR and presents some preprocessing steps that can help with the recognition and then gives examples and study cases of situations where HTR can be used (postal service or signature verification). It finishes by proposing some preprocessing/additional steps to help the recognition such as using word recognizer, n-gram class, lexical techniques, etc.). It concludes by saying that there are good progress in online HTR but it is still mainly in the research area for offline, while hoping that the techniques will improve, in English but also in other languages.

----------

**Reul Christian, Wick Christoph, Noeth Maximilian, Buettner Andreas, Wehner Maximilian, and Springmann Uwe. 2021. "Mixed Model OCR Training on Historical Latin Script for Out-of-the-Box Recognition and Finetuning". In *The 6th International Workshop on Historical Document Imaging and Processing* (*HIP '21*). Association for Computing Machinery, New York, NY, USA, 7–12. DOI:[https://doi.org/10.1145/3476887.3476910](https://doi.org/10.1145/3476887.3476910)**  

In this paper, the authors present their project of building a mixed model for a category of historical printings with polyfonts. After exposing previous works in that area, the authors expose their methodology, training and evaluation data, and their transcription guidelines. Then, they describe the various ways they did their experiments, with one option or another, as well as the errors they mostly encountered. Finally, they present the idea of finetuning the work rather than doing it from scratch, before concluding on those different results and what they can hope to do from there.

----------

**Verónica Romero, Nicolás Serrano, Alejandro H. Toselli, Joan Andreu Sánchez, and Enrique Vidal. 2011. "Handwritten Text Recognition for Historical Documents". In *Proceedings of the Workshop on Language Technologies for Digital Humanities and Cultural Heritage*, pages 90–96, Hissar, Bulgaria. Association for Computational Linguistics**  

In this paper, the authors present the experiments they have done with HTR on historical documents. After an history of HTR and its difference with OCR, the authors describe in details the operation of HTR, step by step, with schemas. Then, before exposing their results, they present the corpora they used, with information about pages, lines and quality of images. Finally, they conclude on what works and what doesn't and what needs to be improve in the future.

----------

**V. Romero, A. H. Toselli, J. A. Sánchez and E. Vidal, "Handwriting Transcription and Keyword Spotting in Historical Daily Records Documents," *2016 12th IAPR Workshop on Document Analysis Systems (DAS)*, 2016, pp. 275-280, doi: [10.1109/DAS.2016.70](https://doi.org/10.1109/DAS.2016.70)**  

In this paper, the authors present the methods they tested to produce a transcription for historical daily records documents. After an introduction where they explain the peculiarity of historical daily records documents in terms of HTR, they presented their corpus. They then explained their different methods used for the transcription (HTR, interactive HTR, KWS). Finally, they present the composition and progress of their experiments, as well as the results with one or the other method. They conclude their paper quite positively, as they notice some encouraging results with some methods.

----------

**Joan Andreu Sánchez, Vicent Bosch, Verónica Romero, Katrien Depuydt, and Jesse de Does. 2014. "Handwritten text recognition for historical documents in the transcriptorium project". In *Proceedings of the First International Conference on Digital Access to Textual Cultural Heritage* (*DATeCH '14*). Association for Computing Machinery, New York, NY, USA, 111–117. DOI:[https://doi.org/10.1145/2595188.2595193](https://doi.org/10.1145/2595188.2595193)**  

In this paper, the authors are presenting their project which aims at performing HTR on historical documents. After a brief history of their project and HTR, as well as a presentation of HTR technology, they expose the collections that they selected to do those experiments. As their collection are in different languages, they describe the issues and specificities they encountered while experimenting. Then, they present the content of their experiments, as well as the results, illustrating it with diagrams, statistics and images. Finally, they discuss what went wrong and what can be improve and they conclude on a positive note, considering the technology that they used as the right one, even though they still think that it might need improvements.

----------

**R. Smith, "An Overview of the Tesseract OCR Engine," *Ninth International Conference on Document Analysis and Recognition (ICDAR 2007)*, 2007, pp. 629-633, doi: [10.1109/ICDAR.2007.4376991](https://doi.org/10.1109/ICDAR.2007.4376991)**  

In this paper, the author presents in details the OCR system Tesseract. After a brief history of its creation, he does a step by step presentation of the way it runs and the results obtained from it.

----------

**Springmann, U., Reul, C., Dipper, S., and Baiter, J., “Ground Truth for training OCR engines on historical documents in German Fraktur and Early Modern Latin”, *arXiv e-prints*, 2018. doi: [10.48550/arXiv.1809.05501](https://doi.org/10.48550/arXiv.1809.05501)**  

In this article, the authors expose the datasets they worked on to obtain models for German Fratkur and Early Modern Latin corpus. After a quick introduction on OCR, the authors presents one by one the content of each of their ground truth corpora, providing illustration of the writing mentioned and information about the number of lines for each part of the dataset. The authors also mention the specificities presented by German Fraktur for the training of a model and how to respond to it. Finally, they describe the rules they have to follow to transcribe their ground truth to help with the subsequent OCR of other corpora.

----------

**Srivastava, Nitish, Geoﬀrey Hinton, Alex Krizhevsky, Ilya Sutskever, et Ruslan Salakhutdinov. 2014. *Dropout: A Simple Way to Prevent Neural Networks from Overﬁtting*. Journal of Machine Learning Research 15 (2014) 1929-1958. [https://jmlr.org/papers/v15/srivastava14a.html](https://jmlr.org/papers/v15/srivastava14a.html).**
In this paper, the authors present the idea of dropout, how does it, in what cases and what is it useful. They also explain the way to use it with different inputs. In the article, we can found mentions of much software, definitions (such as regularization, overfitting, nets, neural networks, etc.) and description of how to proceed to create dropout.

----------

**Phillip Benjamin Ströbel, Simon Clematide, and Martin Volk. 2020. "How Much Data Do You Need? About the Creation of a Ground Truth for Black Letter and the Effectiveness of Neural OCR". In *Proceedings of the 12th Language Resources and Evaluation Conference*, pages 3551–3559, Marseille, France. European Language Resources Association**  

In this paper, the authors are doing experiments to determine the quantity of ground truth necessary to obtain an efficient model for the specific case of black letter corpus (sort of a German Fraktur font). After exposing the specificities present in those kinds of corpora and the previous work done with OCR/HTR systems to improve model quality of those corpora, the authors present their ground truth, as well as the OCR systems chosen for the experiments. Then, they expose the various experiments they did, the goal of the experiments and the results, presenting in details of the operation worked and the differences from one system to another, illustrated by table of statistics and images. Finally, they draw their conclusion on systems efficiency and ground truth size for a good model.

----------

**Jean-Baptiste Tanguy. Exploiter des modèles de langue pour évaluer des sorties de logiciels d’OCR pour des documents français du XVIIe siècle. *6e conférence conjointe Journées d'Études sur la Parole (JEP, 33e édition), Traitement Automatique des Langues Naturelles (TALN, 27e édition), Rencontre des Étudiants Chercheurs en Informatique pour le Traitement Automatique des Langues (RÉCITAL, 22e édition). Volume 3 : Rencontre des Étudiants Chercheurs en Informatique pour le TAL*, Jun 2020, Nancy, France. pp.205-217. ⟨[hal-02786201v3](https://hal.archives-ouvertes.fr/hal-02786201)⟩**  

In this paper, the author conducts experiments to see if he can evaluate OCR outputs without using ground truth.  After presenting the difficulties that ground truth represents, he expose various ways to estimate the quality of the OCR output. He then presents his experiments (the corpus, the process, the results), as well as the different metrics he used. Finally, helped by his results presented with tables, he concludes that he cannot validate nor deny his hypothesis, as he lacks enough data to have sufficient results.

----------
