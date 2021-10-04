# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:56:43 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 2    (1400-05-05 - Tuesday - part 1)
# =============================================================================

# Multiplication table:
N = int(input("Enter your number:"))
for i in range(1, N+1):
    for j in range(1, N+1):
        print(i*j, end="\t")
    print("\n")
