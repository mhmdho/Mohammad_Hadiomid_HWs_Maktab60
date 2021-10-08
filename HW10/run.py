# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:10:45 2021

@author: Lenovo
"""

from model import User, Admin


print("welcome to Events portal")
print("---admin login---")
Ali = Admin()
user = input("Enter username: ")
pss = input("Enter password: ")
print(Ali.sign_up(user, pss))
print(Ali.sign_in(user, pss))

if Ali.sign_in(user, pss):
    print("welcome")
    date = input("Enter event date: ")
    name = input("Enter event name: ")
    place = input("Enter event place: ")
    capacity = int(input("Enter event capacity: "))
    price = input("Enter event price: ")
    Ali.create_event(date, name, place, capacity, price)
    Ali.save()
    Ali.event_id
    print(Ali.event_tickets_condition(Ali.event_id))

    admin_code = input("Enter Admin code: ")
    admin_discount = input("Enter admin discount: ")
    Ali.discount_define(admin_code, "admin", admin_discount)
    student_code = input("Enter student code: ")
    student_discount = input("Enter student discount: ")
    Ali.discount_define(student_code, "student", student_discount)
    employee_code = input("Enter employee code: ")
    employee_discount = input("Enter employee discount: ")
    Ali.discount_define(employee_code, "employee", employee_discount)
    user_code = input("Enter user code: ")
    user_discount = input("Enter user discount: ")
    Ali.discount_define(user_code, "user", user_discount)


print("---user login---")
Hadi = User()
user2 = input("Enter username: ")
pss2 = input("Enter password: ")
print(Hadi.sign_up(user2, pss2))
print(Hadi.sign_in(user2, pss2))

if Hadi.sign_in(user2, pss2):
    print(Hadi.show_all_events())

    event_id = input("Enter event ID: ")
    tickets = int(input("Enter number of tickets: "))
    code = input("Enter discount code: ")
    print(Hadi.select_event(event_id, tickets, code))

    purchase = input("Enter price to complete your purchase: ")
    print(Hadi.buy_ticket(purchase))
