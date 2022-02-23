# Repeated String
# https://www.hackerrank.com/challenges/repeated-string
# Repeat string 's' an infinite number of times and find the occurences of the letter 'a' until character 'n'
import math
s = 'aba'
n = 10

def repeatedString(s, n):
    remainder = n % len(s)                              # Find how many characters are left after dividing n by the lenghth of the string
    times = math.floor(n / len(s))                      # The number of complete iterations of the string
    a = 0                                               # The occurences of 'a' in each s
    
    for item in s:                                      # Calculate the total occurences of 'a' in string 's'
        if item == 'a':
            a += 1
    
    total = (a * times)                                 # Multiply those occurences by the total complete repetitions of 's'

    for item in s:                                      # Add additional a's from the remainder
        if remainder == 0:                              # Once remainder == 0, return the total
            return total
        elif item == 'a':
            total += 1
        remainder -= 1
    
print(repeatedString(s, n))