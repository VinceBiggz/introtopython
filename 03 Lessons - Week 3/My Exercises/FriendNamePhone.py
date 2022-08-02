# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:33:37 2021

@author: Business Analyst
"""

#%%
import csv
def name_phone(csv_filename):
    fopen = open(csv_filename,'w', newline=' ')
    details = []
    newdetails = []
    # open the csv file here
    
    while True:
        nextname = input("Enter a friend's name, press return to end: ")
        if nextname == "":
            break              # break jumps out of the loop
        nextphone = input("Enter your friend's Phone number: ")
        print(nextname, nextphone) 
        newdetails.append(nextname)
        newdetails.append(nextphone)
        details.append(newdetails)
        print(details)
        for item in details:
            csv.writer(fopen).writerow(item)
        newdetails.clear()
    fopen.close()
        
        
        
        # add lines here to build a row (that is, a list) and append these
        # two pieces of data to it.  Write to the csv file
        
    # don't forget to close the csv file
        
#%% 