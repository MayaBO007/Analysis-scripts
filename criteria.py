#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:56:50 2023

@author: maya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy import stats

def find_criteria(data, sec, stat_func, max_iter = 3):
    
    cars = np.array(data['allChoices'])
    press = np.array(data['correctFirstBluePress'] + data['correctFirstRedPress'])
    
    #sec = 30#int(input('Seconds to slide on: '))
    dt = 1000 * sec
    max_time = max(max(cars), max(press))
    
    means_dict = {'time': [], 'per': []}
    h = 0
    stat_counter = 0
    for i in range(0, max_time, dt):
        
        t_min = 0
        t_max = i+dt
        
        c = len([x for x in cars if x > t_min and x < t_max])
        p = len([x for x in press if x > t_min and x < t_max])
        
        means_dict['time'].append(int(i/1000))
        if c == 0:
            #means_dict['per'].append(0)
            continue
        means_dict['per'].append(p/c)
        
        means_df = pd.DataFrame(means_dict)
        
        j = i//dt
        if h != 0:
            continue
        
        if j > 90//sec:
            pval = stat_func(means_df['per'][j-(60//sec-1):j-(30//sec-1)] , means_df['per'][j-(30//sec-1):])[1]
            #pval = stat_func(means_df['per'][j-(45//sec-1):j-(15//sec-1)] , means_df['per'][j-(30//sec-1):])[1]
            if pval > 0.05:
                stat_counter += 1
                if stat_counter >= max_iter:
                    plt.plot(means_df['time'], means_df['per'], color = 'k')
                    plt.vlines(j*sec, min(means_df['per']) - 0.01 , max(means_df['per']) + 0.01 , 'r', '--')
                    h = j*sec
                    return h
            elif stat_counter > 0:
                #pass
                stat_counter = 0
    plt.plot(means_df['time'], means_df['per'], color = 'k')
    plt.vlines(h, min(means_df['per']) - 0.01 , max(means_df['per']) + 0.01 , 'r', '--')
    plt.title(f'Slides = {sec} sec.\nFunc = {str(stat_func)}')
    plt.show()
    return -1
    #return h

path = 'results.json'
# Opening JSON file
with open(path) as json_file:
    data1 = json.load(json_file)
    
#find_criteria(data1, 30, stats.wilcoxon)


#%%
path = 'Downloads/results(7).json'

with open(path) as json_file:
    data = json.load(json_file)

yoda = [d for d in data if '6252' in d['subId']]
yoda = [d for d in yoda if '19' in d['createdAt']]


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

yoda = find_max(yoda)

find_criteria(yoda, 5, stats.ttest_rel, 6)
#find_criteria(yoda, 5, stats.wilcoxon, 6)




