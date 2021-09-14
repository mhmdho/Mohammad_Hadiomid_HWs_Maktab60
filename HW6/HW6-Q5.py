# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:39:19 2021

@author: Lenovo
"""

List_1 = [100, 200, 300, 400, 500]
List_2 = [1, 10, 100, 1000, 10000]

list3 = list(map(lambda arg1, arg2 : arg1+arg2, List_1,List_2)) #lambda is used to sum component of 2 lists
print('\nSum of two lists:\n', list3)


'''
def func(List1, List2): 
    list3 = list(map(lambda arg1, arg2 : arg1+arg2, List_1,List_2)) #lambda is used to sum component of 2 lists
    print('\nSum of your two lists:\n', list3)
    return list3

List_1 = [100, 200, 300, 400, 500]
List_2 = [1, 10, 100, 1000, 10000]
func(List_1, List_2) #you can give your 2 lists to this function
'''
