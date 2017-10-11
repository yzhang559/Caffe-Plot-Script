# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 13:24:51 2017

@author: yzhang559
"""
import os

# Preprocess the validation set 
# Create val.txt by walking through the trainning dataset
i=9

path='/Users/Jenny/Desktop/10class/val/staircase_val/'
files = os.listdir(path)


with open("val9.txt", "w") as a:
         for filename in files:
             f = os.path.join(path, filename)
             a.write(str(f) + ' '+str(i)+os.linesep) 
             