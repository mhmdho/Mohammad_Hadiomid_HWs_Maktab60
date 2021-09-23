# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:58:04 2021

@author: Lenovo
"""
# =============================================================================
# Classwork 9 - (Fridsay 1400-06-26 part 2)
# Use of: ^ \ * + ? \w \w \d \D \s \S \A \Z \b \B *? +? ??
# =============================================================================

import re

TXT = 'This is my email: hadiomid@gmail.com, My phone number is +98935'

# start with ...
print(re.search('^This', TXT))
print(re.search('^hadi', TXT))

# Signals/escape a special sequence/char
print(re.search(r"mail\.", TXT))

# Zero or more
print(re.search('h*is', TXT))

# 1 or more
print(re.search('email+', TXT))

# "g" is optional
print(re.search('g?mail', TXT))

# return match if num, char or _
print(re.search(r'\wmail', TXT))

# return match if . @ # ... and not char word
print(re.search(r'\Wgmail', TXT))

# return match if num
print(re.search(r'\d3', TXT))

# return match if not num
print(re.search(r'\Dom,', TXT))

# return match if contains space
print(re.search(r'\sis', TXT))

# return match if not contains space
print(re.search(r'\Smail', TXT))

# return if begin with...
print(re.search(r'\AT', TXT))

# return if end with...
print(re.search(r'935\Z', TXT))

# both at the end or begining of word
print(re.search(r'\bmail', TXT))

# not end or begining or a word
print(re.search(r'\Bmail', TXT))

# The non-greedy versions of *, +, and ?
print(re.search('phon*?', TXT))
print(re.search('ph+?', TXT))
print(re.search('phone??', TXT))
