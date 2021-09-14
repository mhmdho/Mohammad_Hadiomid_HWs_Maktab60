# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:02:36 2021

@author: Lenovo
"""

import os
allfiles = []
address = str(input('Enter your directory path:'))
#address = 'C:/Users/Lenovo/Documents/Mine/Data science/Maktab sharif/HW6/'
for files in os.listdir(address):
    if os.path.isfile(os.path.join(address, files)):
        allfiles.append(files)

class SkipThisFile(Exception):
    pass

def read_lines(fl):    
    for file in fl:
        yield file

def display_files(fl):
        source = read_lines(fl)
        for line in source:
            print(line, end='')
            inp = input()
            if inp == 'n':
                print('NEXT')
                source.throw(SkipThisFile)
                #break
                #source.close()
                #next(source)

def Reader(*files):
    print('Files name in this path:')    
    print(*files, sep='\n', end='\n')
    for file in files:
        try:    
            with open(file) as f:
                print(f'\n---> Open file: ({file}) <---\n')
                display_files(f)
        except:
            print('---This file closed...---')
            pass

Reader(*allfiles)
