# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:42:49 2021

@author: Business Analyst
"""

""" 
Problem 2_3:
Write a function problem2_3() that should have a 'for' loop that steps
through the list below and prints the name of the state and the number of
letters in the state's name. You may use the len() function.
Here is the output from mine:
In [70]: problem2_3(newEngland)
Maine has 5 letters.
New Hampshire has 13 letters.
Vermont has 7 letters.
Rhode Island has 12 letters.
Massachusetts has 13 letters.
Connecticut has 11 letters.

The function is started for you.  The grader will not use the list newEngland
so don't use the variable newEngland inside your function.
"""
#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for item in range(len(ne)):
        print(ne[item],"has",len(ne[item]),"letters.")
#%%