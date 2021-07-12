# Comparing 2 arrays
# 11-23-2020

import itertools
a = [1, 3, 6]
b = [2, 2, 4]

def compareTriplets(a, b):
    a_total = 0
    b_total = 0
    final = []
    for (x, y) in zip(a, b):
        if (x > y):
            a_total += 1
        elif (y > x):
            b_total +=1
    final.append(a_total)
    final.append(b_total)
    print(final)
    return final

compareTriplets(a, b)