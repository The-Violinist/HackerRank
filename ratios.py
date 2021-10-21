#This finds the ratio of positive, negative, and zero numbers

### VARIABLES ###
#Sample array of integers
arr = (1, 3, 0, -4, 3)

### FUNCTIONS ###
def plusMinus(arr):
    #Set positive and negative counters at 0
    plus = 0
    minus = 0
    #Initiate variable with the length of the array
    n = (len(arr))
    #Loop thru array and calculate the instances of positives and negatives
    for i in arr:
        if (i > 0):
            plus += 1
        elif (i < 0):
            minus += 1
    #Format to 6 decimal places the percentage of each instance
    formatted_plus = "{:.6f}".format(plus / n)
    formatted_minus = "{:.6f}".format(minus / n)
    formatted_zero = "{:.6f}".format((n - plus - minus) / n)
    #Print the outcome
    print(f"{formatted_plus} are positive\n{formatted_minus} are negative\n{formatted_zero} are zeros")

### MAIN ###
plusMinus(arr)
### END ###