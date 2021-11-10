# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4  09:34:16 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Exam - mongo_service    (1400-08-13 - Thursday)
# =============================================================================

import time
import json
import datetime

from pymongo import MongoClient
from pymongo import ASCENDING
from settings import MONGO_HOST, MONGO_USER, MONGO_PASS


class Database:

    def initialize(self):
        try:
            mongo_client = MongoClient(MONGO_HOST, 27017)

            self.database = mongo_client.book_db

            self.book_collection = self.database.book_collection
            self.user_collection = self.database.user_collection
            # todo define collections here

        except Exception:
            print("Mongo Initialization Failed. Passing")
            pass

    def __init__(self):
        self.initialize()
