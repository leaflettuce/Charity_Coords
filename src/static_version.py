# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 07:28:12 2019

@author: andyj
"""
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
 
# import data
df = pd.read_csv('./data/test.csv')
df_edit = df.drop('category', axis = 1)
df_cats = df.drop('name', axis = 1)
# Make the plot
parallel_coordinates(df_cats, 'category', colormap=plt.get_cmap("Set2"))
plt.show()

