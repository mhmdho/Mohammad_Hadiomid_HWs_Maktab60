# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 01:14:29 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Homework 9 - Test of Q1
# =============================================================================

import unittest
from datetime import datetime
import hw9
from hw9 import CheckCredit, CheckDate


class TestOneWayCard(unittest.TestCase):
    '''
        Test subway one way cards to work correctly
    '''

    def setUp(self):
        self.one_way_card_1 = hw9.OneWayCard()
        self.one_way_card_2 = hw9.OneWayCard()

    def test1_id_oneway(self):
        '''Test one way cards ID'''
        self.assertEqual(self.one_way_card_1.idcard, 1001)
        self.assertEqual(self.one_way_card_2.idcard, 1002)

    def test_use_card(self):
        '''Test one way cards using'''
        self.assertEqual(self.one_way_card_1.credit, True)
        self.one_way_card_1.use_card()
        self.assertEqual(self.one_way_card_1.credit, False)

    def test_one_way_exception(self):
        '''Test one way cards exception to raise correctly'''
        self.one_way_card_1.use_card()
        with self.assertRaises(CheckCredit):
            self.one_way_card_1.use_card()


class TestCreditCard(unittest.TestCase):
    '''
        Test subway credit cards to work correctly
    '''

    def setUp(self):
        self.credit_card_1 = hw9.CreditCard()
        self.credit_card_2 = hw9.CreditCard()

    def test1_id_credit(self):
        '''Test credit cards ID'''
        self.assertEqual(self.credit_card_1.idcard, 2001)
        self.assertEqual(self.credit_card_2.idcard, 2002)

    def test_charge_card(self):
        '''Test credit cards to charge correctly'''
        self.assertEqual(self.credit_card_1.credit, 0)
        self.credit_card_1.charge_card(1000)
        self.assertEqual(self.credit_card_1.credit, 1000)

    def test_use_card(self):
        '''Test credit cards when using'''
        self.assertEqual(self.credit_card_1.credit, 0)
        self.credit_card_1.charge_card(1000)
        self.credit_card_1.use_card(300)
        self.assertEqual(self.credit_card_1.credit, 700)
        self.assertGreater(self.credit_card_1.credit, 699)
        self.assertLess(self.credit_card_1.credit, 701)

    def test_credit_exception(self):
        '''Test credit cards exception to raise correctly'''
        self.credit_card_1.charge_card(500)
        with self.assertRaises(CheckCredit):
            self.credit_card_1.use_card(1000)
        self.assertEqual(self.credit_card_1.credit, 500)


class TestExpiringCreditCard(unittest.TestCase):
    '''
        Test subway expiring credit cards to work correctly
    '''

    def setUp(self):
        self.expiring_credit_card_1 = hw9.ExpiringCreditCard()
        self.expiring_credit_card_2 = hw9.ExpiringCreditCard()

    def test1_id_expiring(self):
        '''Test expiring cards ID'''
        self.assertEqual(self.expiring_credit_card_1.idcard, 3001)
        self.assertEqual(self.expiring_credit_card_2.idcard, 3002)

    def test_charge_card(self):
        '''Test expiring cards charge to work correctly'''
        self.assertEqual(self.expiring_credit_card_1.credit, 0)
        self.expiring_credit_card_1.charge_card(1000, '2022/09/01')
        self.assertEqual(self.expiring_credit_card_1.credit, 1000)

    def test_use_card(self):
        '''Test expiring cards when using'''
        self.assertEqual(self.expiring_credit_card_1.credit, 0)
        self.expiring_credit_card_1.charge_card(1000, '2022/09/01')
        self.expiring_credit_card_1.use_card(300)
        self.assertEqual(self.expiring_credit_card_1.credit, 700)
        self.assertGreaterEqual(self.expiring_credit_card_1.expiring_date,
                                datetime.now())

    def test_credit_exception(self):
        '''Test expiring cards credit exception to work correctly'''
        self.expiring_credit_card_1.charge_card(500, '2022/09/01')
        with self.assertRaises(CheckCredit):
            self.expiring_credit_card_1.use_card(1000)
        self.assertEqual(self.expiring_credit_card_1.credit, 500)

    def test_date_exception(self):
        '''Test expiring cards Date exception to work correctly'''
        self.expiring_credit_card_1.charge_card(500, '2020/03/01')
        with self.assertRaises(CheckDate):
            self.expiring_credit_card_1.use_card(200)

    def test_credit_zero(self):
        ''' Test credit to become zero if card expired '''

        self.expiring_credit_card_1.charge_card(500, '2020/03/01')
        with self.assertRaises(CheckDate):
            self.expiring_credit_card_1.use_card(340)
        self.assertEqual(self.expiring_credit_card_1.credit, 0)
        self.assertLess(self.expiring_credit_card_1.expiring_date,
                        datetime.now())


if __name__ == '__main__':
    unittest.main(verbosity=1)
