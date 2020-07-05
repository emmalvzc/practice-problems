# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:15:25 2020

@author: Dell
"""


def added_numbers(_list):
    total_addition = 0
    for i in _list:
        total_addition = total_addition + i
        
    return total_addition


a = added_numbers([1,2,3,100])
print(a)

