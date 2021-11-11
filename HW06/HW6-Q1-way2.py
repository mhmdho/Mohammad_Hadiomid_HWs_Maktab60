# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:02:36 2021

@author: Lenovo
"""
import os
allfiles = []
#address = str(input('Enter your directory path:')+'//')
address = 'C:/Users/Lenovo/Documents/Mine/Data science/Maktab sharif/HW6/ali/'
for file in os.listdir(address):
    if os.path.isfile(os.path.join(address, file)):
        allfiles.append(file)

class SkipThisFile(Exception):
    pass

def read_lines(*files):
    i = 0
    for file in files:
        i += 1
        print(f'\n---> open file: ({file}) <---\n')
        try:    
            with open(address+file, "r") as f:
                yield f.readlines()
        except Exception:
            print('---This file closed---')
            pass

def display_files(*files):
        print('List of files:')    
        print(*files, sep='\n', end='\n')
        source = read_lines(*files)
        for file in source:
            for line in file:
                print(line, end='')
                inp = input()
                if inp == 'n':
                    print('<NEXT>')
                    break
                    source.throw(SkipThisFile)
                    #source.close()
                    #next(source)

display_files(*allfiles)
