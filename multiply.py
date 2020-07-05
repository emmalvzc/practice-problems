# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 23:15:25 2020

@author: Dell
"""


def multiply(numbers):
    if numbers == []:
        return 0
    total_product = 1
    for number in numbers:
        total_product += number
        
    return total_product


a = multiply([])
print(a)

