# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 03:33:51 2021

@author: Business Analyst
"""
#%%
nlis = [2,4,8,105,210,-3,47,8,33,1]  # average should by 41.5
rlis = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4] # average is -9.215
def LisAverage(lis):
    items = len(lis)
    total = sum(lis)
    avg = float(total/items)
    print("The average of this list is",avg)
#%%
mylis = [10,20,30,40,50]

def LisAverage2(lis):
    sum_1 = 0
    fin = len(lis)
    for x in range(0,fin):
        sum_1 = sum_1 + lis[x]
        print(lis[x],end=" ")
        x = x + 1
    print()
    print("The Total is",sum_1)
    print("Number of items is",x)
    avg = sum_1/x
    print("The average of",lis,"is",avg)

#%%
def LisAvg(lis):
    ct = 0
    tot = 0
    for dig in lis:
        ct = ct + 1
        if dig:
            tot = tot + dig
    print(tot)
    print(ct)
    avg = tot/ct
    print("The average of",lis,"is ",avg)
#%%S