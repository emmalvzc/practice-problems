# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:26:19 2020

@author: Dell
"""


def length(_list):
    counter = 0
    for i in _list:
        counter += 1
        
    return counter
        




a = length([1,2,3,4,5,6,7,8,9,100])
print(a)