# Divisible Sum Pairs
# https://www.hackerrank.com/challenges/divisible-sum-pairs
# Add all pair combinations from ar and return the number of pairs divisible by k
ar = [1, 3, 2, 6, 1, 2]
n = 6
k = 3
def divisibleSumPairs(n, k, ar):
    arr_len = (len(ar)-1)                           # Index for the lenght of the array
    i1 = 0                                          # Index to use for first number when calculating the sum
    matches = 0                                     # Counter for pairs that match

    while i1 < arr_len:
        i2 = i1+1                                   # Initiate i2 to be one index greater than i1
        while i2 < len(ar):                         # Loop until i2 gets to the end of the array
            sum_total = (ar[i1] + ar[i2])           # Sum all possible pairs of objects in the array
            if sum_total % k == 0:                  # If sum_total is evenly divisible by k, increment matches by 1
                matches += 1
            i2 += 1                                 # Increment the 2nd number of the pair until the end of the array
        i1 += 1                                     # Increment the first number for the next iteration of the loop
    return matches

print(divisibleSumPairs(n, k, ar))