#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

# Split data into training and testing
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, random_state=42, test_size=0.3)

# Fit data with sklearn decision trees algorithm
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

# Get the accuracy
from sklearn.metrics import accuracy_score
prediction = clf.predict(features_test)



print accuracy_score(prediction, labels_test)

print "Number of poi's in test set", sum(prediction)
print "Number of people in test set", len(features_test)
print "Precison: ", precision_score(prediction,labels_test)
print "Recall: ", recall_score(prediction,labels_test)

print "Actual predcitions", prediction
print "true test labels", labels_test

prediction[4] = 0
prediction[11] = 0
prediction[19] = 0
prediction[21] = 0

print prediction

print "Accuracy if prediction is 0 : ", accuracy_score(prediction,labels_test)




