# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 02:05:48 2021

@author: Lenovo
"""

# Question 1
print( "\nQuestion 1:")
class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
       
class School:
    def __init__(self, students):
        self.students= students            

    def avg(self):
        self.a_avg = 0
        self.h_avg = 0
        self.w_avg = 0
        for i in self.students:
            self.a_avg += i.age
            self.h_avg += i.height
            self.w_avg += i.weight
        self.a_avg = self.a_avg/len(self.students)
        self.h_avg = self.h_avg/len(self.students)
        self.w_avg = self.w_avg/len(self.students)

        print(f"Age average = {self.a_avg}")
        print(f"Height average = {self.h_avg}")
        print(f"Weight average = {self.w_avg}")


na = int(input('Enter number of students:'))
aa = list(map(int, input('Enter age of students:').split()))
ha = list(map(int, input('Enter height of students:').split()))
wa = list(map(int, input('Enter weight of students:').split()))

listA=[]
for i in range(na):
    listA.append(Student(aa[i],ha[i],wa[i]))

nb = int(input('Enter number of students:'))
ab = list(map(int, input('Enter age of students:').split()))
hb = list(map(int, input('Enter height of students:').split()))
wb = list(map(int, input('Enter weight of students:').split()))

listB=[]
for i in range(nb):
    listB.append(Student(ab[i],hb[i],wb[i]))

A = School(listA)
B = School(listB)
print('\nClass A:')
A.avg()
print('\nClass B:')
B.avg()

if A.h_avg > B.h_avg:
    print('\nHeight of Class A is more')
elif A.h_avg < B.h_avg:
    print('\nHeight of Class B is more')
else:
    if A.w_avg > B.w_avg:
        print('\nWeight of Class A is more')
    elif A.w_avg < B.w_avg:
        print('\nWeight of Class B is more')
    else:
        print('\n---Same---')
        



# Question 2
print( "\nQuestion 2:")
class Cell:
    def __init__(self, typee):
        self.typee = typee
    
    def __str__(self):
        return f'{self.typee}'

class Board:
    def __init__ (self):
        self.size = 3
        self.cells = []
        for i in range(self.size**2 + 1):
            c = Cell('')
            self.cells.append(c)

    def show(self):
       counter = 1
       for i in range(self.size):
           for j in range(self.size):
               print(f'{counter}: {self.cells[counter]}', end='\t')
               counter += 1
           print('\n')

    def cl(self, k):        
        return f'{self.cells[k]}'

    def cl2(self, k, inn):        
        self.cells[k] = inn

 
class Player:
    def __init__ (self, name, smbl):
        self.name = name
        self.smbl = 'X'

u = Player(input("Enter your name:"), 'X')
pc = Player('PC' , 'O')

b = Board()
b.show()

import random
while True:
    Action = int(input(f"{u.name} Enter Number to put X: "))
    while b.cl(Action) != '':
        Action = int(input(f"{u.name} this cell is filled enter another one: "))
    else: 
        b.cl2(Action, 'X')
    wintest = [b.cl(1) + b.cl(2) + b.cl(3),
               b.cl(4) + b.cl(5) + b.cl(6),
               b.cl(7) + b.cl(8) + b.cl(9),
               b.cl(1) + b.cl(4) + b.cl(7),
               b.cl(2) + b.cl(5) + b.cl(8),
               b.cl(3) + b.cl(6) + b.cl(9),
               b.cl(1) + b.cl(5) + b.cl(9),
               b.cl(3) + b.cl(5) + b.cl(7)]
    if 'XXX' in wintest:
        b.show()
        print(f'\n{u.name} is the winner')
        break
    else:
        f = []
        for j in range(1, 10):
            f.append(b.cl(j))
        if '' not in f:
            print("OPS, No winner!!!")
            break
        
    if 'XX' in wintest:
        if wintest.index('XX') == 0:
            if b.cl(1) == '':
                b.cl2(1, 'O')
            elif b.cl(2) == '':
                b.cl2(2, 'O')
            else:
                b.cl2(3, 'O')
        elif wintest.index('XX') == 1:
            if b.cl(4) == '':
                b.cl2(4, 'O')
            elif b.cl(5) == '':
                b.cl2(5, 'O')
            else:
                b.cl2(6, 'O')
        elif wintest.index('XX') == 2:
            if b.cl(7) == '':
                b.cl2(7, 'O')
            elif b.cl(8) == '':
                b.cl2(8, 'O')
            else:
                b.cl2(9, 'O')
        elif wintest.index('XX') == 3:
            if b.cl(4) == '':
                b.cl2(4, 'O')
            elif b.cl(7) == '':
                b.cl2(7, 'O')
            else:
                b.cl2(1, 'O')
        if wintest.index('XX') == 4:
            if b.cl(2) == '':
                b.cl2(2, 'O')
            elif b.cl(5) == '':
                b.cl2(5, 'O')
            else:
                b.cl2(8, 'O')
        elif wintest.index('XX') == 5:
            if b.cl(3) == '':
                b.cl2(3, 'O')
            elif b.cl(6) == '':
                b.cl2(6, 'O')
            else:
                b.cl2(9, 'O')
        elif wintest.index('XX') == 6:
            if b.cl(5) == '':
                b.cl2(5, 'O')
            elif b.cl(9) == '':
                b.cl2(9, 'O')
            else:
                b.cl2(1, 'O')
        elif wintest.index('XX') == 7:
            if b.cl(3) == '':
                b.cl2(3, 'O')
            elif b.cl(7) == '':
                b.cl2(7, 'O')
            else:
                b.cl2(5, 'O')
    else:    
        while True:
            rnd = random.randint(1, 9)
            if b.cl(rnd) == '':
                b.cl2(rnd, 'O')
                break
    b.show()
    wintest = [b.cl(1) + b.cl(2) + b.cl(3),
               b.cl(4) + b.cl(5) + b.cl(6),
               b.cl(7) + b.cl(8) + b.cl(9),
               b.cl(1) + b.cl(4) + b.cl(7),
               b.cl(2) + b.cl(5) + b.cl(8),
               b.cl(3) + b.cl(6) + b.cl(9),
               b.cl(1) + b.cl(5) + b.cl(9),
               b.cl(3) + b.cl(5) + b.cl(7)]
    if 'OOO' in wintest:
        print(f'PC is the winner')
        break




# Question 3
print( "\nQuestion 3:")
class rectangle:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def outline(self):
        return (self.x + self.y)*2

    def area(self):
        return self.x * self.y
      
    def result(Self):
        print(f"\nfor x = {Self.x} and y = {Self.y}")
        print(f"   outline is {Self.outline()}")
        print(f"   area is {Self.area()}")

R = rectangle( int(input("Enter x = ")), int(input("Enter y = ")) )
R.result()






