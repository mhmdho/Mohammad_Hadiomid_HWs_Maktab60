# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:38:56 2021

@author: Lenovo
"""
 
print('\n ......Question 4...... \n')
lines = []
import os
#address = 'C:/Users/Lenovo/Documents/Mine/Data science/Maktab sharif/HW4/test'
address = str(input('Enter your directory path:')+'//')
with open(address+'new_file.txt', 'w+') as writer:
    for files in os.listdir(address):
        if os.path.isfile(address+files):
            with open(address+files, 'r') as reader:
                a = reader.readlines()
                lines.extend(a)
    lines.sort()
    writer.writelines(lines)

print('\nThe 5 second lines is:\n')
with open(address+'new_file.txt', 'r') as reader:
    lines = reader.readlines()
    for l in lines:
        print(l, end='')
