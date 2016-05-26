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
# "Switch" statement to take action on type of assignment



def error_print():
        print "This assignment was not found."
        return

def quiz():
        global grades
        global row
        print "\tIQF: "
        print "\tinside quiz function: ", grades[row][1]
        return
        
def switch(assignment):
        return {
            'Quiz 1': quiz(),
            'Quiz 2': quiz(),
            'Quiz 3': quiz(),
            'Quiz 4': quiz(),
            'Quiz 5': quiz(),
            'Quiz 6': quiz(),
            'Quiz 7': quiz(),
            'Quiz 8': quiz(),
            'Quiz 9': quiz(),
            'Quiz 10': quiz(),
        }.get(assignment, error_print())


length = len(grades)    # 11,101 rows in grades
count = 0

for row in range(0, 25):
        row_assignment = str(grades[row][1])
        print "Count: ", count
        count += 1
        #print switch(row_assignment)
        if "Quiz" in row_assignment:
            if "Attendance" in row_assignment:
                print "attendance quiz"
            else:
                print "recitation quiz"
                                        