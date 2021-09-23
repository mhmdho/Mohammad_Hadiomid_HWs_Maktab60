# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:13:13 2021

@author: Lenovo
"""
# =============================================================================
#  HOMEWORK 8 - QUESTION 1
# =============================================================================

from datetime import datetime, timedelta


class MinBalanceWarn(Exception):
    """A class return warning if the balance is less than minimum"""
    pass


class BankAccount:
    """A class that keeps clients' name and balance"""
    min_balance = 100

    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.__open(initial_deposit)  # check the opening balance
        self.history = []
        self.__tr_history('Open Account',
                          initial_deposit)  # record opening deposit in history

    def __open(self, initial_dpst):
        """Check the initial balance to be more than minimum balance"""
        if self.min_balance > initial_dpst:
            print(f"\n{self.name} Account opened under minimum balance!,"
                  f"\n(minimum balance is {self.min_balance}$)")

    def deposit(self, deposit_amount):
        """Deposit money to bank account"""
        self.balance += deposit_amount
        print(f"\n{self.name} Deposit {deposit_amount}$"
              f"\n[New balance: {self.balance}$]")
        self.__tr_history('Deposit', deposit_amount)

    def withdraw(self, withdraw_amount):
        """Withdraw money from bank account"""
        try:
            self.__warn(withdraw_amount)
            self.balance -= withdraw_amount
            print(f"\n{self.name} Withdraw {withdraw_amount}$ is ALLOWED"
                  f"\n[New balance: {self.balance}$]")
            self.__tr_history('Withdraw', withdraw_amount)
        except MinBalanceWarn:
            print(f"\nWithdraw {withdraw_amount}$ is DENIED"
                  f"\n[{self.name} balance: {self.balance}$]"
                  f"\n(Minimum balance: {self.min_balance}$)")

    def transfer(self, des_account, transfer_amount):
        """Transfer money to another bank account"""
        try:
            self.__warn(transfer_amount)
            self.balance -= transfer_amount
            des_account.balance += transfer_amount
            print(f"\n{self.name} transfered {transfer_amount}$"
                  f" to {des_account.name}"
                  f"\n[{self.name} New balance: {self.balance}$]"
                  f"\n[{des_account.name} New balance:"
                  f" {des_account.balance}$]")
            self.__tr_history(f'Transfer to {des_account.name}',
                              transfer_amount)
            des_account.__tr_history(f'Transfer from {self.name}',
                                     transfer_amount)
        except MinBalanceWarn:
            print(f"\nTransfer Denied, not enough balance"
                  f"\n[{self.name} balance: {self.balance}$]"
                  f"\n[{des_account.name} balance: {des_account.balance}$]")

    def __warn(self, withdraw_amnt):
        """Check whether the balance is lower than min or not"""
        if self.balance - withdraw_amnt >= self.min_balance:
            return True
        raise MinBalanceWarn

    def __str__(self):
        return f"\n{self.name} account balance is: {self.balance}$"

    def __repr__(self):
        return f"\n{self.name} account balance is: {self.balance}$"

    def __tr_history(self, transaction_type, amount):
        '''Record bank acount transaction history'''
        transaction_time = datetime.now().strftime("%Y-%b-%d %H:%M")
        self.history.append({'time': transaction_time,
                             'type': transaction_type,
                             'amount': amount,
                             'balance': self.balance})

    def tr_time(self, entry_time):
        '''Report transactions close to entry time
        Enter your time like--> "2021-Sep-19 14:21"'''
        lst = []
        for record in self.history:
            history_time = datetime.strptime(record['time'], '%Y-%b-%d %H:%M')
            entred_time = datetime.strptime(entry_time, '%Y-%b-%d %H:%M')
            if entred_time - timedelta(minutes=2) < history_time\
               < entred_time + timedelta(minutes=2):
                lst.append(record)  # append all 2 min transacions in a list
        if lst == []:
            print("\nNo close record to entred time")
        else:
            print('\n', *lst, sep='\n\n')
