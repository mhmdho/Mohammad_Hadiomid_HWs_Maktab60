# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:58:31 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 2 - Question 2    (1400-05-07 - Thursday - part 1)
# =============================================================================

# summation of 2 arrays

N, M = map(int, input("Enter the dimension of matrix:").split())
A = []
B = []
C = []
# C = [[]] * N


for i in range(N):
    A.append(list(map(int, input(f"Enter array1 row{i+1} numbers:").split())))

for j in range(N):
    B.append(list(map(int, input(f"Enter array2 row{j+1} numbers:").split())))


# first way
for k in range(N):
    C.append([])
    for l in range(M):
        C[k].append(A[k][l] + B[k][l])
    print(*C[k])


# second way
# def func(num1, num2):
#    return num1 + num2
#
#
# for k in range(N):
#    C.append([])
#    C[k] = list(map(func, A[k], B[k]))
#    print(*C[k])


# third way
# def func(num1, num2):
#    return num1 + num2
#
#
# C = [list(map(func, A[k], B[k])) for k in range(N)]
# print(*C)
