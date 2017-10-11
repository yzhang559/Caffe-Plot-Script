#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:06:52 2017

@author: yzhang559
"""

import load
from sklearn import svm
import time

def svm_baseline():
    training_data=load.load_train()
    test_data=load.load_test()
    
    start_time = time.time()
    
    # train
    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])
    
    # test
    predictions = [int(a) for a in clf.predict(test_data[0])]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
    print "Baseline classifier using an SVM."
    print "%s of %s values correct." % (num_correct, len(test_data[1]))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    svm_baseline()


