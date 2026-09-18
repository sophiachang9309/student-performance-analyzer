# Name: Sophia Chang
# Period: AM
# Student Performance Analyzer

# Program introduction

print("======================================")
print("     STUDENT PERFORMANCE ANALYZER    ")
print("======================================")
print()
print("Enter the student's information below")

#Get Student information from the user
name = input("What's the student's name? ")
grade_level = int(input("What grade is the student in? "))
assignment_avg = float(input("What's the student's assignment average? "))
quiz_avg = float(input("What's the student's quiz average? "))
test_avg = float(input("What's the student's test average? "))
attendance = float(input("What's the student's attendance percentage? "))
missing_assignments = int(input("How many missing assignments does the student have? "))

#Calculate the student's overall grade
def calculate_grade(assignment_avg, quiz_avg, test_avg):
    assignments = 0.3 * assignment_avg
    quizzes = 0.3 * quiz_avg
    tests = 0.4 * test_avg
    overall_grade = assignments + quizzes + tests
    return overall_grade

overall_grade = calculate_grade(assignment_avg,quiz_avg,test_avg)

#Calculate the student's letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        print("Letter Grade: A")
    elif overall_grade >= 80:
        print("Letter Grade: B")
    elif overall_grade >= 70:
        print("Letter Grade: C")
    elif overall_grade >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")

#Calculate the student's attendance_status
def attendance_status(attendance):
    if attendance >= 95:
        print("Attendance Status: Excellent Attendance")
    elif attendance >= 90:
        print("Attendance Status: Good Attendance")
    elif attendance >= 80:
        print("Attendance Status: Attendance Warning")
    else:
        print("Attendance Status: Poor Attendance")

#Calculate the student's assignment status
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        print("Missing Assignment Status: Excellent")
    elif missing_assignments <= 2:
        print("Missing Assignment Status: Good")
    elif missing_assignments <= 4:
        print("Missing Assignment Status: Warning")
    elif missing_assignments >= 5:
        print("Missing Assignment Status: Critical")

#calculate whether the student is eligible to pass 
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Reason: Student passed all three requirements.")
            else: 
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")

#calculate whether the student qualifies for honors
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")

#checks whether or not the student has a good standing
def check_good_standing(overall_grade, attendance):
    if (overall_grade >= 70 and attendance >= 90):
        print("Good Standing: YES")
    else:
        print("Good Standing: NO")

#checks whether or not the student needs additional support
def check_support(overall_grade, attendance):
    if (overall_grade < 70) or (attendance < 80):
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

print("Student Login:")

user = input("Enter username: ")
pin = int(input("Enter PIN: "))

#Checks whether or not the student  can login
if user == "student":
    if pin == 1234:
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")

#administers a message to the student depending on the grade level
def grade_level_message(grade_level):
    if grade_level == 12:
        print("Senior year - finish strong!")
    elif grade_level == 11:
        print("Junior year - keep pushing!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 9:
        print("Welcome to your freshman year!")
    else:
        print("Invalid grade level.")

#checks what category the student is strong at
def strongest_category(assignment_avg, quiz_avg, test_avg):
    if (assignment_avg <= quiz_avg and quiz_avg <= test_avg) or (quiz_avg <= assignment_avg and assignment_avg <= test_avg):
        print("Strongest Category: Tests")
    elif (quiz_avg <= test_avg and test_avg <= assignment_avg) or (test_avg <= quiz_avg and quiz_avg <= assignment_avg):
        print("Strongest Category: Assignments")
    elif (test_avg <= assignment_avg and assignment_avg <= quiz_avg) or (assignment_avg <= test_avg and test_avg <= quiz_avg):
        print("Strongest Category: Quizzes")

print("=========================")
print("     Student summary     ")
print("=========================")
print()
print("Student:", name)
print("Grade level:", grade_level)
grade_level_message(grade_level)
print()
print("Assignment Average:", assignment_avg)
print("Quiz Average:", quiz_avg)
print("Test Average:", test_avg)
print("Overall Grade:", calculate_grade(assignment_avg, quiz_avg, test_avg))
print()
check_support(overall_grade,attendance)
print()
print("Attendance:", attendance)
attendance_status(attendance)
print("Missing Assignments:", missing_assignments)
assignment_status(missing_assignments)
print()
letter_grade(overall_grade)
check_good_standing(overall_grade, attendance)
strongest_category(assignment_avg,quiz_avg,test_avg)
check_high_honors(overall_grade, attendance, missing_assignments)
print()
check_eligibility(overall_grade, attendance, missing_assignments)

#checks whether or not the student is outstanding
def check_outstanding_status(overall_grade, attendance, missing_assignments):
    if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and missing_assignments == 0):
        print("Advanced Status: OUTSTANDING STUDENT")
    else:
        print("Advanced Status: STANDARD STUDENT STATUS")

check_outstanding_status(overall_grade, attendance, missing_assignments)
    