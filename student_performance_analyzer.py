# Name: Sophia Chang
# Period: AM
# Student Performance Analyzer

# Program introduction

print("======================================")
print("     STUDENT PERFORMANCE ANALYZER    ")
print("======================================")
print()
print("Enter the student's information below")
name = input("What's the student's name? ")
grade_level = int(input("What grade is the student in? "))
assignment_avg = float(input("What's the student's assignment average? "))
quiz_avg = float(input("What's the student's quiz average? "))
test_avg = float(input("What's the student's test average? "))
attendance = float(input("What's the student's attendance percentage? "))
missing_assignments = int(input("How many missing assignments does the student have? "))

def calculate_grade(assignment_avg, quiz_avg, test_avg):
    assignments = 0.3 * assignment_avg
    quizzes = 0.3 * quiz_avg
    tests = 0.4 * test_avg
    overall_grade = assignments + quizzes + tests
    print("Overall Grade:", overall_grade)

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

def attendance_status(attendance):
    if attendance >= 95:
        print("Attendance Status: Excellent Atendance")
    elif attendance >= 90:
        print("Attendance Status: Good Attendance")
    elif attendance >= 80:
        print("Attendance Status: Attendance Warning")
    else:
        print("Attendance Status: Poor Attendance")

def assignment_status(missing_assignments):
    if missing_assignments == 0:
        print("Missing Assignment Status: Excellent")
    elif missing_assignments <= 2:
        print("Missing Assignment Status: Good")
    elif missing_assignments <= 4:
        print("Missing Assignment Status: Warning")
    elif missing_assignments >= 5:
        print("Missing Assignment Status: Critical")

def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")

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

def check_good_standing(overall_grade, attendance):
    if (overall_grade >= 70 and attendance >= 90):
        print("Good Standing: YES")
    else:
        print("Good Standing: NO")

def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

user = input("Enter username: ")
pin = int(input("Enter PIN: "))

if user == student:
    