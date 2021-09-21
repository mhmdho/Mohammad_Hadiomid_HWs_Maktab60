# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 15:08:23 2021

@author: Lenovo
"""
# =============================================================================
#   Homework 8 - Question 5
# =============================================================================

import re  # import regex


def validation_phone_number(phone):
    ''' Enter your mobile phone number to check validation '''
    answer = re.search(r"^(0098|098|98|0|00|\+0098|\+098|\+98)9[0-9]{9}$",
                       phone)
    if answer:
        answer = re.search("9[0-9]{9}$", phone)  # get last 10 digit
        mobile = f"{0}{answer.group()}"  # add 0 at the begining
    else:
        mobile = f"Invalid Phone Number!"
    return mobile


MOBILE = input('Enter your phone number: ')
print(validation_phone_number(MOBILE))
