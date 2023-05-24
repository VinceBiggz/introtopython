# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:03:18 2021

@author: Business Analyst
"""
#%%
def absolutevalue():
    mynumber = int(input("Enter a number:"))
    if mynumber == 0:
        print("The absolute value of 0 is 0")
    elif mynumber < 0:
        myabsolute = mynumber*-1
        print("The absolute value of ",mynumber, "is ", myabsolute)
    else :
        print("The absolute value of ",mynumber, "is ",mynumber)
#%%