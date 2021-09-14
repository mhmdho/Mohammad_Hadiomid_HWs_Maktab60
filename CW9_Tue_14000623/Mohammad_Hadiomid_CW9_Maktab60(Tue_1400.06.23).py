# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:35:08 2021

@author: Lenovo
"""


from datetime import datetime, timedelta

Pills = 10
pill_hour = timedelta(hours=8)
start_date = "2/19/2018 14:00"  # when consum of pills starts
start_date = datetime.strptime(start_date, '%m/%d/%Y %H:%M')

# datetime that user entered:
Entered_date = input("Enter datetime like sample --> "
                     "[Month/Day/Year Hour:Minute]: ")
Entered_date = datetime.strptime(Entered_date, '%m/%d/%Y %H:%M')

# check the next time for the next pill
next_pilltime = start_date
for i in range(Pills-1):
    next_pilltime += pill_hour
    Pills -= 1
    if next_pilltime > Entered_date:
        print('\npills remained:', Pills)
        print('next pill time:', next_pilltime)
        break
if next_pilltime <= Entered_date:
    print('\nNo pill remained.')
