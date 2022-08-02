# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:50:09 2021

@author: Business Analyst
"""

#%%
def write_to_file():
    filename = input("Enter the Filename and Extension:")
    fopen = open(filename,'w')
    myname = input("Please enter your name:")
    myage = input("Please enter your age:")
    major = input("Please enter your major:")
    fopen.write("My name is "+ myname + "\n")
    fopen.write("My age is "+ myage + "\n")
    fopen.write("I am majoring in "+ major + "\n")
    fopen.write("\n")
#%%