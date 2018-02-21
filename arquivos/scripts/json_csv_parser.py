# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:00:56 2018

@author: Elcius

ALL JSON FILES MUST BE ENCODED IN UTF-8 BEFORE RUNNING THIS SCRIPT.
"""

import json, csv, os

files = [f for f in os.listdir('../json')]  # loading files

for f in files:
    file_name, ext = os.path.splitext(f)
    if ext == '.json':
        print('Processing file: ', f)
        inputFile = open('../json/' + f, encoding = "utf8")
        outputFile = open('../../proposicoes/' + file_name + '.csv', 'w')
    
        json_data = json.load(inputFile)
        json_data = json_data['data']
        inputFile.close()

        output = csv.writer(outputFile)
        output.writerow(json_data[0].keys())   # columns names
        
        for row in json_data:
            output.writerow(row.values())  # writing content

print('Finished!')




