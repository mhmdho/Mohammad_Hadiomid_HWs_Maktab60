# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:14:48 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Homework 9 - Question 1
# =============================================================================

from datetime import datetime


class CheckCredit(Exception):
    '''Raise when credit is not enough'''
    pass


class CheckDate(Exception):
    '''Raise when date expired'''
    pass


class OneWayCard:
    '''
        Subway cards that are usable once
    '''
    id_card = 1000

    def __init__(self):
        self.credit = True
        self.idcard = self.id_generator()

    @classmethod
    def id_generator(cls):
        '''ID generator of cards'''
        cls.id_card += 1
        return cls.id_card

    def use_card(self):
        '''change credit by using card'''
        if self.credit:
            self.credit = False
        else:
            raise CheckCredit(f"No credit, zero trip remained")


class CreditCard(OneWayCard):
    '''
        Subway cards that have credit
    '''
    id_card = 2000

    def __init__(self):
        super().__init__()
        self.credit = 0

    def charge_card(self, charge_amount):
        '''charge card based on the amount of entry'''
        self.credit += charge_amount

    def use_card(self, trip_fare):
        '''decrease credit by using card'''
        if trip_fare <= self.credit:
            self.credit -= trip_fare
        else:
            raise CheckCredit("Not enough credit")


class ExpiringCreditCard(CreditCard):
    '''
        Subway cards that have both credit and expiring date
    '''
    id_card = 3000

    def __init__(self):
        super().__init__()
        self.expiring_date = datetime.now()

    def charge_card(self, charge_amount, expiring_date):
        '''charge card based on the amount of entry and date'''
        super().charge_card(charge_amount)
        # self.expiring_date += timedelta(days=30)
        self.expiring_date = datetime.strptime(expiring_date, '%Y/%m/%d')

    def use_card(self, trip_fare):
        '''decrease credit by using card if the card not expired'''
        if self.credit < trip_fare:
            raise CheckCredit("No credit")
        elif self.expiring_date < datetime.now():
            self.credit = 0
            raise CheckDate("Card expired")
        else:
            self.credit -= trip_fare
