# Sherlock and Squares
# https://www.hackerrank.com/challenges/sherlock-and-squares
# Determine how many square integers are in a given range

import math

a = 24                                                  # Start of range
b = 121                                                 # End of range

def squares(a, b):
    start = int(math.sqrt(a))                           # Find the floor of the square root of 'a'
    if start * start < a:                               # If the square of that number is less than 'a', add 1
        start += 1
    
    end = int(math.sqrt(b)) + 1                         # Find the upper square root number
    if end * end > b:                                   # If the square of that number is greater than 'b', subtract 1
        end -= 1

    num_list = []                                       # List to append all possible square roots
    for num in range(start, end + 1):                   # Add all numbers (inclusive) in the range: start - end
        num_list.append(num)
    return num_list

x = squares(a, b)
print(f"There are {len(x)} numbers between (inclusive) {a} and {b} which have integer square roots.\nThe square roots are: ", end = "")
for item in x:
    print(f"{item}  ", end = "")