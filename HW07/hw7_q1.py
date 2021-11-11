# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:12:36 2021

@author: Lenovo
"""
# =============================================================================
# HOMEWORK 7 - QUESTION 1
# =============================================================================


class BankAccount:
    """A class that keeps clients' name and balance"""
    min_balance = 100

    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.__open(initial_deposit)  # check the opening balance

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

    def withdraw(self, withdraw_amount):
        """Withdraw money from bank account"""
        if self.__warn(withdraw_amount):
            self.balance -= withdraw_amount
            print(f"\n{self.name} Withdraw {withdraw_amount}$ is ALLOWED"
                  f"\n[New balance: {self.balance}$]")
        else:
            print(f"\nWithdraw {withdraw_amount}$ is DENIED"
                  f"\n[{self.name} balance: {self.balance}$]"
                  f"\n(Minimum balance: {self.min_balance}$)")

    def transfer(self, des_account, transfer_amount):
        """Transfer money to another bank account"""
        if self.__warn(transfer_amount):
            print(f"\n\t---(transfer {self.name} to {des_account.name})---")
            self.withdraw(transfer_amount)
            des_account.deposit(transfer_amount)
            print(f"\n\t--------(transfer done)--------")
        else:
            print(f"\nTransfer Denied, not enough balance"
                  f"\n[{self.name} balance: {self.balance}$]"
                  f"\n[{des_account.name} balance: {des_account.balance}$]")

    def __warn(self, withdraw_amnt):
        """Check whether the balance is lower than min or not"""
        if self.balance - withdraw_amnt >= self.min_balance:
            return True
        return False

    def __str__(self):
        return f"\n{self.name} account balance is: {self.balance}$"

    def __repr__(self):
        return f"\n{self.name} account balance is: {self.balance}$"
