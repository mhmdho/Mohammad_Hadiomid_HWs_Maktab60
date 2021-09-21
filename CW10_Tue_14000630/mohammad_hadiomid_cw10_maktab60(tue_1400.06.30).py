# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:38:24 2021

@author: Lenovo
"""
# =============================================================================
# الف ) برای ورودی های زیر regex مناسب بنویسید :
# ۱. نام و نام خانوادگی ( مثال : Mohammad Ahmadi )
# ۲. شماره تماس ( مثال : 09123456789 )
# ۳. ایمیل ( مثال : testmail@gmail.com )
# ۴.پسورد ( مثال : 1TsJustT3st )
# ۵. تاریخ تولد ( مثال : 1/2/1380 )
# ب)سن فردوارد شده را محاسبه و تعداد روزهای باقی مانده تا تولد فردرا حساب کنید.
# ج) زمان محاسبات را بدست آورید .
# =============================================================================
# =============================================================================
# Classwork 9 - (Tuesday 1400-06-30)
# =============================================================================

import re
from datetime import datetime
import time


def func_time(func):
    '''Decorator of function duration'''
    def wrapper(*args):
        start_time = time.time()
        value = func(*args)
        end_time = time.time()
        print('function duration:', end_time - start_time)
        return value
    return wrapper


@func_time
def name_validation(name):
    '''Check name and family format'''
    answer = re.findall(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", name)
    if answer:
        print(f"\n{name} (format is OK)")
    else:
        print(f"Invalid name format!")


@func_time
def moblie_validation(phone):
    '''Check mobile phone format'''
    matching = re.search(r"^09\d{9}$", phone)
    if matching:
        print(f'\n{phone} (format is OK)')
    else:
        print('\nInvalid phone format!')


@func_time
def email_validation(mail):
    '''Check email format'''
    matching = re.search(r'\b[A-Za-z0-9]{2,15}@[A-Za-z0-9]+\.[A-Za-z]{2,}\b',
                         mail)
    if matching:
        print(f'\n{mail} (format is OK)')
    else:
        print('\nInvalid email format!')


@func_time
def pass_validation(password):
    '''Check password format'''
    matching = re.search(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])'
        r'[A-Za-z\d@$!#%*?&]{6,20}$', password)
    if matching:
        print(f'\n{password} (format is OK)')
    else:
        print('\nInvalid pass format!')


@func_time
def birthdate_validation(birthdate):
    '''Check birthdate format'''
    matching = re.search(r'^(19[0-9][0-9]|20[01][0-9]|202[01])-(0[1-9]|1[012])'
                         r'-([0][1-9]|[12][0-9]|3[01])$',
                         birthdate)
    if matching:
        print(f'\n{birthdate} (format is OK)')
    else:
        print('\nInvalid birthdate format!')


@func_time
def age_cal(birthdate):
    '''return age and days remain to birthday'''
    noww = datetime.now()
    age = noww - datetime.strptime(birthdate, '%Y-%m-%d')
    age2 = age.days/365
    birthto = 365 - age.days % 365
    print(f'\nAge : {int(age2)}', f'\ndays to birthday : {birthto}')


name_validation('Mohmmad Ahmadi')
moblie_validation('09123456783')
email_validation('george@gmail.com')
pass_validation('Mypass@1390')
birthdate_validation('1988-02-19')
age_cal('1988-02-12')
