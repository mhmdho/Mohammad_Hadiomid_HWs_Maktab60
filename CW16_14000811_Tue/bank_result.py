# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:25:24 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 16 - Result of Model    (1400-08-11 - Tuessday)
# =============================================================================

from bank import BankAccount
from datetime import datetime

BA_MAHDI = BankAccount('Mahdi', 75)
BA_MOHAMMAD = BankAccount('Mohammad', 100)
BA_ALI = BankAccount('Ali', 2000)

print(BA_MAHDI)
print(BA_MOHAMMAD)
print(BA_ALI)

BA_MOHAMMAD.deposit(731)
BA_ALI.deposit(500)
BA_MOHAMMAD.withdraw(32)
BA_ALI.withdraw(900)
BA_ALI.transfer(BA_MOHAMMAD, 1473)
BA_MOHAMMAD.transfer(BA_MAHDI, 1600)

print('\n', *BA_MAHDI.history, sep='\n\n')
print('\n', *BA_MOHAMMAD.history, sep='\n\n')
print('\n', *BA_ALI.history, sep='\n\n')

BA_MOHAMMAD.tr_time(datetime.now().strftime("%Y-%b-%d %H:%M"))
BA_ALI.tr_time('2021-sep-19 18:20')
BA_MOHAMMAD.tr_time('2021-sep-19 18:20')
