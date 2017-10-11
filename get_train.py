# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 12:38:07 2017

@author: yzhang559
"""
import os

# Preprocess the training set
# Create train.txt by walking through the trainning dataset
i=-1

with open("train.txt", "w") as a:
    for path, subdirs, files in os.walk('/Users/Jenny/Desktop/10class/train'):
         for filename in files:
             f = os.path.join(path, filename)
             a.write(str(f) + ' '+str(i)+os.linesep) 
         i+=1