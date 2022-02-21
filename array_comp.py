# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets
# 11-23-2020

# This function compares each value at the same index of 2 arrays. It keeps a tally of the greater number and returns the occurences of the higher values between [a,b].

import itertools
a = [1, 3, 6]
b = [2, 2, 4]

def compareTriplets(a, b):
    a_total = 0
    b_total = 0
    final = []
    # Compare the values at the same index between 2 arrays.
    for (a, b) in zip(a, b):
        if (a > b):             # If a > b, increment 'a' total by 1
            a_total += 1
        elif (b > a):           # If b > a, increment 'b' total by 1
            b_total +=1
    # Append the 'a' and 'b' totals to the final array
    final.append(a_total)
    final.append(b_total)
    return final

print(compareTriplets(a, b))