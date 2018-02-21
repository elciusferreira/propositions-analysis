# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:00:56 2018

@author: Elcius

ALL JSON FILES MUST BE ENCODED IN UTF-8 BEFORE RUNNING THIS SCRIPT.
"""

import pandas as pd
import os

path_dir = '../../proposicoes/'
files = [f for f in os.listdir(path_dir)]  # loading files
#print(files)
merged2 = []  # store all content of all csv files that will be merged

for f in files:
    filename, ext = os.path.splitext(f)

    if ext == '.csv':
        print('Processing file: ', f)
        read = pd.read_csv(path_dir + f)
        merged2.append(read)

result = pd.concat(merged2)

result.to_csv(path_dir + 'proposicoes_1998_2016.csv')
print('Finished!')