# Repeat a string (s) an infinite number of times and find the occurences of 'a' until character n
import math
s = 'aba'
n = 10

def repeatedString(s, n):
    total = 0
    
    # Find how many characters are left after dividing n by the lenghth of the string
    remainder = n % len(s)
    
    # The number of complete iterations of the string
    times = math.floor(n / len(s))
    
    # The occurences of 'a' in each s
    a = 0
    for item in s:
        if item == 'a':
            a += 1
    
    # Occurences of 'a' in total complete iterations
    total += (a * times)

    # Add additional a's from the remainder
    for item in s:
        if remainder == 0:
            break
        elif item == 'a':
            total += 1
        remainder -= 1
    
    return total
print(repeatedString(s, n))
