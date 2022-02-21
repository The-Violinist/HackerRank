# Calculate if a class will take place depending on the attendance of students
# https://www.hackerrank.com/challenges/angry-professor

# Number of students who must be on time for class to continue
k = 3

# Arrival times by student. Integers greater than zero are late.
a  = [-1,-3,4,2]

def angryProfessor(k, a):
    on_time = 0
    # Sum the number of students who are on-time or early
    for item in a:
        if item <= 0:
            on_time += 1
    # If on time students are less than k, return "YES", class is cancelled
    if on_time < k:
        return "YES"
    else:
        return "NO"

print(angryProfessor(k, a))