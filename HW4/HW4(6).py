# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:38:56 2021

@author: Lenovo
"""

print('\n ......Question 6...... \n')
import os
import shutil
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

source_address = str(input('Enter your source directory path:')+'//')
destination_address = str(input('Enter your destination directory path:')+'//')
print('\n')

for files in os.listdir(source_address):
    if os.path.isfile(source_address+files):
        if 'a' in files:
            with open(source_address + files, 'r') as reader:
                if is_ascii(reader.read()):
                    shutil.copyfile(source_address+files, destination_address+files)
                    print(f'({files}) has been copied in new destination')
                else:
                    print(f'({files}) contain (a) but is not ascii')
        else:
            print(f'(a) is not in ({files}) name')
