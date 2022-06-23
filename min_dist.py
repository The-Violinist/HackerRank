# Minimum Distances
# https://www.hackerrank.com/challenges/minimum-distances
# Find the pair of identical numbers which are closest together and return the difference in the indeces
import collections

a = [7, 1, 3, 4, 1, 7]

''' Using enumerate()
def minimumDistances(a):
    numbers = set(a)
    for item in numbers:
        indices = [i for i, x in enumerate(a) if x == item]
        return indices
'''
def minimumDistances(a):
    dist = 10000
    list_dict = collections.Counter(a)
    repeats = [i for i in list_dict if list_dict[i]>1]
    if repeats == []:
        return -1
    for item in repeats:
        indices = []
        ind = 0
        for num in a:
            if num == item:
                indices.append(ind)
            ind += 1
        if indices[1] - indices[0] < dist:
            dist = indices[1] - indices[0]
    return dist


print(minimumDistances(a))