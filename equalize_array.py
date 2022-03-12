# Equaliz the Array
# https://www.hackerrank.com/challenges/equality-in-a-array
# Determines how many items must be removed from the array to make all items the same value

from collections import Counter

n = 5                                               # Lenght of the array
# arr = [3, 3, 2, 1, 3]
arr = [1,2,3,1,2,3,3,3]                             # List of integers

def equalizeArray(arr):
    counts = Counter(num for num in arr)            # Create a dictionary where k:v = item:occurrences
    values = counts.values()                        # List of all values
    max_val = max(values)                           # Greatest number in values
    return len(arr) - max_val                       # Subtract the greatest value from the length of the array
print(equalizeArray(arr))