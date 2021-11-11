# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:06:31 2021

@author: Lenovo
"""

import pandas as pd
df=pd.read_csv('C:/Users/Lenovo/Documents/Mine/Data science/Maktab sharif/HW5/Book1.csv', sep = ";") #read csv file

df2 = pd.DataFrame() #creat a dataframe for new file
df2['New column1'] = df.iloc[:,0] #copy first column of old scv to first column of new dataframe
df2['New column2'] = df.iloc[:,2] #copy third column of old scv to second column of new dataframe
df2['New column3'] = df.iloc[:,1] #copy second column of old scv to third column of new dataframe
df2['summation'] = df2.sum(axis=1) #summation of three columns

df2.to_csv('C:/Users/Lenovo/Documents/Mine/Data science/Maktab sharif/HW5/Book1(new).csv', index=False) #save new csv file

print(df)
print(df2)