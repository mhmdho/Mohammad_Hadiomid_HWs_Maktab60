# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:01:51 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 1    (1400-05-07 - Thursday - part 1)
# =============================================================================

# Greatest common divisor (GCD)
# This exercise returns multiple of all prime number less than N(entry number)


def gcd(num1, num2):
    '''calsulate GCD of num1 and num2'''
    for i in range(max(num1, num2)):
        ans = max(num1, num2) - i
        if num1 % ans == 0 and num2 % ans == 0:
            break
    return ans


def lcm(num1, num2):
    '''calsulate LCM of num1 and num2'''
    return int(num1 * num2 / gcd(num1, num2))


ANSWER = 1
N = int(input("Enter your number:"))
for j in range(N):
    if gcd(j, N) == 1:
        ANSWER = lcm(ANSWER, j)
print(ANSWER)
