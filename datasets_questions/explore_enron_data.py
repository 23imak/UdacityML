#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print set(len(v) for v in enron_data.values())

#length of poi
numPois = []
for x in enron_data.values():
    if x['poi'] == True:
        numPois.append(x['poi'])
print "Number of POI : ", len(numPois)

#total stock value of James Prentice
print enron_data["PRENTICE JAMES"]["total_stock_value"]

#total mails send from Wesley Colwell to poi
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#total exercised stock options of Jefferey Skilling
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#total payment of poi
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

#no of people with quantified salary
salary_array = []
for x in enron_data.values():
    if x['salary'] == 'NaN':
        salary_array.append(x['salary'])

print len(enron_data) - len(salary_array)

#no of people with email address
email_array = []
for x in enron_data.values():
    if x['email_address'] == 'NaN':
        email_array.append(x['email_address'])
print len(enron_data) - len(email_array)

#percentage of people havong NaN in thier total payments
payment_array = []
for x in enron_data.values():
    if x['total_payments'] == 'NaN':
        payment_array.append(x['total_payments'])
print len(payment_array) #/146


# percentege of poi in dataset having NaN for thier total payments
enron_data_poi_array = []

for x in enron_data.values():
    if x['poi'] == True:
        enron_data_poi_array.append(x)

enron_data_poi_NaNpayments = []

for x in enron_data_poi_array:
    if x['total_payments'] == 'NaN':
        enron_data_poi_NaNpayments.append(x['total_payments'])

print len(enron_data_poi_NaNpayments)

