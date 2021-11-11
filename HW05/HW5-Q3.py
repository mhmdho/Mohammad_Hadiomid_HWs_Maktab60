# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:07:38 2021

@author: Lenovo
"""

def print_list_element(thelist, index):
    while True:
        try:
            thelist[int(index)]
            if int(index) < len(thelist) or type(int(index)) == int:
                break
        except IndexError: # check the index be in range
            print('The index is out of RANGE!')
            index = input('Enter correct index:')
        except ValueError: # check the index not be a character
            print('The index must be a NUMBER!')
            index = input('Enter correct index:')

    print(f'Index {index} of the list is:', thelist[int(index)])

l = input('Enter your list Elemnt wiht SPACE:').split()
i = input('Enter list INDEX:')
print_list_element(l, i)
