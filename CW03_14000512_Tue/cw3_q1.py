# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:40:57 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 3 - Question 1    (1400-05-12 - Tuesday)
# =============================================================================

# Max wire length between N houses

N = int(input("Number of houses:"))
HOUSES = []  # All houses coordinates
MAX_DISTANCE = 0

for i in range(N):
    HOUSES.append(tuple(map(int,
                            input(f"Enter house{i+1} coordinates:").split())))

for i in range(N):
    for j in range(i+1, N):
        DISTANCE = abs(HOUSES[i][0] - HOUSES[j][0]) +\
                    abs(HOUSES[i][1] - HOUSES[j][1])

        if DISTANCE > MAX_DISTANCE:
            max_coordinate = [HOUSES[i], HOUSES[j]]
            MAX_DISTANCE = DISTANCE


print('\nMaximum distance between two houses:', MAX_DISTANCE)
print('The cordinates of these two houses:', max_coordinate)
