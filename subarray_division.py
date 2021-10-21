# m is the birth month and d is the day
# Calculates how many instances there are of consecutive "m" number of indexes which add up to "d"
### VARIABLES ###
s = [1, 2, 1, 3, 2]
d = 3
m = 2

### FUNCTIONS ###
def birthday(s, d, m):
    correct = 0
    #Set the last starting point + m to not exceed the total length of the array 
    length = (len(s)-m)
    #Set the incrementor to 0
    i = 0
    #Loop thru the array and add up all possible consecutive indexes according to the variables above
    while i <= length:
        total = (sum(s[i:i+m]))
        i +=1
        #If the total of the indexes equals "d" then increment the matches (correct) by 1
        if total == d:
            correct += 1
    print(correct)
    # return correct

### MAIN ###
birthday(s, d, m)
### END 3##