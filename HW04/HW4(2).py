# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:38:56 2021

@author: Lenovo
"""


print('\n ......Question 2...... \n')
import numpy as np
import math
class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.co_height = 1  #height coefficient
        self.z = 0

    def area(self):
        return f' Area = {self.width * self.length * self.co_height}'
        
    def perimeter(self):
        return f' Perimeter = {(self.width + self.length)*2}'
        
    def draw(self):
        print('\n')
        for i in range(math.ceil(self.width * self.co_height)):
            print((self.width - i)*self.z * ' ', '* ' * self.length)


class Rectangle(Shape):
    pass

class Square(Shape):
    def __init__(self, width):
        length = width
        super().__init__(width, length)

class Parallelogram(Shape):
    def __init__(self, width, length):
        super().__init__(width, length)
        self.co_height = 1/(np.sqrt(2))
        self.z = 1

class Rhombus(Shape):
    def __init__(self, width):
        length = width
        super().__init__(width, length)
        self.co_height = 1/(np.sqrt(2))
        self.z = 1

class Diamond(Shape):
    def __init__(self, width):
        length = width
        super().__init__(width, length)

    def draw(self):
        self.co_height = np.sqrt(2)
        print('\n')
        n = self.width * 2
        for i in range(1, n, 2):
            print(" " * (n - i), " *" * i)
        for i in range(n - 3 , 0, -2):
            print(" "*(n-i), " *"*i)
'''
        for i in range(self.width):
            print((b - round(i * self.co_height)) * ' ' + ' * ' * round(i * self.co_height))
        for j in range(self.width):
            print(round(j * self.co_height)* ' ' + ' * ' * (b - round(j * self.co_height)))
'''

print('\n')
p = Diamond(6)
print(p.area())
print(p.perimeter())
p.draw()               
