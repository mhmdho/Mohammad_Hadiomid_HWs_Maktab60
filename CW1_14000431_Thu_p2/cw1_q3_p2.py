# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:55:48 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 1 - Question 3    (1400-04-31 - Thursday - part 2)
# =============================================================================

# Compare reverse of two three-digit numbers
NUM1 = input("please enter your 1st number:")
NUM2 = input("please enter your 2nd number:")
REV_NUM1 = int(NUM1[::-1])
REV_NUM2 = int(NUM2[::-1])

if REV_NUM1 < REV_NUM2:
    print('\n', NUM1 + " < " + NUM2)
elif REV_NUM1 > REV_NUM2:
    print('\n', NUM2 + " < " + NUM1)
else:
    print('\n', NUM1 + " = " + NUM2)
