#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###

clf = svm.SVC(kernel="rbf", C=10500)

t0 = time()

#Using 1% of data to train faster
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf = clf.fit(features_train,labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

print accuracy_score(pred,labels_test)

chris = []
for i in pred:
    if i == 1:
        chris.append(i)

print len(chris)

print "For 10th element: ", pred[10]
print "For 26th element: ", pred[26]
print "For 50th element: ", pred[50]



#########################################################



