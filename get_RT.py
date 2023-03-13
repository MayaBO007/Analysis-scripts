#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:12:11 2023

@author: maya
"""

import pandas as pd
import numpy as np
import pickle
import glob
import matplotlib.pyplot as plt
import math


filelist = glob.glob('ST***')

rt_data = pd.DataFrame()
rt_list = []


for file in filelist:
    try:
 #      spyFile = open(f'{file}','rb')
       spyFile = open(file,'rb')
   #    print(spyFile.readline())
       data = pickle.load(spyFile)
      # load_dictionary(spyFile)
    except:
        continue
    allFirstPress = data['correctFirstBluePress'] + data['correctFirstRedPress']

    for item in allFirstPress:
        list_under_press = np.array(data['allChoices'])[np.array(data['allChoices']) < item]
        rt_list.append(item - max(list_under_press))
        rt_data = {
            "rt_mean": np.mean(rt_list),
            "rt_std": np.std(rt_list)
            }

file = open('all_data_ST', 'rb')
data_st = pickle.load(file)
all_data_ST = all_data_ST.append(rt_data, ignore_index=True)
pickle.dump(all_data_ST, file) 