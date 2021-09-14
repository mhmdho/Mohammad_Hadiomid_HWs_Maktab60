# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:44:35 2021

@author: Lenovo
"""

List = ["Jane", "Lee", "Will", "Brie"]

newlist = list(map(lambda arg : ("Hello " + arg), List )) #here lambda add "Hello" to the begining of each component
print('\nHello added:\n', newlist)


'''
def ls(List):
    newlist = list(map(lambda arg : ("Hello " + str(arg)), List ))
    print(newlist)
    return newlist

List = ["Jane", "Lee", "Will", "Brie", 1]
ls(List)
'''
