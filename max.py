# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 22:02:39 2020

@author: Dell
"""


def max_number(num_1, num_2):
    if num_1 > num_2:
        max_val = num_1
        return max_val
    max_val = num_2
    return max_val


a = max_number(100000.0,10000001.2)
print(a)
