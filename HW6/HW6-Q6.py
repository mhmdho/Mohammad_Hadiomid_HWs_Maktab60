# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:29:58 2021

@author: Lenovo
"""

List = [(19542209, 'New York') ,(4887871, 'Alabama'), (88566699, 'Tehran1400'), (111111, 'Ahvaz')]

List.reverse()
print('\nReversed list is:\n', List, "\n")

List.sort(key = lambda arg : arg[1][::-1]) #sort the list by the use of lambda
print('Sorted list is:\n', List)


'''
def func(Lst:list): #This function first show reversed list and then sort it
    Lst.reverse()
    print('\nReversed list is:\n', Lst, "\n")

    Lst.sort(key = lambda arg : arg[1][::-1]) #sort the list by the use of lambda
    print('Sorted list is:\n', Lst)

    return Lst

List = [(19542209, 'New York') ,(4887871, 'Alabama'), (88566699, 'Tehran1400'), (111111, 'Ahvaz')]
func(List) # you can give this function your list
'''
