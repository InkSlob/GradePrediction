import csv

# make a grade container: reader is list, row is list
grades = []
count = 0

with open('Extracted_Grades.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        grades.append(row)
        count += 1
f.close()
# Rows: 'Enrollement_Id', 'Name', 'PointsAwarded', 'PointsPossible'

# grades 2 dimension list, inner list is 4 elements
#  a new dictionary for grades, will be a dictionary keyed by student id.  
#  each value in this dictionary will hold another dictionary for the specific grades.
d_grades = dict()
grade_list = []
current_student_grades = []

length = len(grades)    # 11,101 rows in grades

for row in range(1, length):        # skip first row, header.
        # extract needed data
        student_id = str(grades[row][0])
        grade_calculated = float(grades[row][2]) / float(grades[row][3])
        assignment_name = grades[row][1]
        
        # Make a list to hold assignment and calculated grade [assignment name, grade]
        grade_list.append(assignment_name) 
        grade_list.append(grade_calculated)
        
        # add grades to the dictionary
        # student id already in the dictionary
        if student_id in d_grades:
            # extract grades from dictionary value by key
            current_student_grades = d_grades[student_id]
            # add new assignment and grade to the student id in dict
            current_student_grades = current_student_grades + grade_list
            d_grades[student_id] = current_student_grades
        else:
            d_grades[student_id] = grade_list
        # clear grade list              
        grade_list[:] = []
        
        
# The if then statement for first entry is adding the first entry twice.
dict_len_original = len(d_grades)


# Removing the entries that are not complete.  Not sure why there are ids with only a couple grades
key_list = []

for key in d_grades:
    if len(d_grades[key]) < 10:
        key_list.append(key)

for k in key_list:
    del d_grades[k]

print "start: ", dict_len_original, " end: ", len(d_grades)


