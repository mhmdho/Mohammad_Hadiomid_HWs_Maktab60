# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:57:54 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 3    (1400-05-05 - Tuesday - part 1)
# =============================================================================

# Xbar
while True:
    N = int(input("Enter your number:"))
    if N == 0:
        break
    for i in range(1, N+1):
        print(N)


# Xbar (2nd way)
L = []
while True:
    N = int(input("Enter your number:"))
    L.append(N)
    if N == 0:
        break
for i in L:
    for j in range(i):
        print(i)
