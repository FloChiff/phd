#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: March 2024
- description: Producing lists of n-grams
- output: Python files
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: file with the lists of n-grams
"""

import sys
#Python method that transform a paragraph of text into lines of maximum width of characters
from textwrap import wrap

correct_transcription = ["THE", "BURGENLAND", "JEWS", "BOAT", "On", "1938", "Jewish", "inhabitants", "of", "Kittsee", "and", "AUSTRIA", "from", "starved", "bayonets", "Danube", "Royka", "years", "Jewish", "approached", "saving", "lutely", "Refugees", "£100", "fifty", "No. 56.", "Jødelovgivningen", "Bulgarien", "16.2.1943.", "Ges", "No", "143", "4", "Gennemslag", "Henvisning", "til", "tidligere", "Indberetninger", "Konsulatet", "ifølge", "Forordning", "rigsministeren", "Presse", "Provinsen", "fremgik", "Konsulatets", "Indberetning", "94", "arbejdslø-", "kun", "faa", "Sofia", "gennemfører", "Kommissariatet", "Jødeanliggender", "en", "udvisning", "Hver", "Familie", "en", "Frist", "at", "forlade", "meddeles", "hvilken", "Flytningen", "Jøder", "ikke", "opfylder", "denne", "Forordning", "udvist", "23.000", "denne", "Forordning", "25.000", "kun", "Statsborgere", "kan", "41.000", "10.000", "civilmobiliseret", "Størsteparten", "Vejbygningsarbejder", "Gunnar", "kgl", "Gesandtskab", "Bukarest", "Ved", "Beslaglæggelsen", "foretaget", "paahviler", "Ejendom", "à", "à", "près", "moitié", "emmeés", "paraît", "remontèrent", "où", "y", "à", "Il", "voyage", "arrêta", "à", "a/à", "âgés", "à", "répondirent", "déclarèrent", "voyagaient", "arrivèrent", "au", "environs", "français", "baraques", "mêmes", "que", "Le", "très", "pénible", "lesquels", "qu", "à", "mètres", "être", "paraît", "5ème", "que", "Quant", "à", "recevaient", "pain", "900", "noirâtre", "Il", "très", "ayant", "quelqu", "Ayant", "à", "réfugié", "choisi", "l’", "25ans", "déjà", "frères", "à", "derrière", "complètement", "dégoûté", "réfugié", "qu", "empêcher", "l’", "qu", "chaque", "l’", "indiqua", "être", "qu", "vécut", "une", "annonça", "très", "même", "être", "portés", "Après", "fût", "dûment", "à", "4I7/92", "I6", "marzo", "I943", "XXI", "portato", "oro", "valuta", "sulle", "persone", "sono", "disgraziati", "quali", "può", "veramente", "dire", "han", "occhi", "preoccupazioni", "9.000", "deportandi", "sofferenze", "vengono", "brutalità", "più", "modo", "è", "anche", "mesi", "veniva", "senza pane", "guardie", "adoperano", "ogni", "fruste", "promiscuità", "impossible", "ciò", "sono", "suicidi", "secondo", "donne", "pazzia", "qui", "Macedonia", "è", "però", "grosso", "che", "eseguirla", "essi", "più", "assoluto", "più", "I'll", "vedendo", "autorità", "israelita", "campi", "9", "già", "409", "ulterior", "decisione", "Rappresentante", "Il", "già", "Sicurezza", "è", "1°", "2°", "ebrei", "Reich", "a", "3°", "città", "Prezídiu", "ministerstva", "vnútra", "1891", "minút", "odsú", "Fuchsa", "budú", "zpäť", "dôsledku", "budú", "ďalšie"]
model_ehri = ["EE", "BURGENIANp", "IEys", "POAT", "on", "l0z8", "rewieb", "inhebitante", "og", "Kitteee", "ann", "AUSTBLA", "fron", "staryed", "bavonets", "Danuhe", "Royvka", "vears", "Jewiwh", "apnroached", "saying", "utely", "Refuges", "f100", "fiftyv", "Ho. 26.", "Jødelovivmingem", "mulgsrien", "19.2.1943.", "ces", "Ho", "139", "3", "Genaemslag", "Rerviemning", "ti", "tidligæere", "Dudberetminger", "konsulatév", "ifelge", "Fororchning", "rigeministeren", "Fresse", "Provingem", "frengik", "Konzulatets", "Indberetaing", "3", "artejdsle-", "hun", "fa", "Gofia", "gememférer", "Kommiesariatet", "Jødeanligender", "on", "udvisnine", "Bwer", "Fanilie", "em", "Friet", "et", "forlæde", "medeles", "hvilkon", "Plytningen", "Jeder", "ihle", "ogfylder", "demme", "Fororduiggn", "udwist", "23.00", "demne", "Forordming", "23.00", "hun", "Stataborgere", "kam", "31.000", "10.00", "eivilmobiliseret", "Sterstepartem", "Vejboremimgmarbejder", "Cunmar", "kol", "Gezematsekab", "Zakarest", "ved", "Beslaglaggelsen", "forataget", "pashviler", "Eiendom", "N", "A", "prěs", "moitis", "emmeás", "paraft", "remontörent", "ob", "v", "A", "D", "vovage", "arreta", "a", "sn", "Ægés", "3", "rápondirent", "déclarörent", "vovagaient", "arriverent", "am", "envírons", "francais", "barac hes", "měmes", "due", "le", "trös", "pánible", "lesduels", "du", "a", "mötres", "Stre", "paraft", "S9me", "due", "Ouant", "4", "recevsient", "hain", "0", "noirätre", "I1", "trös", "avant", "quelou", "Avant", "A", "réfugiś", "chdisi", "1", "2Sans", "déja", "freres", "a", "derriere", "completement", "dégoďté", "røfugig", "du", "empScher", "1", "cu", "chadue", "1", "indioua", "Stre", "du", "vácut", "nne", "annonca", "trös", "meme", "etre", "pprtés", "Apres", "füt", "düment", "a", "4II/2", "16", "margo", "L943", "rII", "portsto", "orv", "valnta", "sule", "Persone", "eno", "6lsgrasisati", "cali", "pa", "versæente", "Güire", "her", "ochi", "preocupazioni", "5.000", "deportand", "soferenze", "vensono", "brutalita", "pih", "medo", "5", "gncha", "masi", "kemiva", "gænzansne", "gnardie", "adoperanc", "cgni", "fræste", "promiscuith", "impossibile", "cib", "somo", "saicidi", "seconco", "donme", "pazia", "oni", "Nacedonia", "6", "perb", "srosso", "cohe", "esesnirla", "si", "pic", "ssoluto", "pih", "1.11", "vedezdo", "autorith", "isrselita", "csmpo", "O", "gih", "408", "ulterion", "decisions", "Rapresentante", "I1", "gia", "Siourezza", "e", "19", "26", "sbrei", "Feich", "s", "36", "citta", "Prezýdiu", "minieterstva", "vnutra", "1801", "minut", "odsu", "Ruchsa", "budů", "zpät", "děsledku", "budů", "Galšie"]

#Create lists for each n-grams
list_4grams = []
list_3grams = []
list_2grams = []
#Choose the list to call
for element in correct_transcription:
    ngrams = wrap(element, 4)
    ngrams = str(ngrams)
    list_4grams.append(ngrams)
    ngrams = wrap(element, 3)
    ngrams = str(ngrams)
    list_3grams.append(ngrams)
    ngrams = wrap(element, 2)
    ngrams = str(ngrams)
    list_2grams.append(ngrams)
tetragrams_correct_transcription = "".join(list_4grams)
trigrams_correct_transcription = "".join(list_3grams)
bigrams_correct_transcription = "".join(list_2grams)
list_4grams = []
list_3grams = []
list_2grams = []
for element in model_ehri:
    ngrams = wrap(element, 4)
    ngrams = str(ngrams)
    list_4grams.append(ngrams)
    ngrams = wrap(element, 3)
    ngrams = str(ngrams)
    list_3grams.append(ngrams)
    ngrams = wrap(element, 2)
    ngrams = str(ngrams)
    list_2grams.append(ngrams)
tetragrams_model_ehri = "".join(list_4grams)
trigrams_model_ehri = "".join(list_3grams)
bigrams_model_ehri = "".join(list_2grams)
with open(sys.argv[1], "w") as file_out:
    print(f'Writing to {sys.argv[1]}')
    file_out.write("tetragrams_correct_transcription = " + tetragrams_correct_transcription + "\n")
    file_out.write("trigrams_correct_transcription = " + trigrams_correct_transcription + "\n")
    file_out.write("bigrams_correct_transcription = " + bigrams_correct_transcription + "\n")
    file_out.write("tetragrams_model_ehri = " + tetragrams_model_ehri + "\n")
    file_out.write("trigrams_model_ehri = " + trigrams_model_ehri + "\n")
    file_out.write("bigrams_model_ehri = " + bigrams_model_ehri)