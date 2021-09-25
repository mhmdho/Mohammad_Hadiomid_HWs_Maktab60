# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:47:21 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 1 - Question 2    (1400-04-31 - Thursday - part 2)
# =============================================================================

# Find the max of 4 numbers
NUM1 = int(input("Please enter your 1st number: "))
NUM2 = int(input("Please enter your 2nd number: "))
NUM3 = int(input("Please enter your 3rd number: "))
NUM4 = int(input("Please enter your 4th number: "))

MAX = NUM1
if NUM2 > MAX:
    MAX = NUM2
if NUM3 > MAX:
    MAX = NUM3
if NUM4 > MAX:
    MAX = NUM4
print(MAX)
