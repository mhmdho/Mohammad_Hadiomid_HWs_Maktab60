# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:46:39 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 3    (1400-05-07 - Thursday - part 2)
# =============================================================================

# Eyesight test

N = int(input("Enter the number of words:"))
ANSWER = input("Enter the student answer:")
TEST = input("Enter the test answer:")
ERROR = 0

for i in range(N):
    if ANSWER[i] != TEST[i]:
        ERROR += 1
print(f"Errors: {ERROR}")
# print("Errors:", ERROR)
