# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 03:14:47 2021

@author: Business Analyst
"""

#%%

lis = ["lion","bear","monkey","chicken","daisy","iris"]
def who_is_there(lis): 
    if "bear" in lis:
        print("There's a bear.")
    if "lion" in lis:
        print("There's a lion.")
    if "daisy" in lis or "iris" in lis:
        print("There are flowers.")
    if "daisy" in lis and "iris" in lis:
        print("There are at least two flowers.")
    if "donkey" in lis:
        print("There is a donkey.")
    if "horse" not in lis:
        print("There is no horse in the list.")
    print("The list has",len(lis), "items")  
#%%