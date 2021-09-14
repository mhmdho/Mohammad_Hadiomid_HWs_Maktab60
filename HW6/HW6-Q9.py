# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:43:50 2021

@author: Lenovo
"""

def get_next_multiple(n): #return the multiple of a number from the smallest one
    i = 1
    while True:
        yield n * i
        i += 1

get_multiple_of_number = get_next_multiple(int(input("Enter your number: ")))
print("\nmultiples of your number are:")
for i in range(4):      #show the first four multiples of entered number:
    print(next(get_multiple_of_number))


'''
for i in get_multiple_of_number:
    print(next(get_multiple_of_number))
    if next(get_multiple_of_number) > 100:
        #get_multiple_of_number.throw(ValueError("We don't like large numbers"))
        get_multiple_of_number.close()        
'''   
