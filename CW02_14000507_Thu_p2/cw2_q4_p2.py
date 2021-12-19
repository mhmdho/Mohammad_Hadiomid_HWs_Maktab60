# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:59:48 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 4    (1400-05-07 - Thursday - part 2)
# =============================================================================

# Xanduba challenge

BAG = []

N = int(input("Enter number of operations:"))
for i in range(N):
    operation = input("Enter your operation:").split()
    if operation[0] == "add":
        BAG.append(int(operation[1]))
        BAG.sort()
    else:
        print(BAG[int(operation[1])-1])
