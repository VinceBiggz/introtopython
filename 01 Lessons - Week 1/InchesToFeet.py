# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:39:05 2021

@author: Business Analyst
"""
#%%
def inches2feet():
    inches = input("Please enter the inches: ")
    if inches.isdigit():
        inch = int(inches)
        feet = inch//12 
        rem = inch % feet
        print(inch,"inches is ",feet,"feet and ",rem,"inches.")
#%%