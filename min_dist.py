# Minimum Distances
# https://www.hackerrank.com/challenges/minimum-distances
# Find the pair of identical numbers which are closest together and return the difference in the indeces

a = [7, 1, 3, 4, 1, 7]
def minimumDistances(a):
    numbers = set(a)
    for item in numbers:
        indices = [i for i, x in enumerate(a) if x == item]
        print(indices)
minimumDistances(a)