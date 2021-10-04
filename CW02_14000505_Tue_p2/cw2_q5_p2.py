# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:52:01 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 5    (1400-05-05 - Tuesday - part 2)
# =============================================================================

# Array changes
Q = int(input("Enter the numbers of your operations:"))
L = []
for i in range(Q):
    o = input('Enter your operation number '+str(i+1)+': ').split()
    operation = o[0]
    index = int(o[1])-1
    if operation == "+":
        number = int(o[2])
        L.insert(index, number)
    else:
        L.pop(index)
    print(*L if bool(L) else ["Empty"])
