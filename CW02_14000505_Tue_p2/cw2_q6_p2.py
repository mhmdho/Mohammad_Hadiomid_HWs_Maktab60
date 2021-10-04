# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:01:20 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 6    (1400-05-05 - Tuesday - part 2)
# =============================================================================

# Making sequence
L, R = input("Enter the begining and end of your sequence:").split()
L, R = int(L), int(R)

SEQUENCE = "10"
while len(SEQUENCE) < R:
    SEQUENCE += SEQUENCE[::-1]

print(SEQUENCE)
print(SEQUENCE[L-1:R])
