# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:39:53 2021

@author: Business Analyst


Problem 2_6:
Let's continue with our simulation of dice by rolling two of them. This time
each die can come up with a number from 1 to 6, but you have two of them. The
result or outcome is taken to be the sum of the pips on the two dice. Write a 
program that will roll 2 dice and produce the outcome. This time let's roll 
the two dice 100 times. Print the outcomes one outcome per line.
"""
#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    for x in range(431,531):
        x = random.randint(1,6) 
        y = random.randint(1,6)
        z = x + y
        #print(x,y,end="")
        #print()
        print(z)

   
#%%
"""
Test run with seed 82, but make sure that you submit with the seed 431:

problem2_6()
6
8
4
9
3
8
6
5
7
5
7
6
5
6
3
9
4
8
11
'
'
'
9
6
7
10
4

"""