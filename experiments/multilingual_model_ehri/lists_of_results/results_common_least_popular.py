#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
- author: Floriane Chiffoleau
- date: February 2024
- description: Results from the scripts for the least popular tokens
"""

#Number of occurrences: 0
common_2grams  = []

#Number of occurrences: 0
common_3grams  = []

#Number of occurrences: 0
common_4grams  = []

#Number of occurrences: 16
hungarian_slovak_2grams  = ['Em', 'Ga', 'Hu', 'Já', 'Mu', 'Rö', 'VA', 'Wi', 'Wo', 'db', 'gd', 'ht', 'mü', 'pc', 'ue', 'ív']

#Number of occurrences: 42
hungarian_slovak_3grams  = ['Bar', 'Her', 'Ján', 'Kit', 'Kom', 'Ste', 'Ter', 'Wil', 'Wol', 'ack', 'dbe', 'ein', 'ejt', 'epi', 'fac', 'fon', 'ici', 'ime', 'ito', 'keb', 'ler', 'lic', 'lom', 'moc', 'nik', 'oba', 'odo', 'org', 'pás', 'rot', 'rál', 'sil', 'smi', 'spe', 'stn', 'tív', 'uni', 'usi', 'vil', 'zom', 'zub', 'íci']

#Number of occurrences: 12
hungarian_slovak_4grams  = ['Bert', 'Wolf', 'arok', 'augu', 'kalo', 'konc', 'legi', 'nali', 'nove', 'smer', 'szeg', 'tein']

#Number of occurrences: 10
hungarian_english_2grams  = ['Fl', 'LO', 'NC', 'OR', 'Pi', 'Qu', 'ZE', 'nh', 'nr', 'sg']

#Number of occurrences: 45
hungarian_english_3grams  = ['Bar', 'Gaz', 'HON', 'Han', 'Hos', 'Jug', 'Kap', 'Kit', 'Sen', 'Vis', 'Zel', 'aen', 'afo', 'amp', 'arc', 'bin', 'bit', 'cem', 'das', 'dne', 'efu', 'elu', 'epi', 'erk', 'fan', 'fif', 'gan', 'gip', 'imu', 'ito', 'lom', 'lov', 'ncy', 'oms', 'pin', 'raz', 'rle', 'seh', 'tig', 'tni', 'ton', 'tos', 'utt', 'vac', 'zia']

#Number of occurrences: 32
hungarian_english_4grams  = ['Pers', 'Term', 'arde', 'bord', 'chal', 'cher', 'dere', 'elem', 'eles', 'evel', 'gari', 'gato', 'gest', 'gips', 'gros', 'homo', 'hrer', 'inge', 'isch', 'mine', 'muni', 'nrat', 'omat', 'omma', 'pici', 'rant', 'reme', 'traf', 'unis', 'vast', 'vene', 'vent']

#Number of occurrences: 13
hungarian_polish_2grams  = ['Br', 'Ca', 'IT', 'Id', 'PA', 'RS', 'db', 'ds', 'ef', 'ht', 'tc', 'ue', 'uf']

#Number of occurrences: 42
hungarian_polish_3grams  = ['Aug', 'Bar', 'Cap', 'Cha', 'Ges', 'Hal', 'Her', 'Pod', 'Ter', 'abo', 'arf', 'ase', 'ast', 'bin', 'cbe', 'cer', 'dne', 'dsz', 'egs', 'erk', 'ers', 'gro', 'hom', 'kle', 'kul', 'mal', 'mis', 'nig', 'oba', 'rni', 'seh', 'szu', 'tla', 'tni', 'tre', 'yne', 'yzn', 'zec', 'znó', 'zom', 'zre', 'zup']

#Number of occurrences: 13
hungarian_polish_4grams  = ['Augu', 'Capo', 'Gest', 'Mend', 'Star', 'chal', 'echt', 'kart', 'kilo', 'nali', 'osta', 'szni', 'toka']

#Number of occurrences: 12
hungarian_danish_2grams  = ['ER', 'FO', 'IE', 'Is', 'Pi', 'TA', 'Tu', 'bd', 'cy', 'hm', 'ht', 'ub']

#Number of occurrences: 45
hungarian_danish_3grams  = ['Ang', 'Aug', 'Fle', 'Hid', 'Hil', 'Hos', 'Jug', 'Kap', 'Ken', 'Lev', 'Mih', 'Mir', 'Nac', 'Tek', 'Val', 'Vin', 'abo', 'alb', 'bin', 'cer', 'dap', 'dne', 'ein', 'ekl', 'ekv', 'eti', 'fan', 'fon', 'gro', 'ilk', 'jus', 'keb', 'ldb', 'lom', 'mga', 'mre', 'nig', 'nta', 'sre', 'stn', 'tiv', 'tti', 'uni', 'vos', 'yre']

#Number of occurrences: 18
hungarian_danish_4grams  = ['Augu', 'Nach', 'Star', 'apes', 'beho', 'edte', 'elde', 'elit', 'enig', 'fent', 'ifik', 'kana', 'lene', 'omat', 'prot', 'udta', 'vill', 'ynek']

#Number of occurrences: 13
hungarian_german_2grams  = ['Ah', 'BI', 'FO', 'Id', 'Já', 'PA', 'Pi', 'RT', 'Wü', 'db', 'tc', 'Ös', 'öd']

#Number of occurrences: 55
hungarian_german_3grams  = ['Cap', 'Dun', 'Fel', 'Get', 'Hor', 'Jug', 'Kam', 'Los', 'Rom', 'Soh', 'Tar', 'Zür', 'abo', 'aza', 'buc', 'bun', 'büs', 'dde', 'ddi', 'efu', 'egü', 'ekb', 'elu', 'epi', 'eti', 'fab', 'fon', 'hav', 'hod', 'ike', 'ime', 'ive', 'jud', 'kün', 'lha', 'lon', 'lün', 'moc', 'mod', 'mom', 'oba', 'ope', 'ror', 'sba', 'sev', 'smi', 'sre', 'tik', 'tiv', 'tsz', 'ttr', 'uli', 'völ', 'zis', 'zup']

#Number of occurrences: 40
hungarian_german_4grams  = ['Augu', 'Capo', 'Hann', 'Herm', 'Juge', 'Kris', 'Moto', 'Sala', 'anti', 'ause', 'bevo', 'bres', 'ebur', 'edet', 'edte', 'eiss', 'elek', 'elit', 'eres', 'erve', 'hont', 'hrer', 'imet', 'jude', 'lenk', 'mart', 'mess', 'mode', 'nkba', 'nkra', 'nste', 'ntin', 'rlet', 'rtun', 'ssel', 'tenn', 'terh', 'tlag', 'usch', 'zerr']

#Number of occurrences: 13
hungarian_czech_2grams  = ['Du', 'ER', 'Fl', 'Jo', 'Sá', 'Tí', 'Wo', 'bd', 'cy', 'ee', 'nr', 'pc', 'zy']

#Number of occurrences: 76
hungarian_czech_3grams  = ['Alb', 'Bal', 'Cap', 'Har', 'Jar', 'Jug', 'Kam', 'Kap', 'Ker', 'Kor', 'Kos', 'Mir', 'Per', 'Val', 'Vis', 'Wol', 'apa', 'arc', 'bri', 'báj', 'ciá', 'das', 'dje', 'dké', 'dvé', 'dák', 'elu', 'eps', 'ezl', 'fon', 'fáz', 'gro', 'hei', 'iká', 'isí', 'kci', 'kip', 'kst', 'kul', 'lab', 'láv', 'mod', 'mpo', 'ndi', 'ngo', 'nné', 'nác', 'odo', 'oké', 'osí', 'ozi', 'pál', 'rál', 'sba', 'sbe', 'sej', 'sip', 'suk', 'teo', 'the', 'tná', 'tth', 'tze', 'tín', 'uja', 'ura', 'uss', 'yho', 'yte', 'ytu', 'zez', 'zhe', 'zác', 'ásl', 'áte', 'áti']

#Number of occurrences: 41
hungarian_czech_4grams  = ['Bert', 'Capo', 'Gest', 'Hann', 'Horn', 'Pers', 'Schö', 'Wolf', 'Zeit', 'ansp', 'anti', 'bato', 'cert', 'elek', 'elem', 'elné', 'elád', 'enba', 'enci', 'gest', 'gros', 'ifik', 'iste', 'kalo', 'kilo', 'kopa', 'laso', 'leny', 'nati', 'nems', 'nove', 'nste', 'over', 'rant', 'romo', 'rsch', 'tend', 'teto', 'vers', 'zame', 'zeti']

#Number of occurrences: 7
english_slovak_2grams  = ['Ci', 'KR', 'NS', 'Op', 'lc', 'nl', 'tä']

#Number of occurrences: 37
english_slovak_3grams  = ['Ale', 'Bar', 'Bol', 'Bud', 'Bus', 'Jak', 'Kit', 'Mus', 'Pen', 'Tak', 'Vil', 'cip', 'dro', 'ede', 'edl', 'edy', 'epi', 'hab', 'ick', 'ier', 'ink', 'isl', 'ito', 'kla', 'lom', 'nut', 'olu', 'pil', 'pio', 'reb', 'roc', 'ros', 'sno', 'ssl', 'udi', 'via', 'xan']

#Number of occurrences: 13
english_slovak_4grams  = ['Alex', 'Jako', 'Park', 'Schi', 'ande', 'iedo', 'lite', 'nera', 'pion', 'rato', 'rman', 'tres', 'unif']

#Number of occurrences: 5
english_polish_2grams  = ['Ci', 'El', 'Lu', 'NK', 'km']

#Number of occurrences: 37
english_polish_3grams  = ['Arc', 'Bar', 'Bro', 'Cho', 'Gru', 'Maj', 'Mur', 'Mus', 'Tak', 'aci', 'acy', 'atu', 'awn', 'bal', 'bin', 'deg', 'dek', 'dne', 'ebr', 'enb', 'erk', 'etr', 'ewo', 'ink', 'isa', 'mne', 'ork', 'ote', 'pil', 'pus', 'rol', 'seh', 'tek', 'tni', 'twe', 'wac', 'wle']

#Number of occurrences: 15
english_polish_4grams  = ['Arch', 'Jako', 'Musi', 'auta', 'cele', 'chal', 'estr', 'gral', 'piec', 'rato', 'repa', 'taki', 'tres', 'tria', 'wido']

#Number of occurrences: 8
english_danish_2grams  = ['Ae', 'DE', 'ET', 'IG', 'LL', 'ME', 'Pi', 'SC']

#Number of occurrences: 52
english_danish_3grams  = ['Ael', 'Bud', 'Dir', 'Ent', 'Geb', 'Hit', 'Hos', 'Jer', 'Jug', 'Kap', 'Lin', 'Mob', 'Mus', 'Pet', 'Pig', 'SER', 'San', 'Sla', 'Str', 'amt', 'big', 'bin', 'byg', 'cht', 'cip', 'dek', 'dne', 'dro', 'dts', 'ebo', 'etl', 'ets', 'fan', 'fen', 'gsb', 'hre', 'ier', 'iga', 'ios', 'isc', 'itr', 'kis', 'kne', 'lom', 'och', 'pel', 'slo', 'sun', 'tab', 'tef', 'tev', 'ube']

#Number of occurrences: 54
english_danish_4grams  = ['Aelt', 'Barn', 'Bele', 'Buda', 'Dire', 'Ente', 'Film', 'Fred', 'Here', 'Hitl', 'Jugo', 'Mobi', 'Moti', 'Orde', 'Park', 'Patr', 'Pest', 'Pris', 'Rati', 'Tide', 'affe', 'arts', 'besi', 'bond', 'burd', 'cere', 'cite', 'dipl', 'ekto', 'elim', 'endo', 'estr', 'gati', 'illi', 'illu', 'istr', 'itie', 'ivel', 'lder', 'lusi', 'nera', 'ngsb', 'omat', 'orch', 'osit', 'pest', 'rato', 'repu', 'sens', 'stad', 'temp', 'urer', 'utte', 'vere']

#Number of occurrences: 11
english_german_2grams  = ['Ci', 'EN', 'GE', 'HO', 'JU', 'Pi', 'Zo', 'km', 'nq', 'vr', 'zs']

#Number of occurrences: 48
english_german_3grams  = ['Cra', 'Des', 'Det', 'Exp', 'FOR', 'Gal', 'Inf', 'Jer', 'Jug', 'Mem', 'Mob', 'Mus', 'Obs', 'Oes', 'Sou', 'aph', 'asp', 'big', 'bte', 'deg', 'dek', 'dge', 'dro', 'efu', 'elu', 'env', 'epi', 'etl', 'fet', 'htm', 'idl', 'nas', 'nut', 'ork', 'ote', 'ows', 'pie', 'pil', 'raw', 'rhu', 'ros', 'sfu', 'tiz', 'udi', 'unl', 'via', 'vit', 'zil']

#Number of occurrences: 70
english_german_4grams  = ['Bele', 'Bels', 'Brau', 'Expe', 'Ferd', 'Fort', 'Hink', 'Info', 'Jeru', 'Mili', 'Mobi', 'Musi', 'Obst', 'Oest', 'Park', 'Reli', 'Sani', 'Sche', 'True', 'Vero', 'asiu', 'bell', 'chim', 'degr', 'drin', 'elli', 'erri', 'fres', 'gass', 'grap', 'gymn', 'heir', 'hest', 'hrer', 'idor', 'ient', 'illi', 'insc', 'laid', 'line', 'lite', 'loss', 'mati', 'mora', 'nega', 'nger', 'nota', 'ntie', 'onne', 'orch', 'phon', 'rain', 'rats', 'rdnu', 'repa', 'rfue', 'ries', 'smit', 'spri', 'stag', 'taug', 'trat', 'trif', 'unan', 'unen', 'unha', 'unle', 'vere', 'wach', 'zsch']

#Number of occurrences: 10
english_czech_2grams  = ['Ci', 'ED', 'Fl', 'Gi', 'LL', 'Lu', 'Oe', 'Zo', 'nq', 'nr']

#Number of occurrences: 52
english_czech_3grams  = ['Arc', 'Des', 'Eld', 'Flo', 'Jug', 'Kap', 'Kro', 'Kru', 'Maj', 'Mil', 'Nev', 'Obs', 'Oes', 'Ord', 'Pop', 'Rau', 'San', 'Vil', 'Vis', 'ael', 'arc', 'atu', 'das', 'deg', 'dun', 'elu', 'emo', 'enh', 'hat', 'hly', 'ida', 'ier', 'luc', 'lwa', 'mie', 'mwi', 'nis', 'nun', 'oce', 'ols', 'ork', 'ota', 'psy', 'pta', 'raf', 'ras', 'rur', 'tab', 'udi', 'vit', 'von', 'xan']

#Number of occurrences: 64
english_czech_4grams  = ['Arch', 'Brau', 'Buda', 'Carm', 'Frei', 'Jugo', 'Lind', 'Oest', 'Pers', 'Raum', 'Sani', 'Sche', 'amen', 'atro', 'avou', 'benc', 'cere', 'chte', 'chur', 'elem', 'elli', 'erbe', 'erei', 'erre', 'erto', 'evil', 'gest', 'gros', 'harm', 'holo', 'icis', 'inem', 'insk', 'istr', 'lest', 'lite', 'majo', 'mask', 'nato', 'ndan', 'neck', 'nera', 'ners', 'niti', 'ovis', 'pest', 'pita', 'plet', 'psyc', 'puri', 'rant', 'renc', 'repu', 'sedu', 'soci', 'stru', 'tenl', 'tera', 'titi', 'tras', 'tres', 'vous', 'wach', 'wirt']

#Number of occurrences: 14
slovak_polish_2grams  = ['Bo', 'Ci', 'Cu', 'db', 'dt', 'fs', 'ft', 'ht', 'ij', 'lf', 'mk', 'ml', 'pt', 'ue']

#Number of occurrences: 51
slovak_polish_3grams  = ['Bar', 'Chc', 'Cuk', 'Her', 'Men', 'Mus', 'Odd', 'Ros', 'Roz', 'Tak', 'Ter', 'Zaj', 'Zal', 'amu', 'ato', 'dna', 'dra', 'eri', 'erz', 'for', 'hal', 'her', 'iko', 'ini', 'ink', 'izb', 'kru', 'kup', 'lit', 'mac', 'mla', 'niu', 'oba', 'obj', 'obr', 'obu', 'ojn', 'omi', 'opo', 'opr', 'pil', 'pis', 'pop', 'red', 'ret', 'stu', 'tar', 'tec', 'tur', 'zes', 'zom']

#Number of occurrences: 24
slovak_polish_4grams  = ['Jako', 'Tere', 'dkam', 'edlo', 'iezo', 'mate', 'moje', 'nale', 'nali', 'nika', 'obra', 'obst', 'odzn', 'opis', 'pili', 'podn', 'pomo', 'popr', 'rato', 'samo', 'tres', 'zaba', 'zakr', 'zdar']

#Number of occurrences: 5
slovak_danish_2grams  = ['IN', 'Ob', 'Vr', 'ht', 'vk']

#Number of occurrences: 30
slovak_danish_3grams  = ['Ann', 'Bud', 'Bur', 'Fri', 'Jud', 'Jul', 'Mag', 'Mus', 'Ris', 'ame', 'anu', 'cip', 'dok', 'dro', 'ein', 'fon', 'heb', 'ier', 'iko', 'ius', 'keb', 'lmo', 'lom', 'orn', 'pon', 'rid', 'sed', 'stn', 'uni', 'use']

#Number of occurrences: 21
slovak_danish_4grams  = ['Anna', 'Jude', 'Juli', 'Park', 'Regi', 'VIII', 'amer', 'disc', 'dler', 'eden', 'hebr', 'ille', 'nera', 'pris', 'rato', 'rich', 'ridi', 'rins', 'sche', 'spor', 'will']

#Number of occurrences: 7
slovak_german_2grams  = ['Ci', 'Já', 'ct', 'db', 'ij', 'jo', 'np']

#Number of occurrences: 38
slovak_german_3grams  = ['Bur', 'Hug', 'Jan', 'Jos', 'Mac', 'Mus', 'Ros', 'VII', 'aeg', 'ato', 'bor', 'dli', 'dro', 'epi', 'ezi', 'fon', 'hni', 'ial', 'ice', 'ila', 'ime', 'ius', 'moc', 'mür', 'nom', 'nos', 'nut', 'oba', 'omo', 'opi', 'pil', 'ref', 'rid', 'ros', 'smi', 'sna', 'udi', 'via']

#Number of occurrences: 16
slovak_german_4grams  = ['Fron', 'Hugo', 'Jose', 'Park', 'Stro', 'disc', 'dter', 'ebor', 'enos', 'ille', 'konz', 'lite', 'nete', 'rasi', 'stil', 'veru']

#Number of occurrences: 13
slovak_czech_2grams  = ['Ci', 'Mü', 'Wo', 'Zm', 'ct', 'fy', 'nm', 'pc', 'rč', 'ék', 'úc', 'ýš', 'šu']

#Number of occurrences: 63
slovak_czech_3grams  = ['Bur', 'Fri', 'Hed', 'Jul', 'Mac', 'Mül', 'Roz', 'Vil', 'Wol', 'Zák', 'amk', 'anu', 'avs', 'cie', 'dli', 'dna', 'doč', 'duj', 'ezi', 'fon', 'für', 'heb', 'ial', 'ier', 'iso', 'kré', 'mac', 'mác', 'niu', 'odo', 'odr', 'opi', 'otv', 'oty', 'ref', 'rei', 'rný', 'rál', 'sne', 'tko', 'udi', 'und', 'upu', 'urs', 'vaj', 'veb', 'ver', 'vik', 'vkr', 'vle', 'vyn', 'xan', 'zvý', 'ádk', 'áčk', 'íno', 'ísa', 'íče', 'úči', 'Čet', 'čný', 'čně', 'žby']

#Number of occurrences: 84
slovak_czech_4grams  = ['Bert', 'Bude', 'Burg', 'Chce', 'Frie', 'Hert', 'Hugo', 'Morg', 'Müll', 'Pozn', 'Wolf', 'Zají', 'ache', 'arsk', 'aráv', 'atým', 'chla', 'dané', 'ejsk', 'elka', 'elky', 'ezen', 'ezli', 'hebr', 'häft', 'iknu', 'išli', 'kalo', 'kové', 'lený', 'letá', 'lite', 'llin', 'lodí', 'mali', 'moje', 'muje', 'nede', 'neop', 'nepl', 'nera', 'nete', 'nezd', 'nečn', 'nili', 'nist', 'nove', 'nápi', 'nému', 'obra', 'odov', 'olsk', 'opro', 'orgá', 'ovný', 'ozna', 'posk', 'pouk', 'povi', 'prap', 'refe', 'schv', 'stři', 'tres', 'ujem', 'ustá', 'vané', 'vkro', 'vydá', 'vyhr', 'vyzn', 'zaba', 'zavi', 'zost', 'zpoč', 'zvýš', 'álen', 'ítan', 'úraz', 'Četn', 'Čísl', 'čili', 'ženo', 'žiku']

#Number of occurrences: 6
polish_danish_2grams  = ['Ke', 'Sz', 'Um', 'ep', 'ht', 'tz']

#Number of occurrences: 33
polish_danish_3grams  = ['Aug', 'Bli', 'Blu', 'Mus', 'abo', 'bad', 'bin', 'cer', 'che', 'dek', 'dne', 'dor', 'eba', 'efo', 'egu', 'emi', 'erf', 'fak', 'fer', 'gro', 'ies', 'iko', 'ise', 'kin', 'kto', 'lil', 'lok', 'nig', 'omn', 'rsk', 'tad', 'tus', 'uel']

#Number of occurrences: 20
polish_danish_4grams  = ['Augu', 'Bere', 'Post', 'Star', 'berg', 'dant', 'dsta', 'enne', 'enta', 'erau', 'estr', 'etar', 'fakt', 'iden', 'kale', 'klam', 'loka', 'mman', 'nade', 'rato']

#Number of occurrences: 10
polish_german_2grams  = ['Ci', 'Id', 'PA', 'db', 'gy', 'ij', 'km', 'ks', 'mz', 'tc']

#Number of occurrences: 42
polish_german_3grams  = ['Cap', 'Ida', 'Kun', 'Mus', 'PAR', 'Pow', 'Ros', 'Sam', 'abo', 'alo', 'ato', 'atr', 'bad', 'bla', 'cen', 'deg', 'dek', 'dep', 'dwi', 'dza', 'gaz', 'ica', 'kin', 'mfü', 'nag', 'nda', 'nni', 'oba', 'ork', 'ote', 'pil', 'ram', 'rep', 'rom', 'rop', 'sek', 'tad', 'upi', 'usz', 'wam', 'zau', 'zup']

#Number of occurrences: 25
polish_german_4grams  = ['Augu', 'Blum', 'Capo', 'Czec', 'Musi', 'Part', 'Powi', 'Stam', 'alen', 'echo', 'emer', 'form', 'iden', 'konf', 'mfüh', 'norm', 'punk', 'repa', 'rmfü', 'rwal', 'rzen', 'sale', 'stur', 'wago', 'zumi']

#Number of occurrences: 3
polish_czech_2grams  = ['Ci', 'Lu', 'gn']

#Number of occurrences: 56
polish_czech_3grams  = ['Arc', 'Cap', 'Dob', 'Dru', 'Gro', 'Lub', 'Maj', 'Mam', 'Man', 'Naz', 'Por', 'Rod', 'Roz', 'Ryb', 'Sos', 'Tos', 'Unt', 'Zas', 'Zna', 'atu', 'bic', 'bla', 'boc', 'che', 'chr', 'deg', 'dna', 'dus', 'eds', 'epr', 'fak', 'geh', 'gro', 'hte', 'isk', 'jec', 'kul', 'liz', 'lub', 'mac', 'nah', 'niu', 'nor', 'ock', 'omy', 'ork', 'osi', 'ozu', 'psa', 'rus', 'ryt', 'syn', 'upi', 'zbu', 'zep', 'zmi']

#Number of occurrences: 48
polish_czech_4grams  = ['Arch', 'Capo', 'Chci', 'Dobr', 'Dost', 'Gest', 'Jank', 'Lubl', 'Poci', 'Sosn', 'Stad', 'Unte', 'berg', 'chni', 'chor', 'domk', 'fakt', 'form', 'hale', 'ijal', 'kilo', 'lata', 'laza', 'mana', 'moje', 'nach', 'nada', 'nade', 'nano', 'norm', 'obli', 'obra', 'odli', 'odsu', 'omil', 'opra', 'ozil', 'poma', 'poru', 'rera', 'rozr', 'skle', 'skrz', 'spod', 'tres', 'usta', 'zaba', 'zaje']

#Number of occurrences: 9
danish_german_2grams  = ['FO', 'Pi', 'SE', 'UD', 'fm', 'oi', 'uu', 'xe', 'ye']

#Number of occurrences: 75
danish_german_3grams  = ['Adv', 'Bem', 'Ben', 'Bio', 'Bur', 'Dav', 'Fas', 'Hes', 'Inh', 'Jer', 'Jug', 'Mob', 'Mus', 'Paa', 'Rat', 'Rea', 'Sek', 'TEL', 'Umf', 'Vid', 'abo', 'aet', 'ags', 'alk', 'app', 'bad', 'big', 'dek', 'dro', 'dsf', 'eer', 'esr', 'eti', 'etl', 'fon', 'gsg', 'gsv', 'iat', 'ifa', 'irt', 'isr', 'ius', 'kin', 'klo', 'lik', 'lre', 'mae', 'mni', 'msf', 'mur', 'nga', 'nre', 'orc', 'rgi', 'rid', 'riu', 'rks', 'rov', 'rta', 'sfa', 'sha', 'sra', 'sre', 'ssk', 'sum', 'säm', 'tad', 'tiv', 'tog', 'tso', 'tut', 'ufa', 'uha', 'umi', 'uun']

#Number of occurrences: 74
danish_german_4grams  = ['Advo', 'Akte', 'Augu', 'Beko', 'Bele', 'Davi', 'Gang', 'Garn', 'Gend', 'Inha', 'Kraf', 'Krim', 'Lang', 'Last', 'Meda', 'Mobi', 'Park', 'Petr', 'Real', 'Saal', 'Thea', 'Treu', 'Umfa', 'aura', 'bade', 'bank', 'bist', 'dend', 'ding', 'disc', 'edle', 'edte', 'elit', 'elsm', 'endd', 'ends', 'erig', 'fand', 'fels', 'gion', 'henh', 'henl', 'iden', 'igte', 'ille', 'illi', 'ison', 'isra', 'klas', 'lind', 'meid', 'moti', 'ndsf', 'ngas', 'oden', 'onsk', 'orch', 'orde', 'rere', 'rigt', 'rime', 'rist', 'sigk', 'sona', 'spli', 'stig', 'sula', 'tate', 'titu', 'tore', 'uhel', 'uhol', 'vens', 'vere']

#Number of occurrences: 7
danish_czech_2grams  = ['Db', 'ER', 'LL', 'bd', 'cy', 'fm', 'xe']

#Number of occurrences: 61
danish_czech_3grams  = ['Ame', 'Ben', 'Bis', 'Bom', 'Bon', 'Bur', 'Dav', 'Eri', 'Fri', 'Hes', 'Jug', 'Jul', 'Jur', 'Kap', 'Kul', 'Mas', 'Mir', 'Obl', 'San', 'Sei', 'Sko', 'Spo', 'Val', 'anu', 'ban', 'bel', 'che', 'cyk', 'dfo', 'die', 'edr', 'esg', 'fak', 'fir', 'fon', 'gik', 'gro', 'heb', 'ids', 'ier', 'ifa', 'iku', 'ikv', 'klu', 'lej', 'lif', 'mos', 'nel', 'onn', 'rgi', 'riu', 'rma', 'rte', 'rvi', 'sav', 'sik', 'tab', 'tka', 'umi', 'utr', 'vej']

#Number of occurrences: 52
danish_czech_4grams  = ['Amer', 'Bomb', 'Bond', 'Buda', 'Davi', 'Holl', 'Jugo', 'Kult', 'Majo', 'Mark', 'Raas', 'Reva', 'alde', 'altu', 'bank', 'berg', 'boxe', 'cere', 'cist', 'cykl', 'demo', 'ding', 'elsm', 'ener', 'fakt', 'fire', 'fone', 'genr', 'haft', 'hebr', 'ifik', 'istr', 'kval', 'lett', 'lidt', 'love', 'nade', 'navl', 'nera', 'nesv', 'obil', 'part', 'pest', 'regi', 'repu', 'scha', 'sedl', 'semi', 'serv', 'tgen', 'trag', 'vans']

#Number of occurrences: 11
german_czech_2grams  = ['Ci', 'Kö', 'Lä', 'Ol', 'Zo', 'ct', 'fm', 'gä', 'lü', 'nq', 'xe']

#Number of occurrences: 72
german_czech_3grams  = ['Ben', 'Bur', 'Cap', 'Dav', 'Des', 'Dra', 'Gün', 'Hes', 'Jug', 'Kam', 'Laz', 'Lot', 'Mac', 'Noc', 'Obs', 'Oes', 'Ohr', 'Sau', 'Sil', 'Tri', 'Uni', 'Zol', 'Zum', 'ara', 'bau', 'bla', 'chö', 'cki', 'ckr', 'deg', 'dli', 'edu', 'elc', 'elu', 'esk', 'eus', 'exi', 'eze', 'ezi', 'ezo', 'fon', 'gal', 'hon', 'ial', 'ifa', 'inh', 'ivi', 'ivá', 'lde', 'lni', 'mbe', 'mec', 'mod', 'ngu', 'nko', 'opi', 'ork', 'pet', 'pfu', 'ref', 'rgi', 'riu', 'sba', 'sli', 'tod', 'ubr', 'udi', 'umi', 'upi', 'vit', 'öhn', 'öne']

#Number of occurrences: 79
german_czech_4grams  = ['Brau', 'Bren', 'Capo', 'Danz', 'Davi', 'Drec', 'Grab', 'Günt', 'Hann', 'Hess', 'Hugo', 'Janu', 'Kami', 'Karl', 'Klau', 'Klin', 'Kurt', 'Laza', 'Mach', 'Mand', 'Oest', 'Prof', 'Reda', 'Sani', 'Sche', 'Silb', 'Soll', 'Ster', 'Stut', 'Tats', 'XXXX', 'Zoll', 'Zuck', 'ansc', 'anti', 'apat', 'arti', 'azil', 'bank', 'bara', 'bsch', 'chem', 'ding', 'disk', 'ekle', 'elek', 'elli', 'elsm', 'eska', 'exis', 'fale', 'form', 'fung', 'htes', 'indi', 'inko', 'krit', 'lisa', 'lite', 'llsc', 'nere', 'nete', 'norm', 'nsky', 'nste', 'nzle', 'poln', 'ramt', 'rest', 'sbru', 'schü', 'sitz', 'svor', 'teri', 'tori', 'unke', 'vidu', 'wach', 'ziti']

