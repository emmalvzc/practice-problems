# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:15:25 2020

@author: Dell
"""


def _sum(numbers):
    total_addition = 0
    for number in numbers:
        total_addition += number
        
    return total_addition


a = _sum([1,2,3,100])
print(a)

