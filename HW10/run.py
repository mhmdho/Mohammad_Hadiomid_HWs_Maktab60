# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:10:45 2021

@author: Lenovo
"""

from model import User, Admin


print("welcome to Events portal")

TESTUSER = Admin()
user = input("Enter username: ")
pss = input("Enter password: ")

if TESTUSER.sign_in(user, pss) is False:
    TESTUSER = User()
    if TESTUSER.sign_in(user, pss) is False:
        print("please sign-up!")
        input("press enter to redirect to sign-up")
        user = input("Enter username: ")
        pss = input("Enter password: ")
        print(TESTUSER.sign_up(user, pss))

print(TESTUSER.sign_in(user, pss))
if TESTUSER.sign_in(user, pss):
    if TESTUSER.usertype == "admin":
        print("---admin login--- | ---welcome---")
        date = input("Enter event date: ")
        name = input("Enter event name: ")
        place = input("Enter event place: ")
        capacity = int(input("Enter event capacity: "))
        price = input("Enter event price: ")
        TESTUSER.create_event(date, name, place, capacity, price)
        TESTUSER.save()
        TESTUSER.event_id
        print(TESTUSER.event_tickets_condition(TESTUSER.event_id))

        print("--- Define discount code & percentage for each user: ---")
        admin_code = input("Enter Admin code: ")
        admin_discount = input("Enter admin discount: ")
        TESTUSER.discount_define(admin_code, "admin", admin_discount)
        student_code = input("Enter student code: ")
        student_discount = input("Enter student discount: ")
        TESTUSER.discount_define(student_code, "student", student_discount)
        employee_code = input("Enter employee code: ")
        employee_discount = input("Enter employee discount: ")
        TESTUSER.discount_define(employee_code, "employee", employee_discount)
        user_code = input("Enter user code: ")
        user_discount = input("Enter user discount: ")
        TESTUSER.discount_define(user_code, "user", user_discount)

    else:
        print("---user login--- | ---welcome---")
        input("\nPress Enter to see all events")
        print(TESTUSER.show_all_events())
        event_id = input("Enter event ID: ")
        tickets = int(input("Enter number of tickets: "))
        code = input("Enter discount code: ")
        if code == "":
            code = None
        print(TESTUSER.select_event(event_id, tickets, code))

        purchase = int(input("Enter price to complete your purchase: "))
        TESTUSER.buy_ticket(purchase)
