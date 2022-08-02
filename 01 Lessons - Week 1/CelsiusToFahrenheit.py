# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:22:59 2021

@author: Business Analyst
"""
#%%
def celsius_to_fahrenheit():
    celsius_str = input("Enter the Celsius Value: ")
    if celsius_str:
        if celsius_str.isdigit():
            celsius = int(celsius_str)
            fahren = ((9/5)*celsius_str)+32 
            print("The Celsius Temp ",celsius," is equivalent to ",fahren," Fahrenheit")
        else:
            print("You must enter an integer. Bye.")
#%%