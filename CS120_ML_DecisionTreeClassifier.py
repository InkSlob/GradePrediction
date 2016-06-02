import pickle
from sklearn.cross_validation import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.grid_search import RandomizedSearchCV
from sklearn.grid_search import GridSearchCV
from time import time
import os
import subprocess
from operator import itemgetter
from scipy.stats import randint


# Structure of ML data:
#  0	1	 2	  3	   4	5	 6	  7	   8	9					   
# Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 

#  10    11    12    13    14    15    16    17    18     19 
# AQ1 | AQ2 | AQ3 | AQ4 | AQ5 | AQ6 | AQ7 | AQ8 | AQ9 | AQ10 

#     20         21         22        23       24
#  A1 Final | A2 Final | A3 Final | Exam 1 | Exam 2

# ________________________________ LOADING DATA ____________________________
Corpus = open('CS120_ML_data.p', 'rb') 
corpus = pickle.load(Corpus)

five_week_df = corpus.loc[:, ['Q1', 'Q2', 'AQ1', 'AQ2', 'A1 Final']]
X = five_week_df.as_matrix()

corpus = corpus.as_matrix()

Y = corpus[:, 28:29]  # Grabs the letter grades

#Split data into train & test 80 / 20
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.20)

print "Grades data loaded and split for train and test.\n"
print "--------------------------------------------------"
print "Fitting Regression Model\t\tFitting Regression Model"
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=10)
regr_1.fit(x_train, y_train)
regr_2.fit(x_train, y_train)
regr_3.fit(x_train, y_train)
print "Predicting\t\tPredicting\t\tPredicting"
y_1 = regr_1.predict(x_test)
y_2 = regr_2.predict(x_test)
y_3 = regr_2.predict(x_test)

cv_val = 10

cv_1 = cross_val_score(regr_1, x_test, y_test, cv = cv_val)
cv_2 = cross_val_score(regr_2, x_test, y_test, cv = cv_val)
cv_3 = cross_val_score(regr_3, x_test, y_test, cv = cv_val)

mean_1 = cv_1.mean()
mean_2 = cv_2.mean()
mean_3 = cv_3.mean()
std_1 = cv_1.std()
std_2 = cv_2.std()
std_3 = cv_3.std()

print "Accuracy based on Cross Validation of", cv_val
print "\t \t Reg_1 \t Reg_2 \t Reg_3"
print "\t MEAN:", "\t", "%.3f" % round(mean_1, 3), "\t", "%.3f" % round(mean_2, 3), "\t", "%.3f" % round(mean_3, 3)
print "\t STD: ", "\t", "%.3f" % round(std_1,3), "\t", "%.3f" % round(std_2,3), "\t", "%.3f" % round(std_3,3)

print "END"