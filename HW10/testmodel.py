# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 21:34:23 2021

@author: Lenovo
"""


import unittest
import redis
from model import Event, ReadEvent, User, Admin, Student, Employee, redis_event


class TestEventMethods(unittest.TestCase):
    ''' Test Event class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_test = redis.Redis(decode_responses=True)
        self.event = Event()

    def test_save(self):
        ''' Test save '''
        self.event.create_event('2021/12/24 17:00', "html", 'Tehran', 30, 120)
        self.event.save()
        event_from_redis = self.redis_test.hmget(
                f'event:{self.event.event_id}:info', "Date")
        self.assertIsNotNone(event_from_redis)


class TestReadEventMethods(unittest.TestCase):
    ''' Test ReadEvent class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_test = redis.Redis(decode_responses=True)
        self.event = Event()
        self.read_event = ReadEvent()

    def test_show_all_events(self):
        ''' Test show_all_events '''
        self.event.create_event('2021/12/24 17:00', "html", 'Tehran', 30, 120)
        self.event.save()
        tst = self.read_event.show_all_events()
        self.assertIsNotNone(tst)

    def test_select_event(self):
        ''' Test select_event '''
        self.event.create_event('2021/12/24 17:00', "html", 'Tehran', 30, 120)
        self.event.save()
        self.read_event.discount_return("11stu", "teacher")
        tst = self.read_event.select_event(1, 5)
        self.assertIsNotNone(tst)

    def test_discoutn_return(self):
        ''' Test discoutn_return '''
        self.event.create_event('2021/12/24 17:00', "html", 'Tehran', 30, 120)
        self.event.save()
        tst = self.read_event.discount_return("22stu", "father")
        self.assertFalse(tst)

    def test_buy_ticket(self):
        ''' Test but_ticket '''
        self.event.create_event('2021/12/24 17:00', "html", 'Tehran', 30, 120)
        self.event.save()
        self.read_event.discount_return("11stu", "teacher")
        self.read_event.select_event(1, 5)
        self.read_event.buy_ticket(500)
        ts = self.redis_test.hget(f"event:{self.event.event_id}:info",
                                  "Ticket Remained")
        self.assertEqual(int(ts), 30)


class TestUser(unittest.TestCase):
    ''' Test User class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_test = redis.Redis(decode_responses=True)
        self.user = User()

    def test_sign_up(self):
        ''' Test sign_up '''
        self.user.sign_up("ali22", "12345")
        ts = self.redis_test.hget(f"login:ali22:info",
                                  "Username")
        self.assertEqual(ts, "ali22")

    def test_sign_in(self):
        ''' Test sign_in '''
        self.user.sign_in("ali22", "12345")
        ts1 = self.redis_test.hget(f"login:ali22:info",
                                   "Username")
        ts2 = self.redis_test.hget(f"login:ali22:info",
                                   "Userpass")
        self.assertEqual(ts1, "ali22")
        self.assertEqual(ts2, "12345")


class TestAdmin(unittest.TestCase):
    ''' Test User class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_test = redis.Redis(decode_responses=True)
        self.admin = Admin()

    def test_sign_up(self):
        ''' Test sign_up '''
        self.admin.sign_up("ali22", "12345")
        ts = self.redis_test.hget(f"login:ali22:info",
                                  "Username")
        self.assertEqual(ts, "ali22")

    def test_sign_in(self):
        ''' Test sign_in '''
        self.admin.sign_in("ali22", "12345")
        ts1 = self.redis_test.hget(f"login:ali22:info",
                                   "Username")
        ts2 = self.redis_test.hget(f"login:ali22:info",
                                   "Userpass")
        self.assertEqual(ts1, "ali22")
        self.assertEqual(ts2, "12345")


class TestStudent(unittest.TestCase):
    ''' Test User class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_test = redis.Redis(decode_responses=True)
        self.student = Student()

    def test_sign_up(self):
        ''' Test sign_up '''
        self.student.sign_up("ali22", "12345")
        ts = self.redis_test.hget(f"login:ali22:info",
                                  "Username")
        self.assertEqual(ts, "ali22")

    def test_sign_in(self):
        ''' Test sign_in '''
        self.student.sign_in("ali22", "12345")
        ts1 = self.redis_test.hget(f"login:ali22:info",
                                   "Username")
        ts2 = self.redis_test.hget(f"login:ali22:info",
                                   "Userpass")
        self.assertEqual(ts1, "ali22")
        self.assertEqual(ts2, "12345")


class TestEmployee(unittest.TestCase):
    ''' Test User class to work correctly '''

    def setUp(self):
        ''' Define redis '''
        self.redis_test = redis.Redis(decode_responses=True)
        self.employee = Employee()

    def test_sign_up(self):
        ''' Test sign_up '''
        self.employee.sign_up("ali22", "12345")
        ts = self.redis_test.hget(f"login:ali22:info",
                                  "Username")
        self.assertEqual(ts, "ali22")

    def test_sign_in(self):
        ''' Test sign_in '''
        self.employee.sign_in("ali22", "12345")
        ts1 = self.redis_test.hget(f"login:ali22:info",
                                   "Username")
        ts2 = self.redis_test.hget(f"login:ali22:info",
                                   "Userpass")
        self.assertEqual(ts1, "ali22")
        self.assertEqual(ts2, "12345")


if __name__ == '__main__':
    unittest.main(verbosity=1)
