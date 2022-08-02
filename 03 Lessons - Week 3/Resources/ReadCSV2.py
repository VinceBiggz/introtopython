# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 07:27:22 2021

@author: Business Analyst
"""

#%%
import csv

def read_csv_file2(filename):
    """Reads a CSV file and prints each row without list brackets. """
    f = open(filename)
    for row in csv.reader(f):
        for x in row:
            print(x, end=' ')
        print()
    f.close()
#%%