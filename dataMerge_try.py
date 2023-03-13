#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:08:15 2023

@author: maya
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy import stats
import glob
import pickle


#def get_data (  ):
filelist = glob.glob('ST***')

all_data_ST = pd.DataFrame()
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
    if data['devButton'][0] == 0:
        dev_color = 'Blue'
        dev_color_all = 'blue'
        nondev_color = 'Red'
        nondev_color_all = 'red'
    else:
        dev_color = 'Red'
        dev_color_all = 'red'
        nondev_color = 'Blue'
        nondev_color_all = 'blue'
    
    allFirstPress = data['correctFirstBluePress'] + data['correctFirstRedPress']
    
    for item in allFirstPress:
        list_under_press = np.array(data['allChoices'])[np.array(data['allChoices']) < item]
        rt_list.append(item - max(list_under_press))
        # rt_data = {
        #     #"sub_id": data['subId'],
        #     "rt_mean": np.mean(rt_list),
        #     "rt_std": np.std(rt_list)
        #     }

    if data['subId']== '63bebcb47c10d146b25b5873' or data['subId']== '63bebcb97c10d146b25b5874':
        user_data = {
            'training': 0,
            "nat_perc": (len([i for i in data['correctFirst{}Press'.format(dev_color)] if i >= 180000])+len([i for i in data['correctFirst{}Press'.format(dev_color)] if i >= 180000]))/len([i for i in data['allChoices'] if i >= 180000]),
            "nat_dev_button_perc": (len(data['correctFirst{}Press'.format(dev_color)]))/len(data['{}Choice'.format(dev_color_all)]),
#            "nat_perc": (len(data['correctFirstBluePress'])+len(data['correctFirstRedPress']))/len(data['allChoices']),
            "nat_nondev_button_perc": (len(data['correctFirst{}Press'.format(nondev_color)]))/len(data['{}Choice'.format(nondev_color_all)]),
            "dev_tot_perc": (len(data['correctBluePressDevtest'])+len(data['correctRedPressDevtest']))/len(data['allChoicesDev']),
            "dev_button_perc": (len(data['correct{}PressDevtest'.format(dev_color)]))/len(data['{}ChoiceDev'.format(dev_color_all)]),
            "nondev_button_perc": (len(data['correct{}PressDevtest'.format(nondev_color)]))/len(data['{}ChoiceDev'.format(nondev_color_all)]),
            "switch_perc": (len(data['correctFirstBluePressSwitch'])+len(data['correctFirstRedPressSwitch']))/len(data['allChoicesSwitch']),
            "yellow_perc": (len(data['correctFirstBluePressYellow'])+len(data['correctFirstRedPressYellow']))/len(data['allChoicesYellow']),
            "yellow_accu": int(data['howManyYellows'][0])/len(data['yellowChoiceYellow']),
            # "rt_mean": np.mean(rt_list),
            # "rt_std": np.std(rt_list)
            }    
    else:
        user_data = {
            'training': 0,
            "nat_perc": (len([i for i in data['correctFirst{}Press'.format(dev_color)] if i >= 180000])+len([i for i in data['correctFirst{}Press'.format(dev_color)] if i >= 180000]))/len([i for i in data['allChoices'] if i >= 180000]),
#            "nat_perc": (len(data['correctFirstBluePress'])+len(data['correctFirstRedPress']))/len(data['allChoices']),
            "nat_dev_button_perc": (len(data['correctFirst{}Press'.format(dev_color)]))/len(data['{}Choice'.format(dev_color_all)]),
            "nat_nondev_button_perc": (len(data['correctFirst{}Press'.format(nondev_color)]))/len(data['{}Choice'.format(nondev_color_all)]),
            "dev_tot_perc": (len(data['correctFirstBluePressDevtest'])+len(data['correctFirstRedPressDevtest']))/len(data['allChoicesDev']),
            "dev_button_perc": (len(data['correctFirst{}PressDevtest'.format(dev_color)]))/len(data['{}ChoiceDev'.format(dev_color_all)]),
            "nondev_button_perc": (len(data['correctFirst{}PressDevtest'.format(nondev_color)]))/len(data['{}ChoiceDev'.format(nondev_color_all)]),
            "switch_perc": (len(data['correctFirstBluePressSwitch'])+len(data['correctFirstRedPressSwitch']))/len(data['allChoicesSwitch']),
            "yellow_perc": (len(data['correctFirstBluePressYellow'])+len(data['correctFirstRedPressYellow']))/len(data['allChoicesYellow']),
            "yellow_accu": int(data['howManyYellows'][0])/len(data['yellowChoiceYellow']),
            # "rt_mean": np.mean(rt_list),
            # "rt_std": np.std(rt_list)
        }
        
#    user_data = pd.merge(user_data, rt_data)
    all_data_ST = all_data_ST.append(user_data, ignore_index=True)
  #  all_data_ST = all_data_ST.append(rt_data, ignore_index=True)
    all_data_ST['nondev_button_perc'][1] = 1    
        
    spyFile.close() 
    

file = open('all_data_ST', 'wb')
pickle.dump(all_data_ST, file)    
    # pd.dataframe 
    
    # df = fd.append
    #%%
    
filelist = glob.glob('ET***')

all_data_ET = pd.DataFrame()

for file in filelist:
    try:
 #      spyFile = open(f'{file}','rb')
       spyFile = open(file,'rb')
   #    print(spyFile.readline())
       data = pickle.load(spyFile)
      # load_dictionary(spyFile)
    except:
        continue
    if data['devButton'][0] == 0:
        dev_color = 'Blue'
        dev_color_all = 'blue'
        nondev_color = 'Red'
        nondev_color_all = 'red'
    else:
        dev_color = 'Red'
        dev_color_all = 'red'
        nondev_color = 'Blue'
        nondev_color_all = 'blue'
    allFirstPress = data['correctFirstBluePress'] + data['correctFirstRedPress']
    
    for item in allFirstPress:
        list_under_press = np.array(data['allChoices'])[np.array(data['allChoices']) < item]
        rt_list.append(item - max(list_under_press))

    user_data = {
            'training': 1,
            "nat_perc": (len([i for i in data['correctFirst{}Press'.format(dev_color)] if i >= 180000])+len([i for i in data['correctFirst{}Press'.format(dev_color)] if i >= 180000]))/len([i for i in data['allChoices'] if i >= 180000]),
#            "nat_perc": (len(data['correctFirstBluePress'])+len(data['correctFirstRedPress']))/len(data['allChoices']),
            "nat_dev_button_perc": (len(data['correctFirst{}Press'.format(dev_color)]))/len(data['{}Choice'.format(dev_color_all)]),
            "nat_nondev_button_perc": (len(data['correctFirst{}Press'.format(nondev_color)]))/len(data['{}Choice'.format(nondev_color_all)]),
            "dev_tot_perc": (len(data['correctFirstBluePressDevtest'])+len(data['correctFirstRedPressDevtest']))/len(data['allChoicesDev']),
            "dev_button_perc": (len(data['correctFirst{}PressDevtest'.format(dev_color)]))/len(data['{}ChoiceDev'.format(dev_color_all)]),
            "nondev_button_perc": (len(data['correctFirst{}PressDevtest'.format(nondev_color)]))/len(data['{}ChoiceDev'.format(nondev_color_all)]),
            "switch_perc": (len(data['correctFirstBluePressSwitch'])+len(data['correctFirstRedPressSwitch']))/len(data['allChoicesSwitch']),
            "yellow_perc": (len(data['correctFirstBluePressYellow'])+len(data['correctFirstRedPressYellow']))/len(data['allChoicesYellow']),
            "yellow_accu": 1-((len(data['yellowChoiceYellow'])-int(data['howManyYellows'][0]))/len(data['yellowChoiceYellow']))
            # "rt_mean": np.mean(rt_list),
            # "rt_std": np.std(rt_list)
        }

    all_data_ET = all_data_ET.append(user_data, ignore_index=True)
        
    spyFile.close() 
    
file = open('all_data_ET', 'wb')
pickle.dump(all_data_ET, file)     

#%%
import math

df1 = pd.DataFrame()
et_mean = all_data_ET.mean()
st_mean = all_data_ST.mean()
st_str = all_data_ST.std()/math.sqrt(5)
et_str = all_data_ET.std()/math.sqrt(5)

df1 = df1.append(st_mean, ignore_index=True)
df1 = df1.append(et_mean, ignore_index=True)
df1 = df1.append(st_str, ignore_index=True)
df1 = df1.append(et_str, ignore_index=True)

# df1 = df1.T
# df1 = df1.rename(columns={0:"ST", 1:"ET", 2:"ST_STR", 3:"ET_STR"})

file = open('data_plot', 'wb')
pickle.dump(df1, file)     