# Calculate if a class will take place depending on the attendance of students

# Number of students who must be on time
k = 3

# Arrival times
a  = [-1,-3,4,2]

def angryProfessor(k, a):
    on_time = 0
    for item in a:
        if item <= 0:
            on_time += 1
    print(on_time)
    # If on time students are less than k, return "YES", class is cancelled
    if on_time < k:
        return "YES"
    else:
        return "NO"

print(angryProfessor(k, a))