# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:21:29 2021

@author: Lenovo
"""

import random
class Thrower:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.error = (self.height - self.weight) * (random.random()*1.5 + 0.5)
        #self.error = (self.height - self.weight) * (random.randint(5000, 20001)/10000)

    def show_error(self):
        return self.error

class Attendance:
    def __init__(self):
        self.throwers = []
        
    def get_thrower(self, thrower):
        self.throwers.append(thrower)
        self.throwers.sort(reverse = True, key = Thrower.show_error)

    def mean_error(self):
        sum_er = 0
        for thrw in self.throwers:
            sum_er += thrw.error
        return sum_er/len(self.throwers)


a1 = Thrower('Ali', 208, 105)
a2 = Thrower('Hadi', 195, 96)
a3 = Thrower('Taha', 194, 98)
a4 = Thrower('Hamed', 212, 109)
a5 = Thrower('Omid', 201, 102)

all_at = Attendance()
all_at.get_thrower(a1)
all_at.get_thrower(a2)
all_at.get_thrower(a3)
all_at.get_thrower(a4)
all_at.get_thrower(a5)

at_list = all_at.throwers

print('\n')
print('Results are as the following:')
print(f'mean of all errors = {all_at.mean_error()}', '\n')
print('Name', 'Height', 'Weight', 'Error', sep='\t')
for item in at_list:
    print(item.name, item.height, item.weight, item.show_error(),  sep='\t')


            