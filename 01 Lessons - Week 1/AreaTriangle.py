# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:00:35 2021

@author: Business Analyst
"""
#%%
def areatriangle():
    b = input("Enter the base length: ")
    h = input("Enter the height: ")
    if b and h:
        if b.isdigit() and h.isdigit():
            b = int(b) 
            h = int(h)
            area=.5*b*h
            print("The area of a triangle of base ",b," and height ",h," is " ,area)
        else:
            print("Kindly enter an integer. Bye.")
    
    
#%%