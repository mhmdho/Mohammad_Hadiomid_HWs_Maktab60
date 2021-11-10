# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:27:39 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 16 - db of Model    (1400-08-11 - Tuessday)
# =============================================================================

import psycopg2


conct = psycopg2.connect(database="bank", user="postgres",
                         password="2332213", host="127.0.0.1", port="5432")
cursor = conct.cursor()


# create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (user_id serial PRIMARY KEY NOT NULL,
                       name VARCHAR(50) NOT NULL
                       );''')
conct.commit()


# create history table
cursor.execute('''CREATE TABLE IF NOT EXISTS history
                      (history_id serial PRIMARY KEY NOT NULL,
                       user_id INT NOT NULL,
                       history_time TIMESTAMP NOT NULL,
                       history_type VARCHAR(50) NOT NULL,
                       amount INT NOT NULL,
                       balance INT NOT NULL,
                       FOREIGN KEY(user_id)
                              REFERENCES users(user_id));''')
conct.commit()

# cursor.execute('''DROP TABLE users;''')
# conct.commit()
