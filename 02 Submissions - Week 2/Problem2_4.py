# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:54:06 2021

@author: Business Analyst
"""
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    for x in range(70,80):
        x = 5 
        y = random.random() * x
        #print(y)
        z = 30 + y
        print(z,end=" ")

#%%
