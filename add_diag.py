# Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference
# "a" is a 2d array. This function sums the diagonals and finds the absolute difference.
# Assumes that the input ('a') is an array of arrays where the lenght of each array is the same as the total number of arrays, thereby creating a square of integers. 
# 11-23-2020

import itertools

# Sample 2d array stacked top to bottom
a = ([1, 3, 6],[2, 2, 4],[8, 3, 1])

def diagonalDifference(arr):
    place_forward = 0                                               # Starting point  of forward descending diagonal (top left to lower right) 
    total_forward = 0                                               # Sum of values for the forward diagonal
    # Increment index by 1 for each group in 'a' to find the diagonal values
    for group in arr:
        total_forward = total_forward + group[place_forward]        # Sum the diagonal integers from top left
        place_forward += 1                                          # Move the index forward by 1
    
    #Set starting point for retrograde descending diagonal (top right to lower left). This is the last index.
    place_retro = len(arr) -1
    total_retro = 0                                                 # Sum of values for the retrograde diagonal
    for group in arr:
        total_retro = total_retro + group[place_retro]              # Sum the diagonal integers from top right
        place_retro -= 1                                            # Move the index back by 1
    
    # Calculate the absolute difference between the 2 diagonals
    difference = int(abs(total_forward - total_retro))
    return difference
print(diagonalDifference(a))