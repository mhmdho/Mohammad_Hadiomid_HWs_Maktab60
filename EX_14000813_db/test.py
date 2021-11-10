# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4  09:34:16 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Exam - Model test    (1400-08-13 - Thursday)
# =============================================================================

import datetime
from mongo_service import Database
import unittest
import book


class TestBook(unittest.TestCase):
    ''' Test to work correctly '''

    def setUp(self):
        ''' Define db '''
        self.db = Database()

    def test_create_book(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        b = book.create_book(book1)
        self.assertIsNotNone(b)
        self.db.book_collection.delete_one({"title": "test"})

    def test_create_duplicate_book(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        b = book.create_book(book1)
        b2 = book.create_book(book1)
        self.assertIsNotNone(b)
        self.assertIsNone(b2)
        self.db.book_collection.delete_one({"title": "test"})

    def test_create_book_fields(self):
        book1 = {
                "title": "test",

                "published_date": datetime.datetime(2009, 10, 12)}
        b = book.create_book(book1)
        self.assertIsNone(b)
        self.db.book_collection.delete_one({"title": "test"})

    def test_create_user(self):
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        u = book.create_user(user1)
        self.assertIsNotNone(u)
        self.db.user_collection.delete_one({"name": "nametest"})

    def test_create_duplicate_user(self):
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        u = book.create_user(user1)
        u2 = book.create_user(user1)
        self.assertIsNotNone(u)
        self.assertIsNone(u2)
        self.db.user_collection.delete_one({"name": "nametest"})

    def test_create_user_fields(self):
        user1 = {
                "name": "nametest",

                }
        u = book.create_user(user1)
        self.assertIsNone(u)
        self.db.user_collection.delete_one({"name": "nametest"})

    def test_create_like_book(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        b = book.create_book(book1)
        u = book.create_user(user1)
        tst = book.create_like_book(b, u)
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_delete_like_book(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        b = book.create_book(book1)
        u = book.create_user(user1)
        tst = book.delete_like_book(b, u)
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_create_comment_book(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        b = book.create_book(book1)
        u = book.create_user(user1)
        tst = book.create_comment_book(b, u, 'Great test book')
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_get_all_books(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        book.create_book(book1)
        book.create_user(user1)
        tst = book.get_all_books()
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_get_all_books_bytag(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        book.create_book(book1)
        book.create_user(user1)
        tst = book.get_all_books('dbtest')
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_get_all_book_comments(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        b = book.create_book(book1)
        u = book.create_user(user1)
        book.create_comment_book(b, u, 'Great test book')
        tst = book.get_all_book_comments(b, 3, 0)
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_get_all_user_liked_and_taked_comment_book(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        user1 = {
                "name": "nametest",
                "natinalcode": "0083032184",
                "pass": "1234"}
        b = book.create_book(book1)
        u = book.create_user(user1)
        book.create_like_book(b, u)
        tst = book.get_all_user_liked_and_taked_comment_book(u)
        self.assertIsNotNone(tst)
        self.db.user_collection.delete_one({"name": "nametest"})
        self.db.book_collection.delete_one({"title": "test"})

    def test_get_books_tag_count(self):
        book1 = {
                "title": "test",
                "author": "Miketest",
                "publication": "Nashrenotest",
                "tag": ["mongotest", "dbtest"],
                "published_date": datetime.datetime(2009, 10, 12)}
        book.create_book(book1)
        tst = book.get_books_tag_count()
        self.assertIsNotNone(tst)
        self.db.book_collection.delete_one({"title": "test"})


if __name__ == '__main__':
    unittest.main(verbosity=1)
