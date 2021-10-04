# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:44:17 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 4    (1400-05-05 - Tuesday - part 2)
# =============================================================================

# sum of 2 array:
N = int(input("Enter the length of your arrays:"))
A = input("Enter your 1st array numbers:").split()
B = input("Enter your 2nd array numbers:").split()
C = []

if len(A) == len(B) == N:
    for i in range(N):
        A[i] = int(A[i])
        B[i] = int(B[i])
        C.append(A[i] + B[i])
    print(A)
    print(B)
    print(C)
else:
    print(f"The numbers in array is not equal to {N}")
