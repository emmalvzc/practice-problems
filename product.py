# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:15:25 2020

@author: Dell
"""


def multiply_numbers(_list):
    total_product = 1
    for i in _list:
        total_product = total_product * i
        
    return total_product


a = multiply_numbers([2,3,10])
print(a)

