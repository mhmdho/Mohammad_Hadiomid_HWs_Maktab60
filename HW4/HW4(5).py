# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:38:56 2021

@author: Lenovo
"""

print('\n ......Question 5...... \n')
import os
address = str(input('Enter your directory path:'))
if not os.path.isdir(address):
    os.mkdir(address)
    print('\nThe new folder has been created.')
else:
    print('\nThis folder was created before!')
