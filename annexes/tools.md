---
layout: page
title: "Tools"
---

##### KaMi App 
KaMi stands for Kraken Model Inspector  
This tool evaluates the success of a transcription task comparing a correct transcription (reference) and a prediction. The results are then the Levenshtein distance of this evaluation, the Word Error Rate (WER), the Character Error Rate (CER), the Word Accuracy (Wacc), as well as some others statistics taken from the Speech Recognition domain.  
KaMi also offers the possibility to ignore some specificities from the transcription to obtain a more accurate analysis. Thus, it is possible to choose to ignore digits, punctuation, diacritics and cases from the transcription. The statistics at the end will be given with and without what was chosen before initializing the comparison. For example, if everything is selected, the statistics given will be one with a complete comparison, no specificities taken into account, then one with the digits ignored, one with the punctuation ignored, etc. and at the end, one with all the options ignored combined.


----------

##### eScriptorium
[https://escriptorium.paris.inria.fr/](https://escriptorium.paris.inria.fr/)  
eScriptorium is a digital text production pipeline for print and handwritten texts using machine learning techniques. Completely open-source and well-documented, it offers multiple ways to work on the transcription of corpora.  
First of all, eScriptorium offers the possibility to import and export many things. The images can be imported in different formats, such as TIFF, JPG or PDF, but also with their IIIF links, provided that the manifest is on hand. In the case where a transcription/segmentation is already available in an ALTO/PAGE XML format, it can also be imported into eScriptorium. Finally, models can be imported into eScriptorium to do segmentation, transcription or training. The interface also allows us to export from it, whether it is the transcription once it is done (in PAGE XML, ALTO XML or text format), the images or the new models. In summary, everything that has been imported can usually be exported right back.  
With eScriptorium, it is possible to do automatic and manual transcription. If a model is available to segment and/or transcribe the corpus, it can be applied to the images after being imported on the interface. Once it is done, it is still possible to modify this transcription manually, as the production of the model (the transcription) is available and modifiable. If no model can be used, eScriptorium also proposes manual transcription, line by line, according to the segmentation of the images. 
Finally, and that might be one of the most important part, with those transcriptions, manual or automatic, eScriptorium can train models for segmentation or text recognition. This training can be done from scratch, with only the ground truth selected for the training, or finetuned, by preselecting an already imported model from eScriptorium to improve its recognition.