# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:38:56 2021

@author: Lenovo
"""

print('\n ......Question 3...... \n')
import os
allfiles_count = 0
allfolders_count = 0
address = str(input('Enter your directory path:'))
for root, directories, files in os.walk(address):
    for f in files:
        allfiles_count += 1
    for d in directories:
        allfolders_count += 1
print(f'Number of all files = {allfiles_count}')
print(f'Number of folders and subfolders = {allfolders_count}')
