#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:10:25 2017

@author: yzhang559
"""
import glob
from scipy import misc
import numpy as np

# preprocess the training images

def load_train():
        labels=[]
        train_entity = np.empty((0,65536,3), "uint8")
        
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/0/*.PNG"):
                a1=misc.imread(image_path)

                if(len(a1.shape)==3):
                    d1=np.reshape(a1,(1,65536,3)) 
                else:
                    d1=np.reshape(a1,(65536,1))
                    BW1=np.empty((65536,0), "uint8")
                    BW1 = np.append(BW1, d1, axis=1)
                    BW1= np.append(BW1, d1, axis=1)
                    BW1 = np.append(BW1, d1, axis=1)
                    d1=np.reshape(BW1,(1,65536,3)) 
                    
                train_entity = np.append(train_entity, d1, axis=0)
                
                labels.append(0)
        
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/1/*.PNG"):
                a2=misc.imread(image_path)

                if(len(a2.shape)==3):
                    d2=np.reshape(a2,(1,65536,3)) 
                else:
                    d2=np.reshape(a2,(65536,1))
                    BW2=np.empty((65536,0), "uint8")
                    BW2 = np.append(BW2, d2, axis=1)
                    BW2= np.append(BW2, d2, axis=1)
                    BW2 = np.append(BW2, d2, axis=1)
                    d2=np.reshape(BW2,(1,65536,3)) 
                         
                train_entity = np.append(train_entity, d2, axis=0)
                
                labels.append(1)   
        
               
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/2/*.PNG"):
                a3=misc.imread(image_path)
                
                if(len(a3.shape)==3):
                    d3=np.reshape(a3,(1,65536,3)) 
                else:
                    d3=np.reshape(a3,(65536,1))
                    BW3=np.empty((65536,0), "uint8")
                    BW3 = np.append(BW3, d3, axis=1)
                    BW3= np.append(BW3, d3, axis=1)
                    BW3 = np.append(BW3, d3, axis=1)
                    d3=np.reshape(BW3,(1,65536,3)) 
                           
                train_entity = np.append(train_entity, d3, axis=0)
                
                labels.append(2)
                
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/3/*.PNG"):
                a4=misc.imread(image_path)
                
                if(len(a4.shape)==3):
                    d4=np.reshape(a4,(1,65536,3)) 
                else:
                    d4=np.reshape(a4,(65536,1))
                    BW4=np.empty((65536,0), "uint8")
                    BW4 = np.append(BW4, d4, axis=1)
                    BW4= np.append(BW4, d4, axis=1)
                    BW4 = np.append(BW4, d4, axis=1)
                    d4=np.reshape(BW4,(1,65536,3)) 
                    
                    
                train_entity = np.append(train_entity, d4, axis=0)
                labels.append(3)
            
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/4/*.PNG"):
                a5=misc.imread(image_path)
                
                if(len(a5.shape)==3):
                    d5=np.reshape(a5,(1,65536,3)) 
                else:
                    d5=np.reshape(a5,(65536,1))
                    BW5=np.empty((65536,0), "uint8")
                    BW5 = np.append(BW5, d5, axis=1)
                    BW5= np.append(BW5, d5, axis=1)
                    BW5 = np.append(BW5, d5, axis=1)
                    d5=np.reshape(BW5,(1,65536,3)) 
                           
                train_entity = np.append(train_entity, d5, axis=0)
                
                labels.append(4)
           
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/training-images/5/*.PNG"):
                a6=misc.imread(image_path)
                
                if(len(a6.shape)==3):
                    d6=np.reshape(a6,(1,65536,3)) 
                else:
                    d6=np.reshape(a6,(65536,1))
                    BW6=np.empty((65536,0), "uint8")
                    BW6 = np.append(BW6, d6, axis=1)
                    BW6= np.append(BW6, d6, axis=1)
                    BW6 = np.append(BW6, d6, axis=1)
                    d6=np.reshape(BW6,(1,65536,3)) 
                        
                train_entity = np.append(train_entity, d6, axis=0)
                
                labels.append(5)
        
        train_entity=np.reshape(train_entity,(6000,196608)) 
        train_label=np.asarray(labels)
        train_arr=(train_entity,train_label)
        print 'Train load Done!'
        return train_arr

def load_test():
        tlabels=[]
        test_entity = np.empty((0,65536,3), "uint8")
        
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/test-images/0/*.PNG"):
                ta1=misc.imread(image_path)
                
                if(len(ta1.shape)==3):
                    td1=np.reshape(ta1,(1,65536,3)) 
                else:
                    td1=np.reshape(ta1,(65536,1))
                    tBW1=np.empty((65536,0), "uint8")
                    tBW1 = np.append(tBW1, td1, axis=1)
                    tBW1= np.append(tBW1, td1, axis=1)
                    tBW1 = np.append(tBW1, td1, axis=1)
                    td1=np.reshape(tBW1,(1,65536,3)) 
                    
                test_entity = np.append(test_entity, td1, axis=0)
                
                tlabels.append(0)
        
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/test-images/1/*.PNG"):
                ta2=misc.imread(image_path)

                if(len(ta2.shape)==3):
                    td2=np.reshape(ta2,(1,65536,3)) 
                else:
                    td2=np.reshape(ta2,(65536,1))
                    tBW2=np.empty((65536,0), "uint8")
                    tBW2 = np.append(tBW2, td2, axis=1)
                    tBW2= np.append(tBW2, td2, axis=1)
                    tBW2 = np.append(tBW2, td2, axis=1)
                    td2=np.reshape(tBW2,(1,65536,3)) 
                         
                test_entity = np.append(test_entity, td2, axis=0)
                
                tlabels.append(1)   
        
               
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/test-images/2/*.PNG"):
                ta3=misc.imread(image_path)
                
                if(len(ta3.shape)==3):
                    td3=np.reshape(ta3,(1,65536,3)) 
                else:
                    td3=np.reshape(ta3,(65536,1))
                    tBW3=np.empty((65536,0), "uint8")
                    tBW3 = np.append(tBW3, td3, axis=1)
                    tBW3= np.append(tBW3, td3, axis=1)
                    tBW3 = np.append(tBW3, td3, axis=1)
                    td3=np.reshape(tBW3,(1,65536,3)) 
                           
                test_entity = np.append(test_entity, td3, axis=0)
                
                tlabels.append(2)
                
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/test-images/3/*.PNG"):
                ta4=misc.imread(image_path)
                
                if(len(ta4.shape)==3):
                    td4=np.reshape(ta4,(1,65536,3)) 
                else:
                    td4=np.reshape(ta4,(65536,1))
                    tBW4=np.empty((65536,0), "uint8")
                    tBW4 = np.append(tBW4, td4, axis=1)
                    tBW4= np.append(tBW4, td4, axis=1)
                    tBW4 = np.append(tBW4, td4, axis=1)
                    td4=np.reshape(tBW4,(1,65536,3)) 
                    
                    
                test_entity = np.append(test_entity, td4, axis=0)
                tlabels.append(3)
            
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/test-images/4/*.PNG"):
                ta5=misc.imread(image_path)
                
                if(len(ta5.shape)==3):
                    td5=np.reshape(ta5,(1,65536,3)) 
                else:
                    td5=np.reshape(ta5,(65536,1))
                    tBW5=np.empty((65536,0), "uint8")
                    tBW5 = np.append(tBW5, td5, axis=1)
                    tBW5= np.append(tBW5, td5, axis=1)
                    tBW5 = np.append(tBW5, td5, axis=1)
                    td5=np.reshape(tBW5,(1,65536,3)) 
                           
                test_entity = np.append(test_entity, td5, axis=0)
                
                tlabels.append(4)
           
        for image_path in glob.glob("/Users/Jenny/Desktop/imageResize/test-images/5/*.PNG"):
                ta6=misc.imread(image_path)
                
                if(len(ta6.shape)==3):
                    td6=np.reshape(ta6,(1,65536,3)) 
                else:
                    td6=np.reshape(ta6,(65536,1))
                    tBW6=np.empty((65536,0), "uint8")
                    tBW6 = np.append(tBW6, td6, axis=1)
                    tBW6= np.append(tBW6, td6, axis=1)
                    tBW6 = np.append(tBW6, td6, axis=1)
                    td6=np.reshape(tBW6,(1,65536,3)) 
                        
                test_entity = np.append(test_entity, td6, axis=0)              
                tlabels.append(5)
                
        test_entity=np.reshape(test_entity,(1200,196608))       
        test_label=np.asarray(tlabels)
        test_arr=(test_entity,test_label)
        print 'Test load Done!'
        
        return test_arr   
        


    
    