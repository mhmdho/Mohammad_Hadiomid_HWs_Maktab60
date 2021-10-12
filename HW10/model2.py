# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:01:28 2021

@author: Lenovo
"""

from datetime import datetime
import redis

redis_event = redis.Redis(decode_responses=True)
redis_event.set('event_id', 0)
redis_event.set('user_id', 1000)


class LoginError(Exception):
    pass


class Log:
    ''' write all log in log.text file'''

    @staticmethod
    def get_log_info(description):
        with open("log.txt", 'a') as file:
            print(datetime.now(), description, file=file)


class UserLogin():
    '''define users'''
    def __init__(self):
        self.login = False

    @staticmethod
    def id_generator():
        ''' generate user ID'''
        redis_event.incr('user_id')
        return redis_event.get('user_id')

    def sign_up(self, username, userpass):
        '''register user'''
        usern = redis_event.hget(f"login:{username}:info", "Username")
        if usern:
            result = "This username exist"
            Log.get_log_info(result)
        else:
            redis_event.hmset(f"login:{username}:info", mapping={
                "ID": self.id_generator(),
                "Username": username,
                "Userpass": userpass,
                "Usertype": self.usertype})
            # result0 = redis_event.hgetall(("login:{username}:info"))
            result = f"User created"
            Log.get_log_info(result)
        return result

    def sign_in(self, username, userpass):
        '''login users'''
        usern = redis_event.hget(f"login:{username}:info", "Username")
        userp = redis_event.hget(f"login:{username}:info", "Userpass")
        usert = redis_event.hget(f"login:{username}:info", "Usertype")
        if usern == username and userp == userpass and usert == self.usertype:
            self.login = True
            Log.get_log_info(f'{usern} logged in')
        else:
            self.login = False
            Log.get_log_info(f'Incorrect username or password')
            raise LoginError
        return self.login


class Event(UserLogin):
    '''create event by admin'''

    def create_event(self, date, event_name, location, capacity, ticket_price):
        '''create event with all required components'''
        if self.login:
            # self.date = datetime.strptime(date, '%Y/%m/%d %H:%M')
            self.date = date
            self.event_name = event_name
            self.location = location
            self.capacity = capacity
            self.remained_capacity = capacity
            self.ticket_price = ticket_price
            self.event_id = self.eid_generator()

    @staticmethod
    def eid_generator():
        ''' generate event ID'''
        redis_event.incr('event_id')
        return redis_event.get('event_id')

    def save(self):
        ''' save event'''
        if self.login:
            redis_event.hmset(name=f"event:{self.event_id}:info", mapping={
                "ID": self.event_id,
                "Date": self.date,
                "Event Name": self.event_name,
                "Location": self.location,
                "Capacity": self.capacity,
                "Ticket Remained": self.remained_capacity,
                "Ticket Price": self.ticket_price})
            Log.get_log_info(f"New Event, {self.event_name} created.")
            return redis_event.hgetall(f"event:{self.event_id}:info")

    def discount_define(self, code, usertype, discount):
        ''' define discount for each event'''
        if self.login:
            redis_event.hmset(name=f"discount:{code}:info", mapping={
                "Usertype": usertype,
                "Discount": discount})

    def event_tickets_condition(self, event_id):
        '''show remained and sold tickets'''
        if self.login:
            capacity = redis_event.hget(f"event:{event_id}:info",
                                        "Capacity")
            available_tickets = redis_event.hget(f"event:{event_id}:info",
                                                 "Ticket Remained")
            sold_tickets = int(capacity) - int(available_tickets)
            ans = f"Sold Tickets:{sold_tickets} - Remained:{available_tickets}"
            return ans


class ReadEvent(UserLogin):
    ''' show all event for users'''

    @staticmethod
    def show_all_events(self):
        '''return all events'''
        if self.login:
            lst = []
            events = redis_event.keys(pattern="event:*:info")
            for event in events:
                lst.append(redis_event.hgetall(event))
            return lst

    def select_event(self, event_id, tickets, code=None):
        ''' choose an event by user'''
        if self.login:
            self.event_id = event_id
            self.tickets = tickets
            self.ticket_price = redis_event.hget(f"event:{event_id}:info",
                                                 "Ticket Price")
            ev_name = redis_event.hget(f"event:{event_id}:info", "Event Name")
            available_tickets = redis_event.hget(f"event:{event_id}:info",
                                                 "Ticket Remained")
            if self.tickets > int(available_tickets):
                result = f"No enough capacity"
                Log.get_log_info(f'No enough capacity for {ev_name}')
            else:
                self.total_price = self.tickets * float(self.ticket_price) *\
                    (1-self.discount_return(code, self.usertype))
                result = f"The total price for {self.tickets} tickets with {self.discount_return(code, self.usertype)} discount is {self.total_price}$"
            return result

    def discount_return(self, code, usertype):
        ''' return discount base on code'''
        if self.login:
            self.usertype = usertype
            if redis_event.hget(
                    f"discount:{code}:info", "Usertype") == self.usertype:
                dis = float(redis_event.hget(
                        f"discount:{code}:info", "Discount"))
            else:
                Log.get_log_info('Incorrect discount code')
                dis = 0
            return dis

    def buy_ticket(self, price):
        ''' buy a ticket by user'''
        if self.login:
            self.event_name = redis_event.hget(f"event:{self.event_id}:info",
                                               "Event Name")
            self.remained_capacity = int(redis_event.hget(
                f"event:{self.event_id}:info", "Ticket Remained"))
            print(self.total_price)
            if price == self.total_price:
                redis_event.hmset(name=f"sold:{self.event_id}:info", mapping={
                    "ID": redis_event.hget(
                            f"event:{self.event_id}:info", "ID"),
                    "Date": redis_event.hget(
                            f"event:{self.event_id}:info", "Date"),
                    "Event Name": redis_event.hget(
                            f"event:{self.event_id}:info", "Event Name"),
                    "Location": redis_event.hget(f"event:{self.event_id}:info",
                                                 "Location"),
                    "Sold Tickets": self.tickets,
                    "Total Price": self.total_price})
                Log.get_log_info(
                    f"{self.tickets} Tickets of event {self.event_name} Sold.")
                self.remained_capacity -= self.tickets
                redis_event.hmset(
                    name=f"event:{self.event_id}:info", mapping={
                            "Ticket Remained": self.remained_capacity})

                print("Your purchase was successful",
                      redis_event.hget(f"event:{self.event_id}:info", "ID"),
                      redis_event.hget(f"event:{self.event_id}:info", "Date"),
                      redis_event.hget(f"event:{self.event_id}:info",
                                       "Event Name"),
                      redis_event.hget(
                              f"event:{self.event_id}:info", "Location"),
                      self.tickets,
                      self.total_price,
                      sep="\n")
                print(redis_event.hgetall(f"event:{self.event_id}:info"))
                print(redis_event.hgetall(f"sold:{self.event_id}:info"))

            else:
                print("Unsuccessful transaction, Entered incorrect price")
                Log.get_log_info(f'Unsuccessful transaction, incorrect price')


class User(ReadEvent):
    '''Admin user'''
    def __init__(self):
        self.usertype = "user"


class Admin(User, Event):
    '''Admin user'''
    def __init__(self):
        self.usertype = "admin"


class Student(User):
    '''Student user'''
    def __init__(self):
        self.usertype = "student"


class Employee(User):
    '''Employee user'''
    def __init__(self):
        self.usertype = "employee"
