# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:50:13 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 1    (1400-05-05 - Tuesday - part 1)
# =============================================================================

# factorial:
N = int(input("Enter your number:"))
FACTORIAL = 1
for i in range(1, N+1):
    FACTORIAL = FACTORIAL * i

print(f" {N}! = ", FACTORIAL)
