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
d_grades = dict()
current_student_grades = []

length = len(grades)    # 11,101 rows in grades

for row in range(1, length):
    student_id = int(grades[row][0])
    d_grades[student_id] = ""


for row in range(1, length):        # skip first row, header.
        # extract needed data
        student_id = int(grades[row][0])
        grade_calculated = float(grades[row][2]) / float(grades[row][3])
        assignment_name = str(grades[row][1])
        
        # Make a list to hold assignment and calculated grade [assignment name, grade]
        grade_list = []
        grade_list.append(assignment_name) 
        grade_list.append(grade_calculated)
        
        # add grades to the dictionary
        # student id already in the dictionary
        if student_id in d_grades:
            # extract grades from dictionary value by key
            #current_student_grades = d_grades.get(student_id)
            #print "ID: ", student_id, " : ", current_student_grades
            # add new assignment and grade to the student id in dict
            #current_student_grades = current_student_grades + grade_list
            d_grades[student_id] += str(grade_list[0]) 
            d_grades[student_id] += ", "
            d_grades[student_id] += str(grade_list[1]) 
            d_grades[student_id] += ", "
        else:
            print "ERROR IN Dict!"
            
        # clear grade list              
        grade_list[:] = []

# List holding grades extracted from dictionary
grades_all = []
# List holding individual grades
id_list = []

# loop through dict and split each id into an array, append these to grades_all[]
for key in d_grades:
    dict_spot = str(d_grades.get(key))
    #print dict_spot
    id_list = dict_spot.split(',')
    #print id_list
    grades_all.append(id_list)
    #id_list[:] = []

for j in range(0, len(grades_all)):
    if len(grades_all[j]) < 10:
        grades_all[j] = ''

final_grades = []

for i in grades_all:
    if (len(i)>0):
        final_grades.append(i)

with open("cs120_tabulated_grades.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(final_grades)



