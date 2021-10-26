# "a" is a 2d array. This function adds the diagonals and finds the absolute difference.
# 11-23-2020

import itertools
a = ([1, 3, 6],[2, 2, 4],[8, 3, 1])
b = len(a)
c = b - 1
def diagonalDifference(arr):
    place_asc = 0
    total_asc = 0
    for group in arr:
        #Add diagonal from top left
        #group1[0]+group2[1]+group3[2]
        total_asc = total_asc + group[place_asc]
        place_asc += 1
    
    #Set starting point for 
    place_desc = c
    total_desc = 0
    for group in arr:
        #Add diagonal from top right
        #group1[2]+group2[1]+group3[0]
        total_desc = total_desc + group[place_desc]
        place_desc -= 1
    difference = int(abs(total_asc - total_desc))
    print(difference)
    return difference
diagonalDifference(a)