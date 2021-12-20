# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:10:38 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 3 - Question in Telegram    (1400-05-12 - Tuesday)
# =============================================================================

# =============================================================================
# Get text and count upper case and lower case letters. Then put them as values
# in a dictionary with the keys of upper_case and lower_case.
# =============================================================================


STRING = input('Enter your text: ')
CASE_COUNT = {'upper_case': 0, 'lower_case': 0}

for i in STRING:
    if i == ' ':
        pass
    elif i == i.upper():
        CASE_COUNT['upper_case'] += 1
    else:
        CASE_COUNT['lower_case'] += 1

print(CASE_COUNT)
