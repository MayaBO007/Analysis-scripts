#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 08:43:37 2023

@author: maya
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy import stats
import pickle

path = '/Users/maya/Downloads/results(10).json'

with open(path) as json_file:
    data = json.load(json_file)

yoda_all = [d for d in data if '05d' in d['subId']]
yoda_first = [d for d in yoda_all if '26' in d['createdAt']]
yoda_second = [d for d in yoda_all if '-27' in d['createdAt']]

def find_max(lst):
    idx = -1
    max_val = -1
    for i in range(len(lst)):
        try:
            choices = len(lst[i]['allChoices'])
        except:
            continue
        if choices > max_val:
            max_val = choices
            idx = i
    return lst[idx]

yoda_natural = find_max(yoda_first)

def find_yellow(lst):
    idx2 = -1
    for j in range(len(lst)):
        try:
            findYellowTest = len(lst[j]['howManyYellows'])
        except:
            continue
        if findYellowTest != []:
            idx2 = j 
    return lst[idx2]

yellow_test = find_yellow(yoda_first)

def find_switch(lst):
    idx3 = -1
    switch_results = -1
    for h in range(len(lst)):
        try:
            findSwitchTest = len(lst[h]['allChoicesSwitch'])
        except:
            continue
        if findSwitchTest > switch_results:
            switch_results = findSwitchTest
            idx3 = h 
    return lst[idx3]

switch_test = find_switch(yoda_first)

def find_dev(lst):
    idx4 = -1
    dev_results = -1
    for f in range(len(lst)):
        try:
            findDevTest = len(lst[f]['allChoicesDev'])
        except:
            continue
        if findDevTest > dev_results:
            dev_results = findDevTest
            idx4 = f 
    return lst[idx4]

dev_test = find_dev(yoda_second)


#%%


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy import stats
import pickle

file = open('ETRL_3', 'wb')
merged_file = {**dev_test, **switch_test, **yellow_test, **yoda_natural}
pickle.dump(merged_file, file)

#find_criteria(yoda, 5, stats.ttest_rel, 6)
#find_criteria(yoda, 5, stats.wilcoxon, 6)







