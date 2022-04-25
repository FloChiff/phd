# Glossary

**Allographétique** : Various ways of writing the same letter from the Latin script, i.e. long s and curve s

**Allography** : Variant grapheme of a letter or a word

**Character Error Rate (CER)** : Count of the minimum number of character-level operations required to transform the ground truth text into the OCR output. \\
Formula: CER = Substitution(s) + Insertion(s) + Deletion(s) / Number of characters in the GT \\
The lower the CER value (with 0 being a perfect score), the better the performance of the OCR model.

**"Gold" corpus** : Data exclusively created and verified by humans, to obtain a perfect transcription

**Ground Truth (GT)** : (Perfect) transcription of a text (usually human-made), that will later be used to train model(s) fitted for the automatic transcription of a corpus/corpora

**Handwritten Text Recognition (HTR)** : Ability of a computer or device to take as input handwriting from sources such as printed physical documents, pictures and other devices, or to use handwriting as a direct input to a touchscreen and then interpret this as text

**Levenshtein distance** : Metric for measuring the difference between two sequences. The Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

**Optical Character Recognition (OCR)** : Electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document or a scene-photo

**"Silver" corpus** : Data acquired by the prediction of the model made from the gold corpus

**Word Error Rate (WER)** : Count of the minimum number of word-level operations required to transform the ground truth text into the OCR output. \\
Formula: WER = Word substitution(s) + Word insertion(s) + Word deletion(s) / Number of words in the GT \\
The value of the WER is usually higher than the CER value