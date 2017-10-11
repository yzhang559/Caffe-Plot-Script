#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:10:25 2017

@author: yzhang559
"""
import glob
from scipy import misc
import numpy as np


def load_train():
        labels=[]
        train_entity = np.empty((65536,0), "uint8")
        
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/0/*.PNG"):
                    a1=misc.imread(image_path)
                    
                    if(len(a1.shape)==3):
                         a1=a1[:,:,0]
                    
                    d1=np.reshape(a1,(1,65536)) 
                    train_entity = np.append(train_entity, d1, axis=0)
                    labels.append(0)
        
                    
                
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/1/*.PNG"):
                a2=misc.imread(image_path)

                if(len(a2.shape)==3):
                    a2=a2[:,:,0]
                    
                d2=np.reshape(a2,(1,65536)) 
                train_entity = np.append(train_entity, d2, axis=0)
                labels.append(1)   
        
               
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/2/*.PNG"):
                a3=misc.imread(image_path)

                if(len(a3.shape)==3):
                    a3=a3[:,:,0]
                    
                d3=np.reshape(a3,(1,65536)) 
                train_entity = np.append(train_entity, d3, axis=0)
                labels.append(2)   
                
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/3/*.PNG"):
                a4=misc.imread(image_path)
                
                if(len(a4.shape)==3):
                    a4=a4[:,:,0]
                    
                d4=np.reshape(a4,(1,65536)) 
                train_entity = np.append(train_entity, d4, axis=0)
                labels.append(3)   
            
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/4/*.PNG"):
                a5=misc.imread(image_path)

                if(len(a5.shape)==3):
                    a5=a5[:,:,0]
                    
                d5=np.reshape(a5,(1,65536)) 
                train_entity = np.append(train_entity, d5, axis=0)
                labels.append(4)   
           
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/5/*.PNG"):
                a6=misc.imread(image_path)

                if(len(a6.shape)==3):
                   a6=a6[:,:,0]
                    
                d6=np.reshape(a6,(1,65536)) 
                train_entity = np.append(train_entity, d6, axis=0)
                labels.append(5)   
                
        train_label=np.asarray(labels)
        train_arr=(train_entity,train_label)
        print 'Train load Done!'
        return train_arr

def load_test():
    tlabels=[]
    test_entity = np.empty((0,65536), "uint8")
            
    for image_path in glob.glob("/Users/Jenny/Desktop/BWimage/test/0/*.PNG"):
                    ta1=misc.imread(image_path)
                    
                    if(len(ta1.shape)==3):
                         ta1=ta1[:,:,0]
                    
                    td1=np.reshape(ta1,(1,65536)) 
                    test_entity = np.append(test_entity, td1, axis=0)
                    
                    tlabels.append(0)
                    
    
    for image_path in glob.glob("/Users/Jenny/Desktop/BWimage/test/1/*.PNG"):
                    ta2=misc.imread(image_path)
    
                    if(len(ta2.shape)==3):
                         ta2=ta2[:,:,0]
                    
                    td2=np.reshape(ta2,(1,65536)) 
                             
                    test_entity = np.append(test_entity, td2, axis=0)
                    
                    tlabels.append(1)   
            
    print '1-------------------------------------'
    print test_entity.shape  
                   
    for image_path in glob.glob("/Users/Jenny/Desktop/BWimage/test/2/*.PNG"):
                    ta3=misc.imread(image_path)
                    
                    if(len(ta3.shape)==3):
                         ta3=ta3[:,:,0]
                    
                    td3=np.reshape(ta3,(1,65536)) 
                    test_entity = np.append(test_entity, td3, axis=0)
                    tlabels.append(2)
    
    for image_path in glob.glob("/Users/Jenny/Desktop/BWimage/test/3/*.PNG"):
                    ta4=misc.imread(image_path)
                    if(len(ta4.shape)==3):
                    
                        ta4=ta4[:,:,0]
                    
                    td4=np.reshape(ta4,(1,65536)) 
                    test_entity = np.append(test_entity, td4, axis=0)
                    tlabels.append(3) 
                
    for image_path in glob.glob("/Users/Jenny/Desktop/BWimage/test/4/*.PNG"):
                    ta5=misc.imread(image_path)
    
                    if(len(ta5.shape)==3):
                        ta5=ta5[:,:,0]
                    
                    td5=np.reshape(ta5,(1,65536)) 
                               
                    test_entity = np.append(test_entity, td5, axis=0)
                    
                    tlabels.append(4)
               
    for image_path in glob.glob("/Users/Jenny/Desktop/BWimage/test/5/*.PNG"):
                    ta6=misc.imread(image_path)
                    
                    if(len(ta6.shape)==3):
                        ta6=ta6[:,:,0]
                    
                    td6=np.reshape(ta6,(1,65536)) 
                            
                    test_entity = np.append(test_entity, td6, axis=0)              
                    tlabels.append(5)
                       
    test_label=np.asarray(tlabels)
    test_arr=(test_entity,test_label)
    print 'Test load Done!'
            
    return test_arr   
        


    
    