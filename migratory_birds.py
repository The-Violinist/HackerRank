# Calculates the number of instances of each number and returns the number which occurs the most
# If there is a tie, it returns the lower integer.

import collections

arr = [1, 1, 2, 2, 3]
arr1 = [1, 4, 4, 4, 5, 3]
arr2 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
def id_occurrence(arr):
    occurrences = collections.Counter(arr)
    highest_occurrence = 0
    item_id = 1000000
    for item in occurrences:
        this_occurrence = occurrences[item]
        if this_occurrence > highest_occurrence:
            highest_occurrence = this_occurrence
            item_id = item
        elif this_occurrence == highest_occurrence:
            if item < item_id:
                item_id = item
    return item_id

print(id_occurrence(arr))
print(id_occurrence(arr1))
print(id_occurrence(arr2))