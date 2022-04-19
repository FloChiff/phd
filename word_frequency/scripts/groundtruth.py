
# -*- UTF-8 -*-

"""
- author: Floriane Chiffoleau
- date: April 2022
- description: Retrieving the content of the groundtruth
- input : XML files
- output: TXT file
- usage :
    ======
    python name_of_this_script.py arg1
    arg1: folder of the groundtruth in their XML format
"""

import os
import sys
from bs4 import BeautifulSoup

for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        with open(sys.argv[1] + filename, 'r') as xml_file:

            processed_text_as_list = []
            soup = BeautifulSoup(xml_file, 'xml')
            #Extract content from the XML ALTO files
            for string in soup.find_all("String"):
                content = string["CONTENT"]
                processed_text_as_list.append(content)
            new_text = "\n".join(processed_text_as_list)

        with open("ground_truth.txt", "a") as file_out:
            #Warning: the output file is in a "add" mode, which mean that it will add groundtruth, file after file
            file_out.write(new_text)