# Subarray Division
# https://www.hackerrank.com/challenges/the-birthday-bar
# Calculates how many instances there are of consecutive "m" number of indexes which add up to "d"

### VARIABLES ###
s = [1, 2, 1, 3, 2]                     # A test array
d = 3                                   # Birth day
m = 2                                   # Birth month

### FUNCTIONS ###
def birthday(s, d, m):
    correct = 0                         # Counter for how many matches there are
    length = (len(s)-m)                 # Set the last starting point + m to not exceed the total length of the array 
    i = 0                               # Initiate the incrementor to 0
    while i <= length:                  # Loop thru the array and add up all possible consecutive indexes according to the variables above
        total = (sum(s[i:i+m]))         # Sum each consecutive pair in the array
        i +=1
        if total == d:                  # If the sum equals "d" then increment the matches (correct) by 1
            correct += 1
    return correct

### MAIN ###
print(birthday(s, d, m))
### END 3##