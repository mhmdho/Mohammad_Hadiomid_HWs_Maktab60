# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 01:10:38 2021

@author: Lenovo
"""
# =============================================================================
#   Homework 8 - Question 4
# =============================================================================

import re  # import regex


def find_num_a(text):
    '''Enter your text to check that it contains "A", "$" and num'''
#    if re.search("[0-9]", text)\
#        and re.search("[A]", text)\
#            and re.search("[$]", text):
    if re.search(r"(?=.*[0-9])(?=.*[A])(?=.*[$])", text):
        print('\nYes, your text contain all of "num", "A" and "$"')
    else:
        print('\nNo match, your text does not contains any'
              ' or all of "num", "A" and "$"')


# TXT = 'My name is Mohammad from block A with 96$'
TXT = input('Enter your text:')
find_num_a(TXT)
