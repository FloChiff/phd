
# -*- UTF-8 -*-

"""
- author: Floriane Chiffoleau
- date: April 2022
- description: Cleaning ground truth to obtain a word frequency list
- input: TXT file
- output: CSV file
- usage :
    ======
    python name_of_this_script.py arg1 arg2
    arg1: file with all the groundtruth combined
    arg2: file with the word frequency list
"""

import re
import sys

#List of french stopwords
stopwords = ["-", "a", "à", "â", "abord", "afin", "ah", "ai", "aie", "ainsi", "allaient", "allo", "allô", "allons", "après", "assez", "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "auquel", "aura", "auront", "aussi", "autre", "autres", "aux", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir", "ayant", "b", "bah", "beaucoup", "bien", "bigre", "boum", "bravo", "brrr", "c", "ça", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant", "certain", "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "chacun", "chaque", "cher", "chère", "chères", "chers", "chez", "chiche", "chut", "ci", "cinq", "cinquantaine", "cinquante", "cinquantième", "cinquième", "clac", "clic", "combien", "comme", "comment", "compris", "concernant", "contre", "couic", "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "delà", "depuis", "derrière", "des", "dès", "désormais", "desquelles", "desquels", "dessous", "dessus", "deux", "deuxième", "deuxièmement", "devant", "devers", "devra", "différent", "différente", "différentes", "différents", "dire", "divers", "diverse", "diverses", "dix", "dix-huit", "dixième", "dix-neuf", "dix-sept", "doit", "doivent", "donc", "dont", "douze", "douzième", "dring", "du", "duquel", "durant", "e", "effet", "eh", "elle", "elle-même", "elles", "elles-mêmes", "en", "encore", "entre", "envers", "environ", "es", "ès", "est", "et", "etant", "étaient", "étais", "était", "étant", "etc", "été", "etre", "être", "eu", "euh", "eux", "eux-mêmes", "excepté", "f", "façon", "fais", "faisaient", "faisant", "fait", "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha", "hé", "hein", "hélas", "hem", "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit", "huitième", "hum", "hurrah", "i", "il", "ils", "importe", "j", "je", "jusqu", "jusque", "k", "l", "la", "là", "laquelle", "las", "le", "lequel", "les", "lès", "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lorsque", "lui", "lui-même", "m", "ma", "maint", "mais", "malgré", "me", "même", "mêmes", "merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "moi", "moi-même", "moins", "mon", "moyennant", "n", "na", "ne", "néanmoins", "neuf", "neuvième", "ni", "nombreuses", "nombreux", "non", "nos", "notre", "nôtre", "nôtres", "nous", "nous-mêmes", "nul", "o", "o|", "ô", "oh", "ohé", "olé", "ollé", "on", "ont", "onze", "onzième", "ore", "ou", "où", "ouf", "ouias", "oust", "ouste", "outre", "p", "paf", "pan", "par", "parmi", "partant", "particulier", "particulière", "particulièrement", "pas", "passé", "pendant", "personne", "peu", "peut", "peuvent", "peux", "pff", "pfft", "pfut", "pif", "plein", "plouf", "plus", "plusieurs", "plutôt", "pouah", "pour", "pourquoi", "premier", "première", "premièrement", "près", "proche", "psitt", "puisque", "q", "qu", "quand", "quant", "quanta", "quant-à-soi", "quarante", "quatorze", "quatre", "quatre-vingt", "quatrième", "quatrièmement", "que", "quel", "quelconque", "quelle", "quelles", "quelque", "quelques", "quelqu'un", "quels", "qui", "quiconque", "quinze", "quoi", "quoique", "r", "revoici", "revoilà", "rien", "s", "sa", "sacrebleu", "sans", "sapristi", "sauf", "se", "seize", "selon", "sept", "septième", "sera", "seront", "ses", "si", "sien", "sienne", "siennes", "siens", "sinon", "six", "sixième", "soi", "soi-même", "soit", "soixante", "son", "sont", "sous", "stop", "suis", "suivant", "sur", "surtout", "t", "ta", "tac", "tant", "te", "té", "tel", "telle", "tellement", "telles", "tels", "tenant", "tes", "tic", "tien", "tienne", "tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant", "toujours", "tous", "tout", "toute", "toutes", "treize", "trente", "très", "trois", "troisième", "troisièmement", "trop", "tsoin", "tsouin", "tu", "u", "un", "une", "unes", "uns", "v", "va", "vais", "vas", "vé", "vers", "via", "vif", "vifs", "vingt", "vivat", "vive", "vives", "vlan", "voici", "voilà", "vont", "vos", "votre", "vôtre", "vôtres", "vous", "vous-mêmes", "vu", "w", "x", "y", "z", "zut", "alors", "aucuns", "bon", "devrait", "dos", "droite", "début", "essai", "faites", "fois", "force", "haut", "ici", "juste", "maintenant", "mine", "mot", "nommés", "nouveaux", "parce", "parole", "personnes", "pièce", "plupart", "seulement", "soyez", "sujet", "tandis", "valeur", "voie", "voient", "état", "étions"]

def delete_punctuation(text):
    """ Deleting punctuation marks from the text
    
    :param text: Text to clean
    :type text: str
    :returns: Texte without punctuation
    :rtype: str
    """
    punctuation = "!:;\",?'’.°"
    for marker in punctuation:
        text = text.replace(marker, " ")
    return text

def counting(words): 
    """ Counting the number of occurrences of each word in the text
    
    :param words: Content to count
    :type words: str
    :returns: frequency list
    :rtype: dict
    """ 
    calculation = {}
    for word in words:
        if word not in calculation:
            calculation[word] = words.count(word)
    return calculation

with open(sys.argv[1], 'r') as file_in:
    print("reading from "+sys.argv[1])
    text = file_in.read()

    #Remove elements that can't be taken into account in the frequency list
    text = re.sub(r"- [0-9]{1,} -\n", "", text)
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"[0-9]", "", text)
    text = re.sub(r"X{3,}", "", text)
    text = re.sub("/", "", text)
    text = delete_punctuation(text)
    text = text.replace("££", "")
    text = text.replace("€", "")
    
    #Transform every uppercase letter in lowercase to avoid falsifying the count
    text = text.lower()
    
    #Separate the text word by word
    text = text.split()
    
    #Delete all the stopwords from the text to have a realistic count
    output = [w for w in text if not w in stopwords]
    
    #Generate the frequency list as a dictionary
    out = counting(output)
    
    #Create a Python list that sort the frequency list by decreasing number of occurrences
    sortedDict = sorted(out.items(), key=lambda x: x[1], reverse=True)
    
    #Transform the list into string and delete all elements related to a Python list
    out = str(sortedDict)
    out = re.sub(r"\), \('", "\n", out)
    out = re.sub("', ", "\t", out)
    out = re.sub(r"\[\('|\)\]", "", out)
    
    #Create elements for a CSV file
    out = re.sub(r"\n", '"\n"', out)
    out = re.sub(r"^", '"Word", "Number of occurrences"\n"', out)
    out = re.sub(r"$", '"', out)
    out = re.sub(r"\t", '", "', out)

with open(sys.argv[2],"w", encoding='UTF-8') as file_out:
    print("writing to "+sys.argv[2])
    file_out.write(out)