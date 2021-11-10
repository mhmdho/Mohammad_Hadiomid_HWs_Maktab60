# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4  09:34:16 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Exam - Model    (1400-08-13 - Thursday)
# =============================================================================

import pymongo
from mongo_service import Database
from bson.objectid import ObjectId

db = Database()


def create_book(book_data):
    try:
        book_data['title']
        book_data['author']
        book_data['publication']
        book_data['tag']
        book_data['published_date']
        book_entry = db.book_collection.insert_one(book_data)
        return book_entry.inserted_id
    except KeyError:
        print("Your book_data must contains:\
              (title, author, publication, tag, published_date)", book_data)
    except pymongo.errors.DuplicateKeyError:
        print("Inserting duplicate Data:", book_data)
    except Exception:
        print("Inserting Error Log Failed. Data:", book_data)


def create_user(user_data):
    try:
        user_data['name']
        user_data['natinalcode']
        user_data['pass']
        user_entry = db.user_collection.insert_one(user_data)
        # db.user_collection.createIndex({'user_id':user_data['user_id']},
        #                                {'unique':True})
        # db.user_collection.create_index([('user_id', pymongo.ASCENDING)],
        #                                unique=True)
        return user_entry.inserted_id
    except KeyError:
        print("Your user_data must contains:\
              (name, pass, nationalcode)", user_data)
    except pymongo.errors.DuplicateKeyError:
        print("Inserting duplicate Data:", user_data)
    except Exception:
        print("Inserting Error Log Failed. Data:", user_data)


def create_like_book(book_id, user_id):  # uniqueness
    if not db.user_collection.find_one({'_id': ObjectId(user_id)}):
        result = f"Incorrect user_id"
    elif db.book_collection.find_one({"like": ObjectId(user_id)}):
        result = f"You have already liked this book"
    elif not db.book_collection.find_one({'_id': ObjectId(book_id)}):
        result = f"This book is not exist"
    else:
        try:
            db.book_collection.update_one({'_id': ObjectId(book_id)},
                                          {'$push':
                                              {'like': ObjectId(user_id)}})
            result = db.book_collection.find_one({'_id': ObjectId(book_id)})
        except Exception:
            print("Inserting data error")
    return result


def delete_like_book(book_id, user_id):
    if not db.user_collection.find_one({'_id': ObjectId(user_id)}):
        result = f"Incorrect user_id"
    elif not db.book_collection.find_one({'_id': ObjectId(book_id)}):
        result = f"This book is not exist"
    elif not db.book_collection.find_one({"like": ObjectId(user_id)}):
        result = f"You have not already liked this book"
    else:
        try:
            db.book_collection.update_one({'_id': ObjectId(book_id)},
                                          {'$pull':
                                              {'like': ObjectId(user_id)}})
            result = db.book_collection.find_one({'_id': ObjectId(book_id)})
        except Exception:
            print("Inserting data error")
    return result


def create_comment_book(book_id, user_id, comment):
    if not db.user_collection.find_one({'_id': ObjectId(user_id)}):
        result = f"Incorrect user_id"
    elif not db.book_collection.find_one({'_id': ObjectId(book_id)}):
        result = f"This book is not exist"
    else:
        try:
            db.book_collection.update_one(
                    {'_id': ObjectId(book_id)},
                    {'$push': {'comment': {'_id': ObjectId(user_id),
                                           'comment': comment}}})
            result = db.book_collection.find_one({'_id': ObjectId(book_id)})
        except Exception:
            print("Inserting data error")
    return result


def get_all_books(tag=None):  # order by like count -include only comment count
    # if tag is not none filter by tag
    pipline_tag = [
        {
            "$match": {'tag': tag}
        },
        {
            "$project": {"title": "$title",
                         "comment_count":
                             {"$size": {"$ifNull": ["$comment", []]}},
                         "like_count":
                             {"$size": {"$ifNull": ["$comment", []]}}}
        },
        {
            "$sort": {"like_count": -1}
        }]
    pipline_none = [
        {
            "$match": {'tag': {'$regex': '/*'}}
        },
        {
            "$project": {"title": "$title",
                         "comment_count":
                             {"$size": {"$ifNull": ["$comment", []]}},
                         "like_count":
                             {"$size": {"$ifNull": ["$comment", []]}}}
        },
        {
            "$sort": {"like_count": -1}
        }]
    if tag is None:
        result = db.book_collection.aggregate(pipline_none)
    else:
        result = db.book_collection.aggregate(pipline_tag)
    return list(result)
    # return sorted(list(result), key=lambda d: d['like_count'])


def get_all_book_comments(book_id, count, index):  # order by latest
    if not db.book_collection.find_one({'_id': ObjectId(book_id)}):
        result = f"This book is not exist"
    else:
        try:
            comment = db.book_collection.find_one(
                    {'_id': ObjectId(book_id)})['comment']
            result = comment[::-1][index: index+count]
        # not negative
        except KeyError:
            print("There is no comment")
        except Exception:
            print("Inserting data error")
    return result


def get_all_user_liked_book(user_id):
    if not db.user_collection.find_one({'_id': ObjectId(user_id)}):
        result = f"Incorrect user_id"
    else:
        try:
            result = db.book_collection.find({"like": ObjectId(user_id)})
            result = list(result)
        except Exception:
            print("Inserting data error")
    return result


def get_all_user_liked_and_taked_comment_book(user_id):
    if not db.user_collection.find_one({'_id': ObjectId(user_id)}):
        result = f"Incorrect user_id"
    else:
        try:
            result = db.book_collection.find(
                {'$and': [
                    {"like": ObjectId(user_id)},
                    {"comment": {"$elemMatch": {'_id': ObjectId(user_id)}}}
                          ]})
            result = list(result)
        except Exception:
            print("Inserting data error")
    return result


def get_books_tag_count():
    try:
        pipline = [
            {
                "$project": {"Title": "$title", "tag_count": {"$size": "$tag"}}
            }]
        result = db.book_collection.aggregate(pipline)
        return list(result)
    except Exception:
        print("Inserting data error")
