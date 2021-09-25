# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:34:39 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 1 - Question 1    (1400-04-31 - Thursday - part 2)
# =============================================================================

# define the form of water based on the entry temperature
TEMPERATURE = int(input('Enter the temperature:'))
if TEMPERATURE > 100:
    print("Steam")
elif TEMPERATURE < 0:
    print("Ice")
else:
    print("Water")
