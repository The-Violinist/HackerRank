# Circular Array Rotation
# https://www.hackerrank.com/challenges/circular-array-rotation

# Shift all elements in an array to the right by 'k' number of indexes. Loop back to beginning when reaching the end of the array.

a = [3,4,5]                                             # Sample array
k = 1                                                   # number of rotations
queries = [0,1,2]                                       # Find the elements at the following indexes following the rotations

def circularArrayRotation(a, k, queries):
    # Find the relative placement difference in the array
    if k % len(a) == 0:                                 # No shift if k is divisible by the length of the array
        diff = 0
    elif k < len(a):                                    # If k is less than the length of the array, the difference is k itself
        diff = k
    else:                                               # Otherwise the difference is the remainder of k / the length of the array
        diff = k % len(a)
    
    # Create list of the elements at the indexes in 'queries' after the rotations
    query_results = []
    for item in queries:
        num = item - diff
        query_results.append(a[num])
    return query_results

print(circularArrayRotation(a, k, queries))
