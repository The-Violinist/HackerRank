# Grading Students Challenge
# https://www.hackerrank.com/challenges/grading
# Round grades up by 5 point increment. Below 40 (rounded) is fail. Otherwise, return the rounded grade.

grades = [73,67,38,33]
def gradingStudents(grades):
    rounded_grades = []                             # List for the rounded grades
    for grade in grades:
        if grade < 38:                              # If the grade is less than 38, don't round
            grade = grade
        elif grade % 5 > 2:                         # If the grade is 3 points towards the next increment, round to the next 5
            grade = grade + (5 - (grade % 5))
        else:                                       # Otherwise, don't change the grade
            grade = grade
        rounded_grades.append(grade)                # Append the rounded grades to the list
    return rounded_grades
print(gradingStudents(grades))