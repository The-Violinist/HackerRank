# Migratory Birds
# https://www.hackerrank.com/challenges/migratory-birds

# Calculates the number of instances of each number and returns the number which occurs the most
# If there is a tie, it returns the lower object value.

import collections

arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]                     # Sample array
def migratoryBirds(arr):
    occurrences = collections.Counter(arr)                  # Create a library of k,v (object value, occurences) pairs
    highest_occurrence = 0                                  # Variable to track the greatest number of occurences
    for item in occurrences:
        this_occurrence = occurrences[item]                 # The number of occurences for this item
        if this_occurrence > highest_occurrence:            # If the occurences of this item are greater than the previous greatest occurence:
            highest_occurrence = this_occurrence            # Set highest occurence to this occurence
            item_id = item                                  # Set the item_id to the value of the highest occurence object
        elif this_occurrence == highest_occurrence:         # If the occurences are the same, change the object value to the lower of the values
            if item < item_id:
                item_id = item
    return item_id

print(migratoryBirds(arr))
