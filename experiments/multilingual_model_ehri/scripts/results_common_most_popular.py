#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: February 2024
- description: Results from the scripts for the most popular tokens
"""

#Number of occurrences: 45
common_2grams  = ['ad', 'ak', 'al', 'an', 'as', 'at', 'da', 'do', 'ed', 'ek', 'el', 'em', 'en', 'er', 'et', 'ie', 'il', 'in', 'is', 'la', 'le', 'li', 'ma', 'me', 'mi', 'mo', 'na', 'ne', 'ni', 'no', 'od', 'om', 'or', 'po', 'ra', 're', 'ro', 'sa', 'si', 'sp', 'st', 'ta', 'te', 'to', 'tr']

#Number of occurrences: 0
common_3grams  = []

#Number of occurrences: 0
common_4grams  = []

#Number of occurrences: 99
hungarian_slovak_2grams  = ['ab', 'ad', 'ak', 'al', 'an', 'ap', 'as', 'at', 'be', 'bo', 'ca', 'ce', 'ch', 'ci', 'da', 'de', 'di', 'do', 'eb', 'ed', 'ek', 'el', 'em', 'en', 'er', 'et', 'ev', 'ez', 'fi', 'ho', 'ia', 'ie', 'il', 'in', 'is', 'it', 'je', 'ka', 'ke', 'ko', 'kr', 'kt', 'ké', 'la', 'le', 'li', 'ln', 'lo', 'lu', 'ly', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ng', 'ni', 'no', 'ná', 'né', 'ní', 'od', 'ok', 'om', 'or', 'os', 'pi', 'po', 'ra', 're', 'ri', 'ro', 'rá', 'sa', 'se', 'si', 'sn', 'so', 'sp', 'st', 'ta', 'te', 'ti', 'tn', 'to', 'tr', 'tv', 'us', 'va', 've', 'vi', 'vo', 'za', 'zn', 'zo', 'át', 'éh']

#Number of occurrences: 4
hungarian_slovak_3grams  = ['kos', 'men', 'nem', 'vel']

#Number of occurrences: 0
hungarian_slovak_4grams  = []

#Number of occurrences: 177
hungarian_english_2grams  = ['Au', 'Be', 'Bi', 'Bu', 'De', 'It', 'Ma', 'Mi', 'Na', 'SS', 'So', 'ab', 'ad', 'ag', 'ai', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'at', 'au', 'ba', 'bb', 'be', 'bl', 'bo', 'ca', 'ce', 'ch', 'ci', 'da', 'de', 'di', 'do', 'dt', 'du', 'ed', 'ei', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'fa', 'fe', 'fi', 'fo', 'ga', 'ge', 'gg', 'gi', 'gl', 'go', 'gr', 'gs', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'hw', 'ia', 'id', 'ie', 'ig', 'il', 'in', 'ir', 'is', 'it', 'jo', 'ju', 'ke', 'ki', 'kn', 'la', 'ld', 'le', 'lg', 'li', 'll', 'lo', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mb', 'me', 'mi', 'mm', 'mo', 'mu', 'na', 'nc', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'nt', 'nu', 'ny', 'od', 'ok', 'ol', 'om', 'on', 'or', 'os', 'ot', 'pa', 'pe', 'pi', 'pl', 'po', 'pp', 'pt', 'pu', 'ra', 'rc', 'rd', 're', 'rg', 'ri', 'rk', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rv', 'sa', 'sc', 'se', 'si', 'so', 'sp', 'ss', 'st', 'ta', 'te', 'th', 'ti', 'tl', 'to', 'tr', 'ts', 'tt', 'tu', 'ud', 'ug', 'ul', 'un', 'us', 'ut', 'va', 've', 'vi', 'vo', 'ye', 'yo', 'ys', 'za', 'ze', 'zi']

#Number of occurrences: 61
hungarian_english_3grams  = ['Aus', 'Min', 'ali', 'anc', 'and', 'ann', 'app', 'att', 'ban', 'bar', 'bel', 'bet', 'bor', 'chw', 'den', 'emb', 'enc', 'ent', 'ere', 'est', 'fol', 'for', 'gen', 'han', 'hel', 'ide', 'ind', 'int', 'itz', 'ker', 'lat', 'les', 'let', 'lev', 'mar', 'mat', 'men', 'mer', 'min', 'mon', 'mun', 'ort', 'par', 'por', 'reg', 'ret', 'sen', 'ste', 'tak', 'tal', 'tar', 'tel', 'tem', 'ten', 'ter', 'tes', 'tin', 'tot', 'tra', 'ver', 'vis']

#Number of occurrences: 6
hungarian_english_4grams  = ['Ausc', 'appe', 'embe', 'hwit', 'ment', 'tran']

#Number of occurrences: 111
hungarian_polish_2grams  = ['Mi', 'Na', 'SS', 'ad', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'au', 'az', 'ba', 'bo', 'ca', 'ch', 'ci', 'da', 'dn', 'do', 'ed', 'eg', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ga', 'go', 'gr', 'ha', 'ia', 'ie', 'ik', 'il', 'in', 'is', 'ja', 'je', 'ju', 'ka', 'ki', 'ko', 'kr', 'kt', 'la', 'le', 'li', 'lk', 'ln', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'nd', 'ne', 'ni', 'nk', 'no', 'nt', 'nu', 'ny', 'od', 'ok', 'ol', 'om', 'on', 'or', 'os', 'ot', 'oz', 'pa', 'pi', 'po', 'ra', 're', 'ro', 'rt', 'rz', 'sa', 'sc', 'si', 'sp', 'st', 'sz', 'ta', 'te', 'tn', 'to', 'tr', 'tt', 'tu', 'ud', 'ug', 'uk', 'us', 'ut', 'za', 'zb', 'ze', 'zi', 'zn', 'zo', 'ób', 'ór']

#Number of occurrences: 7
hungarian_polish_3grams  = ['ali', 'bar', 'eli', 'mag', 'sza', 'tak', 'tam']

#Number of occurrences: 0
hungarian_polish_4grams  = []

#Number of occurrences: 152
hungarian_danish_2grams  = ['Be', 'De', 'Ha', 'Ma', 'Me', 'Mi', 'ab', 'ad', 'ag', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'ba', 'be', 'bl', 'bo', 'ce', 'ci', 'da', 'de', 'di', 'dn', 'do', 'dt', 'eb', 'ed', 'eg', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'fa', 'fe', 'fi', 'fo', 'ga', 'ge', 'gg', 'gi', 'gl', 'gr', 'gs', 'gt', 'ha', 'he', 'hi', 'ho', 'id', 'ie', 'ig', 'ik', 'il', 'in', 'is', 'it', 'jd', 'je', 'jo', 'ka', 'ke', 'kk', 'ko', 'kr', 'kt', 'la', 'ld', 'le', 'lg', 'lh', 'li', 'lk', 'll', 'lo', 'ls', 'lt', 'lv', 'ma', 'me', 'mi', 'mm', 'mo', 'na', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'nt', 'nu', 'ny', 'od', 'og', 'ol', 'om', 'on', 'or', 'pa', 'pe', 'pl', 'po', 'pp', 'ra', 'rb', 'rd', 're', 'rf', 'rh', 'ri', 'rk', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rv', 'sa', 'sc', 'se', 'si', 'so', 'sp', 'ss', 'st', 'sv', 'ta', 'te', 'ti', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'ud', 'ul', 'un', 'ut', 'va', 've', 'vi', 'vo']

#Number of occurrences: 42
hungarian_danish_3grams  = ['and', 'att', 'bet', 'del', 'den', 'dig', 'eli', 'ell', 'els', 'ent', 'ere', 'for', 'gel', 'gen', 'han', 'hel', 'hol', 'ide', 'ind', 'ker', 'kon', 'lag', 'let', 'mel', 'men', 'mer', 'min', 'nem', 'nge', 'ort', 'ren', 'ret', 'sen', 'ste', 'tem', 'ter', 'tes', 'tet', 'tte', 'ver', 'vet', 'vis']

#Number of occurrences: 1
hungarian_danish_4grams  = ['elle']

#Number of occurrences: 193
hungarian_german_2grams  = ['Au', 'Be', 'Bi', 'Bu', 'De', 'Fe', 'Ha', 'Ka', 'Ma', 'Me', 'Mi', 'Na', 'Or', 'SS', 'So', 'Va', 'ab', 'ad', 'ag', 'ah', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'at', 'au', 'ba', 'be', 'bl', 'ce', 'ch', 'da', 'de', 'di', 'dn', 'do', 'dt', 'du', 'eb', 'ed', 'eg', 'ei', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'fa', 'fe', 'fi', 'fo', 'fü', 'ga', 'ge', 'gi', 'gk', 'gl', 'go', 'gr', 'gs', 'gt', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'hw', 'id', 'ie', 'ig', 'ik', 'il', 'in', 'ir', 'is', 'it', 'ja', 'je', 'ju', 'ka', 'ke', 'ki', 'ko', 'kr', 'kt', 'kö', 'la', 'ld', 'le', 'lg', 'li', 'lk', 'll', 'ln', 'lo', 'ls', 'lt', 'lu', 'ma', 'mb', 'me', 'mi', 'mm', 'mo', 'mu', 'na', 'nb', 'nc', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'nt', 'nu', 'nz', 'od', 'ol', 'om', 'on', 'or', 'os', 'ot', 'pa', 'pe', 'pi', 'po', 'pp', 'ra', 'rb', 'rc', 'rd', 're', 'rf', 'rg', 'rh', 'ri', 'rk', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rz', 'rü', 'sa', 'sc', 'se', 'si', 'so', 'sp', 'sr', 'ss', 'st', 'ta', 'te', 'th', 'ti', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tu', 'tz', 'tü', 'ug', 'ul', 'um', 'un', 'us', 'ut', 'va', 've', 'vi', 'vo', 'za', 'ze', 'zi', 'zo', 'zt', 'zu', 'ün']

#Number of occurrences: 66
hungarian_german_3grams  = ['Aus', 'Ber', 'Fen', 'and', 'ann', 'bar', 'ben', 'bet', 'chw', 'del', 'den', 'dig', 'ege', 'ele', 'ell', 'elt', 'emb', 'eng', 'ent', 'ere', 'ert', 'ese', 'ete', 'fol', 'for', 'für', 'gel', 'gen', 'get', 'hal', 'han', 'hat', 'hol', 'ind', 'itz', 'ken', 'ker', 'kon', 'kön', 'lag', 'len', 'let', 'lte', 'mat', 'men', 'mer', 'min', 'neh', 'nge', 'ort', 'ren', 'sem', 'sen', 'sor', 'ste', 'tel', 'ten', 'ter', 'tes', 'tet', 'tra', 'tte', 'tun', 'ver', 'vol', 'von']

#Number of occurrences: 4
hungarian_german_4grams  = ['Ausc', 'este', 'hwit', 'lage']

#Number of occurrences: 207
hungarian_czech_2grams  = ['Be', 'Bi', 'Bu', 'Ha', 'Ka', 'Ma', 'Me', 'Mi', 'Na', 'SS', 'So', 'ab', 'ad', 'ah', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'at', 'au', 'az', 'ba', 'be', 'bl', 'bo', 'bí', 'ce', 'ch', 'ci', 'da', 'de', 'di', 'dn', 'do', 'du', 'dé', 'eb', 'ed', 'ei', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'ez', 'fe', 'fi', 'fo', 'ga', 'ge', 'go', 'gr', 'ha', 'he', 'ho', 'hu', 'há', 'ia', 'id', 'ie', 'ig', 'ik', 'il', 'in', 'is', 'it', 'iu', 'ja', 'je', 'jo', 'já', 'ka', 'ke', 'ko', 'kr', 'kt', 'ká', 'ké', 'la', 'le', 'li', 'lk', 'll', 'ln', 'lo', 'ls', 'lt', 'lu', 'ly', 'lá', 'lé', 'ma', 'me', 'mi', 'mo', 'mu', 'má', 'na', 'nb', 'nc', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'nt', 'nu', 'ny', 'nz', 'ná', 'né', 'ní', 'od', 'ok', 'ol', 'om', 'on', 'or', 'os', 'ot', 'oz', 'pa', 'pe', 'pi', 'pl', 'po', 'pu', 'ra', 'rc', 're', 'rf', 'rg', 'ri', 'rk', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rv', 'rá', 'sa', 'sc', 'se', 'si', 'sn', 'so', 'sp', 'st', 'sv', 'sá', 'sí', 'ta', 'te', 'ti', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tu', 'tv', 'tá', 'té', 'ud', 'uk', 'ul', 'um', 'un', 'us', 'ut', 'va', 've', 'vi', 'vo', 'vá', 'vé', 'ys', 'za', 'zb', 'zd', 'ze', 'zi', 'zn', 'zo', 'zu', 'zá', 'ák', 'ál', 'ám', 'án', 'ás', 'át', 'áz', 'éh', 'én', 'ít']

#Number of occurrences: 47
hungarian_czech_3grams  = ['Mik', 'ala', 'ali', 'and', 'bar', 'blo', 'den', 'eli', 'ent', 'gel', 'gen', 'ház', 'jel', 'ken', 'ker', 'kon', 'kre', 'len', 'les', 'let', 'lág', 'mat', 'men', 'mez', 'min', 'nap', 'nem', 'ném', 'ort', 'por', 'seb', 'ste', 'tak', 'tal', 'tam', 'tek', 'tel', 'tem', 'ten', 'ter', 'tot', 'tov', 'tra', 'val', 'vel', 'vol', 'zás']

#Number of occurrences: 3
hungarian_czech_4grams  = ['blok', 'krem', 'tran']

#Number of occurrences: 96
english_slovak_2grams  = ['Po', 'Ra', 'ab', 'ad', 'ak', 'al', 'an', 'ap', 'as', 'at', 'av', 'be', 'bo', 'br', 'bu', 'by', 'ca', 'ce', 'ch', 'ci', 'ck', 'da', 'de', 'di', 'do', 'ed', 'ek', 'el', 'em', 'en', 'er', 'et', 'ev', 'fi', 'ho', 'ia', 'ic', 'ie', 'il', 'in', 'is', 'it', 'ke', 'la', 'le', 'li', 'lo', 'lu', 'ly', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ng', 'ni', 'no', 'ns', 'ob', 'od', 'ok', 'om', 'op', 'or', 'os', 'ou', 'ov', 'pi', 'po', 'pr', 'ra', 're', 'ri', 'ro', 'sa', 'se', 'si', 'sl', 'sm', 'so', 'sp', 'st', 'ta', 'te', 'ti', 'to', 'tr', 'up', 'us', 'va', 've', 'vi', 'vo', 'za']

#Number of occurrences: 12
english_slovak_3grams  = ['dit', 'ens', 'fin', 'men', 'pol', 'pre', 'pri', 'ria', 'som', 'sta', 'str', 'tre']

#Number of occurrences: 2
english_slovak_4grams  = ['fina', 'poli']

#Number of occurrences: 123
english_polish_2grams  = ['Ja', 'Mi', 'Na', 'Po', 'Pr', 'SS', 'St', 'ac', 'ad', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'au', 'aw', 'ba', 'bi', 'bo', 'br', 'bu', 'by', 'ca', 'ch', 'ci', 'da', 'do', 'dr', 'ec', 'ed', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ga', 'gh', 'go', 'gr', 'ha', 'ia', 'ic', 'ie', 'il', 'im', 'in', 'io', 'is', 'ju', 'ki', 'la', 'le', 'li', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'my', 'na', 'nd', 'ne', 'ni', 'nk', 'no', 'nt', 'nu', 'ny', 'ob', 'oc', 'od', 'ok', 'ol', 'om', 'on', 'op', 'or', 'os', 'ot', 'ow', 'pa', 'pi', 'po', 'pr', 'ra', 're', 'ro', 'rt', 'ry', 'sa', 'sc', 'si', 'sp', 'st', 'ta', 'te', 'to', 'tr', 'tt', 'tu', 'ty', 'uc', 'ud', 'ug', 'up', 'ur', 'us', 'ut', 'wa', 'we', 'wi', 'wn', 'wo', 'wr', 'ws', 'za', 'ze', 'zi']

#Number of occurrences: 14
english_polish_3grams  = ['ach', 'ali', 'ani', 'ant', 'bar', 'bro', 'end', 'ghe', 'nam', 'pra', 'sta', 'sto', 'str', 'tak']

#Number of occurrences: 1
english_polish_4grams  = ['ghet']

#Number of occurrences: 181
english_danish_2grams  = ['Af', 'Al', 'An', 'Ar', 'Be', 'De', 'En', 'Fo', 'Ge', 'He', 'Ho', 'In', 'Ja', 'La', 'Ma', 'Mi', 'Mo', 'No', 'Pe', 'Po', 'Pr', 'Ra', 'Re', 'Se', 'St', 'ab', 'ad', 'ae', 'af', 'ag', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'av', 'ba', 'be', 'bl', 'bo', 'br', 'ce', 'ci', 'da', 'dd', 'de', 'di', 'do', 'dr', 'ds', 'dt', 'ed', 'ef', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'fa', 'fe', 'fi', 'fo', 'fr', 'ft', 'fu', 'ga', 'ge', 'gg', 'gh', 'gi', 'gl', 'gn', 'gr', 'gs', 'ha', 'he', 'hi', 'ho', 'id', 'ie', 'if', 'ig', 'il', 'in', 'io', 'is', 'it', 'iv', 'jo', 'ke', 'la', 'ld', 'le', 'lf', 'lg', 'li', 'll', 'lo', 'ls', 'lt', 'lv', 'ma', 'me', 'mi', 'mm', 'mo', 'na', 'nd', 'ne', 'nf', 'ng', 'ni', 'nk', 'nn', 'no', 'ns', 'nt', 'nu', 'ny', 'od', 'of', 'ol', 'om', 'on', 'op', 'or', 'ov', 'pa', 'pe', 'pl', 'po', 'pp', 'pr', 'ra', 'rd', 're', 'ri', 'rk', 'rl', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rv', 'sa', 'sc', 'se', 'sf', 'si', 'sl', 'sm', 'so', 'sp', 'ss', 'st', 'su', 'ta', 'te', 'ti', 'tl', 'to', 'tr', 'ts', 'tt', 'ty', 'ud', 'ue', 'ul', 'un', 'ut', 'va', 've', 'vi', 'vo']

#Number of occurrences: 85
english_danish_3grams  = ['For', 'Ges', 'Pro', 'Sta', 'all', 'and', 'ans', 'ati', 'att', 'ber', 'bet', 'ble', 'dem', 'den', 'der', 'des', 'det', 'dis', 'end', 'ens', 'ent', 'era', 'ere', 'ern', 'ers', 'for', 'fre', 'gen', 'ges', 'giv', 'han', 'har', 'hav', 'hel', 'her', 'ide', 'ind', 'ing', 'ini', 'ion', 'ist', 'ita', 'iti', 'ive', 'ker', 'lan', 'led', 'let', 'lin', 'man', 'med', 'men', 'mer', 'min', 'ned', 'nin', 'off', 'one', 'ord', 'org', 'ort', 'ove', 'ret', 'sam', 'sen', 'ser', 'ses', 'som', 'son', 'sse', 'sta', 'ste', 'sti', 'sto', 'str', 'tem', 'ter', 'tes', 'tio', 'tru', 'und', 'ven', 'ver', 'vid', 'vis']

#Number of occurrences: 10
english_danish_4grams  = ['Stat', 'fore', 'have', 'ider', 'oner', 'over', 'ster', 'stra', 'tion', 'unde']

#Number of occurrences: 236
english_german_2grams  = ['Al', 'Am', 'An', 'Ar', 'Au', 'Be', 'Bi', 'Bu', 'Ch', 'De', 'Dr', 'Du', 'En', 'Fr', 'Ge', 'Go', 'He', 'Ho', 'In', 'Ja', 'Je', 'Ju', 'La', 'Ma', 'Mi', 'Mo', 'Na', 'Ne', 'No', 'Pa', 'Pe', 'Po', 'Pr', 'Ra', 'Re', 'Ro', 'Ru', 'SS', 'Sc', 'Se', 'So', 'St', 'Th', 'We', 'Wo', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'at', 'au', 'ba', 'be', 'bi', 'bl', 'br', 'bu', 'by', 'ce', 'ch', 'ck', 'da', 'de', 'di', 'do', 'dr', 'ds', 'dt', 'du', 'ec', 'ed', 'ef', 'ei', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'fa', 'fe', 'ff', 'fi', 'fl', 'fo', 'fr', 'ft', 'fu', 'ga', 'ge', 'gi', 'gl', 'go', 'gr', 'gs', 'gu', 'ha', 'he', 'hi', 'hm', 'ho', 'hs', 'ht', 'hu', 'hw', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'il', 'im', 'in', 'io', 'ir', 'is', 'it', 'ju', 'ke', 'ki', 'la', 'ld', 'le', 'lf', 'lg', 'li', 'll', 'lo', 'ls', 'lt', 'lu', 'ma', 'mb', 'me', 'mi', 'mm', 'mo', 'mu', 'na', 'nc', 'nd', 'ne', 'nf', 'ng', 'ni', 'nk', 'nn', 'no', 'ns', 'nt', 'nu', 'ob', 'oc', 'od', 'of', 'ol', 'om', 'on', 'or', 'os', 'ot', 'ow', 'pa', 'pe', 'pi', 'po', 'pp', 'pr', 'ra', 'rc', 'rd', 're', 'rg', 'ri', 'rk', 'rl', 'rm', 'rn', 'ro', 'rr', 'rs', 'rt', 'ru', 'sa', 'sc', 'se', 'sh', 'si', 'sl', 'so', 'sp', 'ss', 'st', 'su', 'ta', 'te', 'th', 'ti', 'tl', 'to', 'tr', 'ts', 'tt', 'tu', 'tw', 'uc', 'ue', 'ug', 'ul', 'un', 'up', 'ur', 'us', 'ut', 'va', 've', 'vi', 'vo', 'wa', 'we', 'wi', 'wo', 'za', 'ze', 'zi']

#Number of occurrences: 140
english_german_3grams  = ['Aug', 'Aus', 'Fra', 'Ger', 'Ges', 'Naz', 'Sch', 'Sta', 'The', 'ach', 'aft', 'age', 'all', 'als', 'and', 'ann', 'ans', 'ant', 'art', 'ass', 'ate', 'aus', 'aut', 'bar', 'bef', 'bei', 'ber', 'bet', 'ble', 'cha', 'che', 'chi', 'chw', 'dem', 'den', 'der', 'des', 'det', 'die', 'dis', 'doc', 'edi', 'emb', 'end', 'ens', 'ent', 'era', 'ere', 'eri', 'ern', 'ers', 'ess', 'fer', 'fin', 'fol', 'for', 'fre', 'gen', 'ges', 'gin', 'gro', 'han', 'has', 'her', 'hin', 'hts', 'ien', 'ili', 'ind', 'ine', 'ing', 'ins', 'ion', 'ist', 'itz', 'ker', 'lan', 'las', 'let', 'lic', 'lin', 'man', 'mat', 'men', 'mer', 'min', 'mit', 'mor', 'mus', 'nat', 'ner', 'not', 'nsp', 'ond', 'ord', 'ori', 'ort', 'pas', 'pro', 'rac', 'rec', 'res', 'rie', 'rig', 'sch', 'sel', 'sen', 'ser', 'ses', 'sin', 'sol', 'son', 'spa', 'sse', 'sta', 'ste', 'sti', 'str', 'suc', 'tap', 'tel', 'ten', 'ter', 'tes', 'tha', 'tie', 'tio', 'tor', 'tra', 'tre', 'tto', 'und', 'unt', 'ver', 'war', 'was', 'wel', 'wer', 'wil', 'wor']

#Number of occurrences: 16
english_german_4grams  = ['Ausc', 'Gest', 'Nazi', 'Ther', 'afte', 'also', 'eren', 'esie', 'hwit', 'lies', 'mber', 'nsta', 'pass', 'spor', 'tion', 'will']

#Number of occurrences: 195
english_czech_2grams  = ['Al', 'Be', 'Bi', 'Bu', 'Ch', 'Dr', 'Fr', 'He', 'Ho', 'In', 'Ja', 'Je', 'La', 'Ma', 'Mi', 'Mo', 'Na', 'Ne', 'Pa', 'Po', 'Pr', 'Ra', 'Ru', 'SS', 'Sc', 'Se', 'So', 'St', 'ab', 'ac', 'ad', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'at', 'au', 'av', 'ba', 'be', 'bi', 'bl', 'bo', 'br', 'bu', 'by', 'ce', 'ch', 'ci', 'ck', 'co', 'da', 'de', 'di', 'do', 'dr', 'du', 'ec', 'ed', 'ei', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'fe', 'fi', 'fo', 'ga', 'ge', 'gh', 'go', 'gr', 'ha', 'he', 'ho', 'hu', 'ia', 'ic', 'id', 'ie', 'ig', 'il', 'in', 'is', 'it', 'iv', 'jo', 'ke', 'la', 'le', 'li', 'll', 'lo', 'ls', 'lt', 'lu', 'ly', 'ma', 'me', 'mi', 'mo', 'mp', 'ms', 'mu', 'my', 'na', 'nc', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'ns', 'nt', 'nu', 'ny', 'ob', 'oc', 'od', 'ok', 'ol', 'om', 'on', 'op', 'or', 'os', 'ot', 'ou', 'ov', 'pa', 'pe', 'pi', 'pl', 'po', 'pr', 'pu', 'ra', 'rc', 're', 'rg', 'ri', 'rk', 'rl', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rv', 'ry', 'sa', 'sc', 'se', 'si', 'sl', 'sm', 'so', 'sp', 'st', 'su', 'ta', 'te', 'ti', 'tl', 'to', 'tr', 'ts', 'tu', 'ty', 'uc', 'ud', 'ul', 'un', 'up', 'ur', 'us', 'ut', 'va', 've', 'vi', 'vo', 'ys', 'za', 'ze', 'zi']

#Number of occurrences: 75
english_czech_3grams  = ['Pro', 'Sch', 'ali', 'and', 'ani', 'aut', 'bar', 'cen', 'ces', 'cha', 'cla', 'dem', 'den', 'ely', 'ens', 'ent', 'ers', 'fin', 'gen', 'ghe', 'gra', 'ice', 'ici', 'ili', 'inf', 'ing', 'ise', 'ist', 'iti', 'ker', 'led', 'les', 'let', 'lin', 'liv', 'man', 'mat', 'men', 'min', 'mus', 'nec', 'ned', 'not', 'nsp', 'ope', 'ori', 'ort', 'pol', 'pop', 'por', 'pos', 'pra', 'pre', 'pro', 'sch', 'sel', 'ses', 'sid', 'sin', 'sta', 'ste', 'sti', 'sto', 'str', 'tak', 'tal', 'tel', 'tem', 'ten', 'ter', 'tot', 'tra', 'ven', 'vid', 'zat']

#Number of occurrences: 10
english_czech_4grams  = ['entr', 'ghet', 'poli', 'pres', 'prov', 'spor', 'star', 'ster', 'stra', 'tran']

#Number of occurrences: 80
slovak_polish_2grams  = ['Po', 'ad', 'aj', 'ak', 'al', 'an', 'as', 'at', 'bo', 'br', 'bu', 'by', 'ca', 'ch', 'ci', 'da', 'do', 'ed', 'ej', 'ek', 'el', 'em', 'en', 'er', 'et', 'ia', 'ic', 'ie', 'il', 'in', 'is', 'je', 'ka', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'ln', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'ob', 'od', 'ok', 'om', 'op', 'or', 'os', 'pi', 'po', 'pr', 'ra', 're', 'ro', 'sa', 'si', 'sk', 'sp', 'st', 'ta', 'te', 'tn', 'to', 'tr', 'up', 'us', 'za', 'zn', 'zo', 'zp']

#Number of occurrences: 8
slovak_polish_3grams  = ['ale', 'mie', 'nic', 'nie', 'pod', 'ran', 'sta', 'str']

#Number of occurrences: 0
slovak_polish_4grams  = []

#Number of occurrences: 89
slovak_danish_2grams  = ['Po', 'Ra', 'ab', 'ad', 'ak', 'al', 'an', 'as', 'at', 'av', 'be', 'bo', 'br', 'ce', 'ci', 'da', 'de', 'di', 'dk', 'do', 'eb', 'ed', 'ej', 'ek', 'el', 'em', 'en', 'er', 'et', 'ev', 'fi', 'hl', 'ho', 'ie', 'il', 'in', 'is', 'it', 'je', 'ka', 'ke', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'lo', 'ma', 'me', 'mi', 'mo', 'na', 'ne', 'ng', 'ni', 'no', 'ns', 'od', 'om', 'op', 'or', 'ov', 'po', 'pr', 'ra', 're', 'ri', 'ro', 'sa', 'se', 'si', 'sk', 'sl', 'sm', 'so', 'sp', 'st', 'ta', 'te', 'ti', 'tn', 'to', 'tr', 'va', 've', 'vi', 'vo']

#Number of occurrences: 7
slovak_danish_3grams  = ['ale', 'ens', 'men', 'nem', 'som', 'sta', 'str']

#Number of occurrences: 0
slovak_danish_4grams  = []

#Number of occurrences: 98
slovak_german_2grams  = ['Br', 'Po', 'Ra', 'ab', 'ad', 'ak', 'al', 'an', 'ap', 'as', 'at', 'be', 'br', 'bu', 'by', 'ce', 'ch', 'ck', 'da', 'de', 'di', 'do', 'eb', 'ed', 'ek', 'el', 'em', 'en', 'er', 'et', 'fi', 'hl', 'ho', 'hr', 'ic', 'ie', 'il', 'in', 'is', 'it', 'je', 'ka', 'ke', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'ln', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ng', 'ni', 'no', 'ns', 'ob', 'od', 'om', 'or', 'os', 'pi', 'po', 'pr', 'ra', 're', 'ri', 'ro', 'sa', 'se', 'si', 'sk', 'sl', 'so', 'sp', 'st', 'ta', 'te', 'ti', 'tn', 'to', 'tr', 'up', 'us', 'va', 've', 'vi', 'vo', 'za', 'zo']

#Number of occurrences: 12
slovak_german_3grams  = ['ens', 'fin', 'ite', 'lov', 'men', 'nic', 'nie', 'ran', 'sta', 'str', 'tis', 'tre']

#Number of occurrences: 1
slovak_german_4grams  = ['oslo']

#Number of occurrences: 147
slovak_czech_2grams  = ['Br', 'Po', 'Ra', 'ab', 'ad', 'aj', 'ak', 'al', 'an', 'ap', 'as', 'at', 'av', 'be', 'bo', 'br', 'bu', 'by', 'bý', 'ce', 'ch', 'ci', 'ck', 'da', 'de', 'di', 'dk', 'do', 'eb', 'ed', 'ej', 'ek', 'el', 'em', 'en', 'er', 'et', 'ev', 'ez', 'fi', 'hl', 'ho', 'hr', 'ia', 'ic', 'ie', 'il', 'in', 'is', 'it', 'ič', 'je', 'jn', 'ka', 'ke', 'ko', 'kr', 'kt', 'ku', 'ké', 'ký', 'la', 'le', 'li', 'ln', 'lo', 'lu', 'ly', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ng', 'ni', 'no', 'ns', 'ná', 'né', 'ní', 'ný', 'nč', 'ob', 'od', 'ok', 'om', 'op', 'or', 'os', 'ou', 'ov', 'pi', 'po', 'pr', 'ra', 're', 'ri', 'ro', 'rá', 'sa', 'se', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sp', 'st', 'ta', 'te', 'ti', 'tn', 'to', 'tr', 'tv', 'tý', 'up', 'us', 'už', 'va', 've', 'vi', 'vo', 'vy', 'za', 'zn', 'zo', 'zp', 'át', 'éh', 'íc', 'ík', 'ís', 'ýc', 'ým', 'če', 'či', 'čl', 'čn', 'ďa', 'šn', 'št', 'že', 'ži']

#Number of occurrences: 35
slovak_czech_3grams  = ['Rak', 'aby', 'ale', 'býv', 'ens', 'esn', 'fin', 'hod', 'hra', 'ite', 'jin', 'lov', 'men', 'nej', 'nem', 'nic', 'nov', 'níc', 'obc', 'ova', 'pod', 'pok', 'pol', 'pre', 'rak', 'ran', 'ské', 'slu', 'sta', 'str', 'tis', 'vel', 'ého', 'čes', 'čet']

#Number of occurrences: 5
slovak_czech_4grams  = ['hran', 'poli', 'veli', 'česk', 'četn']

#Number of occurrences: 95
polish_danish_2grams  = ['By', 'Ja', 'Mi', 'Os', 'Po', 'Pr', 'St', 'ad', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'ba', 'bo', 'br', 'ci', 'da', 'dl', 'dn', 'do', 'dr', 'ed', 'eg', 'ej', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ga', 'gh', 'gr', 'ha', 'ie', 'ik', 'il', 'in', 'io', 'is', 'je', 'ka', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'lk', 'ma', 'me', 'mi', 'mo', 'na', 'nd', 'ne', 'ni', 'nk', 'no', 'nt', 'nu', 'ny', 'od', 'ol', 'om', 'on', 'op', 'or', 'pa', 'po', 'pr', 'ra', 're', 'ro', 'rt', 'sa', 'sc', 'si', 'sk', 'sp', 'st', 'ta', 'te', 'tn', 'to', 'tr', 'tt', 'ty', 'ud', 'ut']

#Number of occurrences: 7
polish_danish_3grams  = ['ale', 'eli', 'end', 'kom', 'sta', 'sto', 'str']

#Number of occurrences: 0
polish_danish_4grams  = []

#Number of occurrences: 129
polish_german_2grams  = ['Ja', 'Ki', 'Mi', 'Na', 'Ni', 'Po', 'Pr', 'SS', 'St', 'Tr', 'ac', 'ad', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'au', 'ba', 'bi', 'br', 'bu', 'by', 'ch', 'da', 'dl', 'dn', 'do', 'dr', 'ec', 'ed', 'eg', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ew', 'ga', 'go', 'gr', 'ha', 'ic', 'ie', 'ik', 'il', 'im', 'in', 'io', 'is', 'ja', 'je', 'ju', 'ka', 'ki', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'lk', 'ln', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'nd', 'ne', 'ni', 'nk', 'no', 'nt', 'nu', 'ob', 'oc', 'od', 'ol', 'om', 'on', 'or', 'os', 'ot', 'ow', 'pa', 'pi', 'po', 'pr', 'ra', 're', 'ro', 'rt', 'rz', 'sa', 'sc', 'si', 'sk', 'sp', 'st', 'ta', 'te', 'tn', 'to', 'tr', 'tt', 'tu', 'uc', 'ug', 'up', 'ur', 'us', 'ut', 'wa', 'we', 'wi', 'wo', 'za', 'ze', 'zi', 'zo', 'zw']

#Number of occurrences: 16
polish_german_3grams  = ['ach', 'ant', 'bar', 'bra', 'end', 'ich', 'jed', 'kom', 'nic', 'nie', 'ran', 'sie', 'sta', 'str', 'wie', 'zie']

#Number of occurrences: 0
polish_german_4grams  = []

#Number of occurrences: 136
polish_czech_2grams  = ['By', 'Ja', 'Mi', 'Na', 'Os', 'Po', 'Pr', 'SS', 'St', 'ac', 'ad', 'aj', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'au', 'az', 'ba', 'bi', 'bo', 'br', 'bu', 'by', 'ch', 'ci', 'da', 'dl', 'dn', 'do', 'dr', 'ec', 'ed', 'ej', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ga', 'gh', 'go', 'gr', 'ha', 'ia', 'ic', 'ie', 'ik', 'il', 'in', 'is', 'ja', 'je', 'ka', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'lk', 'ln', 'lu', 'ma', 'me', 'mi', 'mn', 'mo', 'mu', 'my', 'na', 'nd', 'ne', 'ni', 'nk', 'no', 'nt', 'nu', 'ny', 'ob', 'oc', 'od', 'oj', 'ok', 'ol', 'om', 'on', 'op', 'or', 'os', 'ot', 'oz', 'pa', 'pi', 'po', 'pr', 'ra', 're', 'ro', 'rt', 'ry', 'sa', 'sc', 'si', 'sk', 'sp', 'st', 'ta', 'te', 'tn', 'to', 'tr', 'tu', 'ty', 'uc', 'ud', 'uk', 'up', 'ur', 'us', 'ut', 'yc', 'za', 'zb', 'ze', 'zi', 'zk', 'zn', 'zo', 'zp']

#Number of occurrences: 26
polish_czech_3grams  = ['ale', 'ali', 'ani', 'bar', 'cho', 'dom', 'dos', 'eli', 'ghe', 'ich', 'jak', 'jed', 'kom', 'nas', 'nic', 'pod', 'pra', 'ran', 'roz', 'sta', 'sto', 'str', 'tak', 'tam', 'zas', 'zna']

#Number of occurrences: 5
polish_czech_4grams  = ['byli', 'dost', 'ghet', 'prac', 'zast']

#Number of occurrences: 197
danish_german_2grams  = ['Al', 'An', 'Ar', 'Ba', 'Be', 'Bl', 'Da', 'De', 'En', 'Ge', 'Gr', 'Ha', 'He', 'Ho', 'Hu', 'In', 'Ja', 'Ko', 'Kr', 'La', 'Le', 'Ma', 'Me', 'Mi', 'Mo', 'No', 'Pe', 'Po', 'Pr', 'Ra', 'Re', 'Ri', 'Sa', 'Se', 'Si', 'St', 'Un', 'Ve', 'ab', 'ad', 'ae', 'af', 'ag', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'ba', 'be', 'bl', 'br', 'ce', 'da', 'de', 'di', 'dl', 'dn', 'do', 'dr', 'ds', 'dt', 'eb', 'ed', 'ef', 'eg', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'fa', 'fe', 'fi', 'fo', 'fr', 'ft', 'fu', 'ga', 'ge', 'gi', 'gl', 'gr', 'gs', 'gt', 'ha', 'he', 'hi', 'hl', 'ho', 'id', 'ie', 'if', 'ig', 'ik', 'il', 'in', 'io', 'is', 'it', 'je', 'ka', 'ke', 'kl', 'ko', 'kr', 'kt', 'ku', 'la', 'ld', 'le', 'lf', 'lg', 'li', 'lk', 'll', 'lo', 'ls', 'lt', 'ma', 'me', 'mi', 'mm', 'mo', 'mt', 'na', 'nd', 'ne', 'nf', 'ng', 'nh', 'ni', 'nk', 'nn', 'no', 'ns', 'nt', 'nu', 'od', 'of', 'ol', 'om', 'on', 'or', 'pa', 'pe', 'po', 'pp', 'pr', 'ra', 'rb', 'rd', 're', 'rf', 'rh', 'ri', 'rk', 'rl', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'sa', 'sb', 'sc', 'se', 'si', 'sk', 'sl', 'so', 'sp', 'ss', 'st', 'su', 'ta', 'te', 'ti', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'ue', 'ul', 'un', 'ut', 'va', 've', 'vi', 'vo']

#Number of occurrences: 99
danish_german_3grams  = ['Bes', 'Der', 'Gen', 'Ges', 'Kon', 'Kri', 'Man', 'Per', 'Pol', 'Sta', 'abe', 'all', 'and', 'ang', 'ans', 'ari', 'beg', 'ber', 'bes', 'bet', 'ble', 'bli', 'chl', 'dan', 'del', 'dem', 'den', 'der', 'des', 'det', 'dig', 'dis', 'ede', 'ell', 'end', 'ens', 'ent', 'era', 'ere', 'ern', 'ers', 'for', 'fra', 'fre', 'gel', 'gen', 'ger', 'ges', 'gte', 'han', 'hen', 'her', 'hol', 'ige', 'ind', 'ing', 'ion', 'ist', 'kan', 'ker', 'kom', 'kon', 'lag', 'lan', 'let', 'lie', 'lin', 'lle', 'lli', 'man', 'men', 'mer', 'min', 'mme', 'nde', 'nge', 'obe', 'omm', 'ord', 'ort', 'ren', 'sen', 'ser', 'ses', 'son', 'sse', 'sta', 'ste', 'sti', 'str', 'tag', 'ter', 'tes', 'tet', 'tig', 'tio', 'tte', 'und', 'ver']

#Number of occurrences: 9
danish_german_4grams  = ['Pers', 'alle', 'ande', 'dere', 'ende', 'komm', 'nder', 'ngen', 'tion']

#Number of occurrences: 173
danish_czech_2grams  = ['Al', 'Ba', 'Be', 'By', 'Da', 'Ha', 'He', 'Ho', 'In', 'Ja', 'Ko', 'Kr', 'La', 'Lo', 'Ma', 'Me', 'Mi', 'Mo', 'Os', 'Po', 'Pr', 'Ra', 'Sa', 'Se', 'St', 'Ve', 'ab', 'ad', 'ak', 'al', 'am', 'an', 'ar', 'as', 'at', 'av', 'ba', 'be', 'bl', 'bo', 'br', 'ce', 'ci', 'da', 'de', 'di', 'dk', 'dl', 'dn', 'do', 'dr', 'dv', 'eb', 'ed', 'ej', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'ev', 'fe', 'fi', 'fo', 'ga', 'ge', 'gh', 'gr', 'ha', 'he', 'hl', 'ho', 'id', 'ie', 'ig', 'ik', 'il', 'in', 'is', 'it', 'iv', 'je', 'jo', 'ka', 'ke', 'kl', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'lk', 'll', 'lo', 'ls', 'lt', 'ma', 'me', 'mi', 'mo', 'na', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'ns', 'nt', 'nu', 'ny', 'od', 'ol', 'om', 'on', 'op', 'or', 'ov', 'pa', 'pe', 'pl', 'po', 'pr', 'ra', 're', 'rf', 'ri', 'rk', 'rl', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'rv', 'sa', 'sb', 'sc', 'se', 'si', 'sk', 'sl', 'sm', 'so', 'sp', 'st', 'su', 'sv', 'ta', 'te', 'ti', 'tl', 'tn', 'to', 'tr', 'ts', 'ty', 'ud', 'ul', 'un', 'ut', 'va', 've', 'vi', 'vn', 'vo', 'yn']

#Number of occurrences: 47
danish_czech_3grams  = ['Pol', 'Pro', 'ale', 'and', 'bud', 'chl', 'dem', 'den', 'eli', 'ens', 'ent', 'ers', 'gel', 'gen', 'ing', 'ist', 'iti', 'kan', 'ker', 'kla', 'kom', 'kon', 'led', 'ler', 'let', 'lin', 'man', 'men', 'min', 'ned', 'nem', 'nes', 'nsk', 'ort', 'ses', 'ska', 'sko', 'sta', 'ste', 'sti', 'sto', 'str', 'tem', 'ter', 'ved', 'ven', 'vid']

#Number of occurrences: 3
danish_czech_4grams  = ['mini', 'ster', 'stra']

#Number of occurrences: 220
german_czech_2grams  = ['Al', 'Ba', 'Be', 'Bi', 'Br', 'Bu', 'Ch', 'Da', 'Do', 'Dr', 'Fr', 'Ha', 'He', 'Hi', 'Ho', 'II', 'In', 'Ja', 'Je', 'Ka', 'Ko', 'Kr', 'La', 'Li', 'Ma', 'Me', 'Mi', 'Mo', 'Mu', 'Na', 'Ne', 'Ob', 'Pa', 'Po', 'Pr', 'Ra', 'Ru', 'SS', 'Sa', 'Sc', 'Se', 'So', 'St', 'Ta', 'Te', 'To', 'Ve', 'Ze', 'ab', 'ac', 'ad', 'ah', 'ak', 'al', 'am', 'an', 'ap', 'ar', 'as', 'at', 'au', 'ba', 'be', 'bi', 'bl', 'br', 'bu', 'by', 'ce', 'ch', 'ck', 'da', 'de', 'di', 'dl', 'dn', 'do', 'dr', 'du', 'eb', 'ec', 'ed', 'ei', 'ek', 'el', 'em', 'en', 'er', 'es', 'et', 'fe', 'fi', 'fo', 'ga', 'ge', 'go', 'gr', 'ha', 'he', 'hl', 'hn', 'ho', 'hr', 'hu', 'ic', 'id', 'ie', 'ig', 'ih', 'ik', 'il', 'in', 'is', 'it', 'ja', 'je', 'ka', 'ke', 'kl', 'ko', 'kr', 'kt', 'ku', 'la', 'le', 'li', 'lk', 'll', 'ln', 'lo', 'ls', 'lt', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'nb', 'nc', 'nd', 'ne', 'ng', 'ni', 'nk', 'nn', 'no', 'ns', 'nt', 'nu', 'nz', 'ob', 'oc', 'od', 'oh', 'ol', 'om', 'on', 'or', 'os', 'ot', 'pa', 'pe', 'pi', 'po', 'pr', 'ra', 'rc', 're', 'rf', 'rg', 'ri', 'rk', 'rl', 'rm', 'rn', 'ro', 'rs', 'rt', 'ru', 'sa', 'sb', 'sc', 'se', 'si', 'sk', 'sl', 'so', 'sp', 'st', 'su', 'ta', 'te', 'ti', 'tl', 'tn', 'to', 'tr', 'ts', 'tu', 'ub', 'uc', 'ul', 'um', 'un', 'up', 'ur', 'us', 'ut', 'va', 've', 'vi', 'vo', 'za', 'ze', 'zi', 'zo', 'zu', 'üh']

#Number of occurrences: 78
german_czech_3grams  = ['Kra', 'Men', 'Pol', 'Pra', 'Sch', 'ade', 'and', 'aut', 'bar', 'bez', 'cha', 'chl', 'cht', 'dem', 'den', 'ech', 'eck', 'ein', 'ens', 'ent', 'ers', 'fin', 'gel', 'gen', 'hla', 'ich', 'ili', 'ing', 'ist', 'ite', 'jed', 'jen', 'kam', 'kan', 'ken', 'ker', 'kli', 'kom', 'kon', 'kte', 'len', 'let', 'lin', 'lov', 'mal', 'man', 'mat', 'men', 'min', 'mus', 'nac', 'nen', 'nic', 'noc', 'not', 'nsp', 'ode', 'oli', 'ori', 'ort', 'pro', 'ran', 'sch', 'sel', 'ses', 'sin', 'sta', 'ste', 'sti', 'str', 'tel', 'ten', 'ter', 'tis', 'tra', 'tro', 'vol', 'zen']

#Number of occurrences: 6
german_czech_4grams  = ['Schu', 'denn', 'jede', 'nich', 'spor', 'stan']

