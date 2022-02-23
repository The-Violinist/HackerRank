# Plus Minus
# https://www.hackerrank.com/challenges/plus-minus
# This finds the ratio of positive, negative, and zero numbers in an array and returns the percentage to 6 decimal places

### VARIABLES ###
arr = (1, 3, 0, -4, 3)                                                      # Sample array of integers

### FUNCTIONS ###
def plusMinus(arr):
    plus = 0                                                                # Set positive counter at 0
    minus = 0                                                               # Set negative counter at 0
    n = (len(arr))                                                          # Length of the array
    for i in arr:                                                           # Loop thru array and calculate the instances of positives and negatives
        if (i > 0):
            plus += 1
        elif (i < 0):
            minus += 1
    formatted_plus = "{:.6f}".format(plus / n)                              # Format to 6 decimal places the percentage of each instance
    formatted_minus = "{:.6f}".format(minus / n)
    formatted_zero = "{:.6f}".format((n - plus - minus) / n)
    print(f"{formatted_plus}\n{formatted_minus}\n{formatted_zero}")
    #print(f"{formatted_plus} are positive\n{formatted_minus} are negative\n{formatted_zero} are zeros")     # Print the outcome in a verbose manner

### MAIN ###
plusMinus(arr)
### END ###