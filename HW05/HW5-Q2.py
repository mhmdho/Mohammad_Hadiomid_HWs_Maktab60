# -*- coding: utf-8 -*-
"""
Created on Tue Aug  31 15:00:01 2021

@author: Lenovo
"""

class Sphere:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        while True: #while the user does not enter a correct number it countinues
            try:
                #int(self.radius) #if the user enter character, it ask radius again
                self.radius = int(self.radius)
                if self.radius <= 0: #Check number to be +
                    raise 
                else:
                    break
            except Exception: #raise if the user input not + or not int
                print('You Entered incorect value!!!;',
                      'radius cannot be (-), (0) or (character)!')
                self.radius = input('Enter radius again:')

    def area(self):
        return f'Area = {4 * self.pi * self.radius**2}'

    def Volume(self):
        return f'Volume = {(4 / 3) * self.pi * self.radius**3}'

r = input('Enter radius:')
S = Sphere(r)
print(S.area())
print(S.Volume())
