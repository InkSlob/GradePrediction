import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score

# Structure of ML data:
#  0	1	 2	  3	   4	5	 6	  7	   8	9					   
# Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 

#  10    11    12    13    14    15    16    17    18     19 
# AQ1 | AQ2 | AQ3 | AQ4 | AQ5 | AQ6 | AQ7 | AQ8 | AQ9 | AQ10 

#     20         21         22        23       24
#  A1 Final | A2 Final | A3 Final | Exam 1 | Exam 2
Corpus = open('CS120_ML_data.p', 'rb') 
corpus = pickle.load(Corpus)

print "head: ", corpus.head()

five_week_df = corpus.loc[:, ['Q1', 'Q2', 'AQ1', 'AQ2', 'A1 Final']]
X = five_week_df.as_matrix()

corpus = corpus.as_matrix()

Y = corpus[:, 27:28]

print "Y shape: ", Y.shape

print "linear regression model initialized\n"
#Split data into train & test 80 / 20
corpus_x_train,corpus_x_test,shelf_y_train,shelf_y_test = \
				train_test_split(X,Y,test_size=0.20)

#Create linear regression object
regr = linear_model.LinearRegression()

#Train the model using training set
regr.fit(corpus_x_train, shelf_y_train)

#The Coefficients
coeff = regr.coef_
print "Coefficients: ", coeff, "\n"

#The root mean square error
pred = regr.predict(corpus_x_test)
RMSE = (np.mean(pred - shelf_y_test)**2)**0.5
print("Residual sum of squares: %.2f"% RMSE)

#Explain variance score: 1 is perfect prediction
var = regr.score(corpus_x_test, shelf_y_test)
print('Variance score: %.2f'% var)
print "__________________________________________________________________________________________________________\n"

print "r2 score: ", r2_score(shelf_y_test, pred)