# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:27:18 2021

@author: Lenovo
"""

import unittest
from bank import BankAccount


class BankTest(unittest.TestCase):
    ''' Test bank accounts to work correct'''
    def setUp(self):
        '''define bank accounts'''
        self.account = BankAccount('Ali', 1000)
        self.account2 = BankAccount('Hasan', 100)

    def test_deposit(self):
        ''' Test bank accounts deposit'''
        self.assertEqual(self.account.balance, 1000)
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        ''' Test bank accounts withdraw'''
        self.assertEqual(self.account.balance, 1000)
        self.account.withdraw(400)
        self.assertEqual(self.account.balance, 600)

    def test_transfer(self):
        ''' Test bank accounts transfer'''
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(self.account2.balance, 100)
        self.account.transfer(self.account2, 300)
        self.assertEqual(self.account.balance, 700)
        self.assertEqual(self.account2.balance, 400)

    def test_min_balance(self):
        ''' Test bank accounts minimum balance'''
        self.assertEqual(self.account.balance, 1000)
        self.account.withdraw(950)
        self.assertGreaterEqual(self.account.balance, 100)
