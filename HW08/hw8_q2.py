# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:04:01 2021

@author: Lenovo
"""
# =============================================================================
#   Homework 8 - Question 2
# =============================================================================

from datetime import datetime


def date_show(year, month, day):
    '''Change entry date to weekday-month-year
    Enter your date like   ->   2018, 6, 21'''
    entry = datetime(year, month, day)  # change entry to datetime format
    return entry.strftime("%A - %B - %Y")  # get wanted format


YEAR, MONTH, DAY = map(int, input('Enter date like-> 2021/09/19: ').split('/'))
print('\n', date_show(YEAR, MONTH, DAY))
