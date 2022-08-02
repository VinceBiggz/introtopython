# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:02:13 2021

@author: Business Analyst
"""

#%%
import random

verbs=["goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def poem():
    for i in range (4):
        article = random.choice(articles)    
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        adverb = random.choice(adverbs)
    
        our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
        our_sentence = our_sentence.capitalize()
        
        print(our_sentence)
        #if i > 0 and i < 5:
           # print(our_sentence)
        
        
#%%S