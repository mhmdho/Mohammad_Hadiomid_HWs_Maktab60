# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4  09:34:16 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Exam - Model test_main    (1400-08-13 - Thursday)
# =============================================================================

import datetime
import book


book1 = {
        "title": "Pymongo",
        "author": "Mike",
        "publication": "Nashreno",
        "tag": ["mongo", "db"],
        "published_date": datetime.datetime(2009, 10, 12)}
book1_id = '6186c37b19b931d90b988212'

book2 = {
        "title": "Pycharm",
        "author": "Tom",
        "publication": "Nashrandish",
        "tag": ["pycharm", "py"],
        "published_date": datetime.datetime(2011, 7, 10)}
book2_id = '6186c38619b931d90b988214'

book3 = {
        "title": "Django",
        "author": "Jack",
        "publication": "sharif",
        "tag": ["jango", "Django"],
        "published_date": datetime.datetime(2019, 9, 26)}
book3_id = '6186c37d19b931d90b988213'

user1 = {
        "name": "Mohammad",
        "natinalcode": "0083432184",
        "pass": "123"}
user1_id = '6186c37d19b931d90b988213'

user2 = {
        "name": "Ahmad",
        "natinalcode": "0083432184",
        "pass": "000"}
user2_id = '6186c77719b931d90b98821a'
user4_id = '6186c77719b931d90b988915'
book4_id = '6186c38019b931d90b988214'


book.create_book(book3)
book.create_user(user2)
book.create_like_book(book1_id, user1_id)
book.delete_like_book(book1_id, user1_id)
book.create_comment_book(book1_id, user1_id, 'good445646 book2')
book.get_all_books()
book.get_all_book_comments(book1_id, 3, 2)
book.get_all_user_liked_book(user2_id)
book.get_all_user_liked_and_taked_comment_book(user1_id)
book.get_books_tag_count()
