#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:32:30 2021

@author: robbyjeffries

In this script, I will predict how many gold medals Team USA will win
during Tokyo 2020. 

The gold medal count per year will be imported from a .csv file, and
statistical methods will be used to predict the medal count for the
2020 games.
"""
import sys
print(sys.version)
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Save the csv to a dataframe variable
df = pd.read_csv("usa_gold_medals_by_year.csv")

# Display the shape of the data
print("\nDataframe (rows, columns) =",df.shape, "\n")

# Print the first 5 rows of data to ensure that the file imported correctly
print(df.head(5))

# Save the Gold Medal Count to an array
golds = df.to_numpy()

X = np.array(df)[:,0].reshape(-1,1)
y = np.array(df)[:,1].reshape(-1,1)

print("X=")
print(X)
print("y=")
print(y)

# Define the X position for 2020 medals to be predicted
to_predict_x = [2020]
to_predict_x = np.array(to_predict_x).reshape(-1,1)

# Fit a straight line to (X,y)
regsr = LinearRegression()
regsr.fit(X,y)

# Predict 2020 gold medal count
predicted_y = regsr.predict(to_predict_x)
m = regsr.coef_
c = regsr.intercept_
print("\nPredicted y: ", predicted_y)
print("slope (m): ", m)
print("y-intercept (c): ", c)

plt.title('Predict Team USAs gold medal count in Tokyo')  
plt.xlabel('Year of Summer Games')  
plt.ylabel('Number of Gold Medals') 
plt.scatter(X,y,color="blue")
new_y=[ m*i+c for i in np.append(X,to_predict_x)]
new_y=np.array(new_y).reshape(-1,1)
plt.plot(np.append(X,to_predict_x),new_y,color="red")
plt.show()





