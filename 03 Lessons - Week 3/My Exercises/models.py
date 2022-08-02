# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:44:36 2021

@author: Business Analyst
"""
#%%
ascars = {"Ford" : "Mustang","Mazda" : "Miata", "Scion" : "FR-S", 
"Subaru" : "BRZ","Dodge" : "Challenger", "Nissan" : "370Z", "Chevy" : "Camaro", 
"Hyundai" : "Genesis Coupe" , "MINI Cooper" : "Roadster"}

tup = ("Liam", "Taji", "Kung'u", "Wachira")

def models():
    for i in ascars.values():
        print(i)
#%%
def brands():
     for y in ascars.keys():
         print(y)
#%%