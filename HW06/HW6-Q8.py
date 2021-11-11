# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:05:07 2021

@author: Lenovo
"""

def double_result(func): #Decorator
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        value2 = lambda v : v * 2
        print(f'  The function result is: {value}') #shows the function value
        print(f'  The double result is: {value2(value)}\n') #shows the function value after putting in decorator
        return value2(value)
    return wrapper

@double_result
def myFunction(a, b):
    return a+b

a1, a2 = map(int, input('Enter your TWO numbers [with space]:').split()) #gets 2 numbers from user
print(myFunction(a1, a2))
