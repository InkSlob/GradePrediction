import csv
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import pickle

# make a grade container: reader is list, row is list
grades = []
count = 0

#494 grade id entries
with open('cs120_tabulated_grades.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        grades.append(row)
        count += 1
f.close()


# Structure of ML data:
#  0	1	 2	  3	   4	5	 6	  7	   8	9					   
# Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 

#  10    11    12    13    14    15    16    17    18     19 
# AQ1 | AQ2 | AQ3 | AQ4 | AQ5 | AQ6 | AQ7 | AQ8 | AQ9 | AQ10 

#     20         21         22        23       24
#  A1 Final | A2 Final | A3 Final | Exam 1 | Exam 2

df_grade = []

for line in grades:
	length = len(line) - 1
	line_grade = np.zeros(25)
	for cell in range(0, length):
		
		item = str(line[cell])
		# _______________________ QUIZ _______________________________________
		if "Quiz 1" in item and "Attendance" not in item and '10' not in item:
			line_grade[0] = line[cell + 1]
		if "Quiz 2" in item and "Attendance" not in item:
			line_grade[1] = line[cell + 1]
		if "Quiz 3" in item and "Attendance" not in item:
			line_grade[2] = line[cell + 1]
		if "Quiz 4" in item and "Attendance" not in item:
			line_grade[3] = line[cell + 1]
		if "Quiz 5" in item and "Attendance" not in item:
			line_grade[4] = line[cell + 1]
		if "Quiz 6" in item and "Attendance" not in item:
			line_grade[5] = line[cell + 1]
		if "Quiz 7" in item and "Attendance" not in item:
			line_grade[6] = line[cell + 1]
		if "Quiz 8" in item and "Attendance" not in item:
			line_grade[7] = line[cell + 1]
		if "Quiz 9" in item and "Attendance" not in item:
			line_grade[8] = line[cell + 1]
		if "Quiz 10" in item and "Attendance" not in item:
			line_grade[9] = line[cell + 1]
		# ___________________ Attendance Quiz _____________________________
		if "Attendance Quiz 1" in item:
			line_grade[10] = line[cell + 1]
		if "Attendance Quiz 2" in item:
			line_grade[11] = line[cell + 1]
		if "Attendance Quiz 3" in item:
			line_grade[12] = line[cell + 1]
		if "Attendance Quiz 4" in item:
			line_grade[13] = line[cell + 1]
		if "Attendance Quiz 5" in item:
			line_grade[14] = line[cell + 1]
		if "Attendance Quiz 6" in item:
			line_grade[15] = line[cell + 1]
		if "Attendance Quiz 7" in item:
			line_grade[16] = line[cell + 1]
		if "Attendance Quiz 8" in item:
			line_grade[17] = line[cell + 1]
		if "Attendance Quiz 9" in item:
			line_grade[18] = line[cell + 1]
		if "Attendance Quiz 10" in item:
			line_grade[19] = line[cell + 1]
		# ___________________ Assignments __________________________________
		if "A1 Final Score" in item:
			line_grade[20] = line[cell + 1]
		if "A2 Final Score" in item:
			line_grade[21] = line[cell + 1]
		if "A3 Final Score" in item:
			line_grade[22] = line[cell + 1]
		# ___________________ Exams _______________________________________
		if "Exam 1" in item:
			line_grade[23] = line[cell + 1]
		if "Exam 2" in item:
			line_grade[24] = line[cell + 1]

	df_grade.append(line_grade)

df = pd.DataFrame(df_grade, columns = ['Q1', 'Q2',  'Q3',  'Q4',  'Q5',  'Q6',  'Q7',  \
	'Q8',  'Q9',  'Q10', 'AQ1', 'AQ2',  'AQ3',  'AQ4',  'AQ5',  'AQ6',  'AQ7',  'AQ8', \
	'AQ9',  'AQ10', 'A1 Final',  'A2 Final',  'A3 Final',  'Exam 1',  'Exam 2'])

df['Q_Total']=(df['Q1']+df['Q2']+df['Q3']+df['Q4']+df['Q5']+df['Q6']+df['Q7']+df['Q8']+\
			   df['Q9']+df['Q10'])/10
df['AQ_Total']=(df['AQ1']+df['AQ2']+df['AQ3']+df['AQ4']+df['AQ5']+df['AQ6']+df['AQ7']+\
				df['AQ8']+df['AQ9']+df['AQ10'])/10
df['Final_Grade']=df['Q_Total']*0.15+df['AQ_Total']*0.05+df['A1 Final']*0.1+\
				  df['A2 Final']*0.15+df['A3 Final']*0.25+df['Exam 1']*0.15+\
				  df['Exam 2']*0.15

# Letter grade function

def letter_grade(score):
	score = float(score)
	if score >= 0.93:
		#g = str('A')
		g = 100
		return g
	if score >= 0.90 and score < 0.93:
		#g = str('A-')
		g = 93
		return g
	if score >= 0.88 and score < 0.90:
		#g = str('B+')
		g = 90
		return g
	if score >= 0.82 and score < 0.88:
		#g = str('B')
		g = 88
		return g
	if score >= 0.80 and score < 0.82:
		#g = str('B-')
		g = 82
		return g
	if score >= 0.78 and score < 0.80:
		#g = str('C+')
		g = 80
		return g
	if score >= 0.70 and score < 0.78:
		#g = str('C')
		g = 78
		return g
	if score >= 0.68 and score < 0.70:
		#g = str('C-')
		g = 70
		return g
	if score >= 0.60 and score < 0.68:
		#g = str('D')
		g = 68
		return g
	if score < 0.60:
		#g = str('F')
		g = 60
		return g

# copy final grade to letter grade
df['Letter_Grade']=df['Final_Grade']
df['Letter_Grade']=df['Letter_Grade'].apply(letter_grade)

print df.head(5)

# dump this dataframe (df) to a pickle file for later use
f = open('CS120_ML_data.p', 'wb')
pickle.dump(df, f)
f.close()