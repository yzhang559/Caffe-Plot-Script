#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:43:58 2017

@author: yzhang559
"""
# plot the train/test accuracy wrt iterarions (input is the console output during training process)
import matplotlib.pyplot as plt
import numpy as np

train_accuracy=[]
test_accuracy=[]
train_iter=np.linspace(0,24980,1250)
test_iter=np.linspace(0,25000,126)
print len(test_iter)

train_loss=[]
test_loss=[]

# input file
f = open('iter25000.txt', 'r')

for line in f:
    if('Train net output #0: accuracy ='in line):
        temp= line.split("Train net output #0: accuracy =",1)
        temp2=float(temp[1])
        train_accuracy.append(temp2)
    elif('Train net output #1: loss = ' in line):
        losstemp=line.split("Train net output #1: loss =",1)
        losstemp2=losstemp[1].split("(* 1",1)
        losstemp3=float(losstemp2[0])
        train_loss.append(losstemp3)
    elif('Test net output #0: accuracy = ' in line):
       test_temp =line.split('Test net output #0: accuracy =',1)
       test_temp2=float(test_temp[1])
       test_accuracy.append(test_temp2)
    elif('Test net output #1: loss =' in line):
        test_losstemp=line.split("Test net output #1: loss = ",1)
        test_losstemp2=test_losstemp[1].split("(* 1",1)
        test_losstemp3=float(test_losstemp2[0])
        test_loss.append(test_losstemp3)
       
#plot train_acc 
ftrain_accuracy = plt.figure()
plt.plot(train_iter,train_accuracy)
plt.ylim(0,1.0)
ftrain_accuracy.suptitle('train_accuracy vs iteration', fontsize=14)
plt.xlabel('iteration', fontsize=12)
plt.ylabel('accuracy', fontsize=12)
ftrain_accuracy.savefig('ftrain_accuracy.pdf', format='pdf')

#plot train_loss
ftrain_loss = plt.figure()
plt.plot(train_iter,train_loss)
plt.ylim(0,2.0)
ftrain_loss.suptitle('Train_loss vs Train_iteration', fontsize=14)
plt.xlabel('iteration', fontsize=12)
plt.ylabel('loss', fontsize=12)
ftrain_loss.savefig('ftrain_loss.pdf',format='pdf')

#plot test_acc 
ftest_accuracy = plt.figure()
plt.plot(test_iter,test_accuracy, 'r')
plt.ylim(0,1.0)
ftest_accuracy.suptitle('test_accuracy vs iteration', fontsize=14)
plt.xlabel('iteration', fontsize=12)
plt.ylabel('accuracy', fontsize=12)
ftest_accuracy.savefig('ftest_accuracy.pdf', format='pdf')

#plot test_loss
ftest_loss = plt.figure()
plt.plot(test_iter,test_loss)
plt.ylim(0,2.0)
ftest_loss.suptitle('Test_loss vs Test_iteration', fontsize=14)
plt.xlabel('iteration', fontsize=12)
plt.ylabel('loss', fontsize=12)
ftest_loss.savefig('ftest_loss.jpg')

#plot accuracy 
faccuracy = plt.figure()
plt.ylim(0,1.0)
plt.plot(train_iter,train_accuracy)
plt.plot(test_iter,test_accuracy, 'r')
faccuracy.suptitle('Accuracy vs Iteration', fontsize=14)
plt.xlabel('iteration', fontsize=12)
plt.ylabel('accuracy', fontsize=12)
faccuracy.savefig('accuracy.pdf', format='pdf')