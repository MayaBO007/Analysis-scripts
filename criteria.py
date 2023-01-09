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

def find_criteria(path, sec, stat_func):
    # Opening JSON file
    with open(path) as json_file:
        data = json.load(json_file)
    
    cars = np.array(data['allChoices'])
    press = np.array(data['allCorrectFirstPress'])
    
    #sec = 30#int(input('Seconds to slide on: '))
    dt = 1000 * sec
    max_time = max(max(cars), max(press))
    
    means_dict = {'time': [], 'per': []}
    h = 0
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
            if stat_func(means_df['per'][j-(60//sec-1):j-(30//sec-1)] , means_df['per'][j-(30//sec-1):])[1] > 0.05:
                plt.plot(means_df['time'], means_df['per'], color = 'k')
                #plt.vlines(j*sec,0.65,0.75, 'r', '--')
                #return True, j
                h = j*sec
    plt.plot(means_df['time'], means_df['per'], color = 'k')
    plt.vlines(h,0.65,0.75, 'r', '--')
    plt.title(f'Slides = {sec} sec.')
    #return False
        #if j < 90//sec:
        #    pvals.append(1)
        #else:
            #p_val = stats.ttest_rel(means_df['per'][j-(60//sec-1):j-(30//sec-1)] , means_df['per'][j-(30//sec-1):])[1]
            #p = 0.65 if p_val < 0.05 else 0.8
            #pvals.append(p)

    #plt.plot(means_df['time'], means_df['per'])
    #plt.plot(means_df['time'], pvals)

find_criteria('results.json', 30, stats.wilcoxon)
