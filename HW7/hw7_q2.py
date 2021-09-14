# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:54:03 2021

@author: Lenovo
"""
# =============================================================================
# HOMEWORK 7 - QUESTION 2
# =============================================================================


import hw7_q1 as Q1

BA0 = Q1.BankAccount('Mahdi', 75)
BA1 = Q1.BankAccount('Mohammad', 100)
BA2 = Q1.BankAccount('Ali', 2000)

print(BA0)
print(BA1)
print(BA2)

BA1.deposit(731)
BA2.deposit(500)

BA1.withdraw(732)
BA2.withdraw(900)

BA2.transfer(BA1, 1473)
BA1.transfer(BA2, 2600)
