# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:19:19 2021

@author: Business Analyst
"""
#%%
import random
def jprandomizer():
    out = ["1","X","2"]
    for x in range(1,18):
        x = random.choice(out)
        print(x,end="")

#%%