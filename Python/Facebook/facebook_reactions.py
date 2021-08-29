#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:38:39 2021

@author: robbyjeffries

This file creates a graph, showing my frequency of Facebook likes and
comments per month
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read the json file into a dataframe
df = pd.read_json('/Users/robbyjeffries/my_reactions.json')

print(df.head(3))

# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)
print(df.head(3))

# drop some unnecessary columns
df = df.drop(['title'], axis=1)

# making sure it's datetime format
pd.to_datetime(df['date'])

print(df.head(3))

print(df.shape)
print(df.tail(3))

# figure out how many posts occured each month
df = df.set_index('date')
post_counts = df['data'].resample('MS').size()
print(post_counts)

## Plot the results!

# set figure size and font size
sns.set(rc={'figure.figsize':(8,6)})
sns.set(font_scale=1.5)

# set x labels
x_labels = post_counts.index

# create bar plot
sns.barplot(x_labels, post_counts, color='blue')

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=12)

# reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

# display the plot
plt.show()
