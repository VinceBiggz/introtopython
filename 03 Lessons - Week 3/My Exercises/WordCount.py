# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:19:32 2021

@author: Business Analyst
"""

#%%
def wordcnt():
    myline = input('Please write a Sentence:')
    split = myline.split()
    mycounter = 0
    for word in split:
        mycounter += 1 
    print(split)
    print(mycounter)
#%%