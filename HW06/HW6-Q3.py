# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:03:46 2021

@author: Lenovo
"""

List = [ -1000, 500, -600, 700, 5000, -90000, -175000]

newlist = list(filter(lambda arg : arg < 0 , List)) #first filter negetive component
newlist = list(map( lambda arg : -arg, newlist)) #then change them to positive number
print('\nNegative components which are changed to positive:\n', newlist)


'''
def flt_minus(lst):
    #filter component which changed to positive in one line
    newlist = list(filter(lambda arg : arg != False, list(map( lambda arg : -arg if arg < 0 else False, List))))
    print(newlist)
    return newlist
flt_minus(List)
'''
