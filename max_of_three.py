# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:19:18 2020

@author: Dell
"""


def max_of_three(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_3:
        return num_2

    return num_3


a = max_of_three(20000,3000,1000)
print(a)
