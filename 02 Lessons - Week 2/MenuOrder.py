# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:25:33 2021

@author: Business Analyst
"""

#%%
def waitress():
    name = str(input("Please Enter your Name:"))
    while name:
        print("Welcome",name,". I'll be taking your order today.")
        order = []
        while True:
            next_item = input("Enter a menu item:")
            if next_item == "Done.":
                break
            order.append(next_item)
        print("Hello",name,"You have ordered",order)
        break
#%%        