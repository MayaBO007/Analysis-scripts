#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:53:52 2023

@author: maya
"""

import pandas as pd
import numpy as np
import pickle
import glob
import matplotlib.pyplot as plt
import math


filelist = glob.glob('all_data_**')

for file in filelist:
    try:
        spyFile = open(file,'rb')
        data = pickle.load(spyFile)
    except:
        continue
    if file == 'all_data_ET':
        et_data = pd.DataFrame(data)
        et_describe = et_data.describe()
        
    else:
        st_data = pd.DataFrame(data)
        st_describe = st_data.describe()
        

    #%%
# create bar plot

barWidth = 0.3

bars1 = [st_describe['nat_perc'][1], st_describe['dev_button_perc'][1], st_describe['nondev_button_perc'][1], st_describe['switch_perc'][1], st_describe['yellow_perc'][1], st_describe['yellow_accu'][1]]

bars2 = [et_describe['nat_perc'][1], et_describe['dev_button_perc'][1], et_describe['nondev_button_perc'][1], et_describe['switch_perc'][1], et_describe['yellow_perc'][1], et_describe['yellow_accu'][1]]

yer1 = [st_describe['nat_perc'][2]/math.sqrt(5), st_describe['dev_button_perc'][2]/math.sqrt(5), st_describe['nondev_button_perc'][2]/math.sqrt(5), st_describe['switch_perc'][2]/math.sqrt(5), st_describe['yellow_perc'][2]/math.sqrt(5), st_describe['yellow_accu'][2]/math.sqrt(5)]

yer2 = [et_describe['nat_perc'][2]/math.sqrt(5), et_describe['dev_button_perc'][2]/math.sqrt(5), et_describe['nondev_button_perc'][2]/math.sqrt(5), et_describe['switch_perc'][2]/math.sqrt(5), et_describe['yellow_perc'][2]/math.sqrt(5), et_describe['yellow_accu'][2]/math.sqrt(5)]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

plt.bar(r1, bars1, width = barWidth, color = 'm', edgecolor = 'black', yerr=yer1, capsize=7, label='ST')

plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer2, capsize=7, label='ET')

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['nat_perc', 'dev_button_perc', 'nondev_button_perc', 'switch_perc', 'yellow_perc', 'yellow_accu'], rotation = 90)
plt.ylabel('% of all options')
plt.legend()
 
# Show graphic
plt.show()

#%%
barWidth = 0.3

bars3 = [st_describe['rt_std'][1]]#, st_describe['rt_std'][1]]

bars4 = [et_describe['rt_std'][1]]#, et_describe['rt_std'][1]]

yer3 = [st_describe['rt_std'][2]/math.sqrt(5)]#, st_describe['rt_std'][2]/math.sqrt(5)]]

yer4 = [et_describe['rt_std'][2]/math.sqrt(5)]#, et_describe['rt_std'][2]/math.sqrt(5)]]
        
r3 = np.arange(len(bars3))
r4 = [x + barWidth for x in r3]

plt.bar(r3, bars3, width = barWidth, color = 'blue', edgecolor = 'black', yerr=yer3, capsize=7, label='ST')

plt.bar(r4, bars4, width = barWidth, color = 'cyan', edgecolor = 'black', yerr=yer4, capsize=7, label='ET')

# general layout
plt.xticks([r + barWidth for r in range(len(bars3))], ['rt_std'], rotation = 90)#, 'rt_std'], rotation = 90)
plt.ylabel('height')
plt.legend()
 
# Show graphic
plt.show()

#%%

import seaborn as sns
import pickle

# file = 'data_plot'
# dataForPlot = open(file,'rb')
# data_plot = pickle.load(dataForPlot)

# df = data_plot

# sns.barplot(data=df, x=df.index, y=df.index, hue='training')

df = sns.load_dataset("penguins")
sns.barplot(data=df, x="island", y="body_mass_g")


#%%
import plotly.express as px

px.bar(df, x=df.index, y=['ET','ST']).show()
