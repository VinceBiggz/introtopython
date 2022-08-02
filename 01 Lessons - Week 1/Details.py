# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:45:24 2021

@author: Business Analyst
"""
#%%
def details():
    """ Input first and last name, combine to one string and print """
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    city = input("Which City do You Live in: ")
    fullname = fname + " " + lname

    print("Your name is",fullname, " and you live in ",city,".")

#%%