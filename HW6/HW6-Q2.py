# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:48:43 2021

@author: Lenovo
"""

List = [ 1000, 500, 600, 700, 5000, 90000, 175000]

newlist = list(map(lambda arg : (arg + 2000) if arg <= 8000 else arg, List )) #add 2000 to each component which is less than 8000
print(newlist)


'''
def plus_2000(lst):
    newlist = list(map(lambda arg : (arg + 2000) if arg <= 8000 else arg, List ))
    print(newlist)
    return newlist
plus_2000(List)
'''
