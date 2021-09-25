# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:53:08 2021

@author: Mohammad - Hadiomid
"""
# =============================================================================
#   Classwork 1 - Question 2    (1400-04-31 - Thursday - part 1)
# =============================================================================


# easier - sum, mean, multiple, max and min of 4 entry numbers
NUM1, NUM2, NUM3, NUM4 = input("Please enter your 4 numbers: ").split()
SUM = int(NUM1)+int(NUM2)+int(NUM3)+int(NUM4)
print('Sum : {:.6f}'.format(SUM))
print('Average : {:.6f}'.format((SUM/4)))
print('Multiple : {:.6f}'.format(int(NUM1)*int(NUM2)*int(NUM3)*int(NUM4)))
print('Max : {:.6f}'.format(max(int(NUM1), int(NUM2), int(NUM3), int(NUM4))))
print('Min : {:.6f}'.format(min(int(NUM1), int(NUM2), int(NUM3), int(NUM4))))
