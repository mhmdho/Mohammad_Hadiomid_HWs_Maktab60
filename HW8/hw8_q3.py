# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:48:03 2021

@author: Lenovo
"""
# =============================================================================
#   Homework 8 - Question 3
# =============================================================================

import re  # import regex


def find_word_end(text, word):
    '''Enter your text and end word it return a message
    whether your text end with entry word or not'''
    answer = re.search(f'{word}$', text)
    if answer:
        print(f'Yes, your text end with "{word}"')
    else:
        print("No match found at the end of your text")


TXT = input('Enter your text:')
WORD = input('Enter your word:')
find_word_end(TXT, WORD)
# TXT = 'My name is Mohammad from Tehran'
