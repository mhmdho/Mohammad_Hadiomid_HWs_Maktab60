# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:45:32 2021

@author: Lenovo
"""

def only_even_parameters(func): #Decorator
    def wrapper(*args):
        value = func(*args)
        for arg in args:
            try:
                if arg % 2 != 0: #check number to be even
                    raise Exception #if the number is not even the exception will raise
            except Exception:
                return f'Please only Enter EVEN numbers!' #if one of the input number is odd, the exception shows this error
        else:
            print(f'\nBoth numbers are Even, The sum is: {value}')
            return value
    return wrapper

@only_even_parameters
def myFunction(a, b):
    return a+b

a1, a2 = map(int, input('Enter your TWO EVEN numbers [with space]:').split()) #gets 2 numbers from user
print(myFunction(a1, a2))
