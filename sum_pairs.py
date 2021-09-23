# Add all pair combinations from ar and return the number of pairs divisible by k
ar = [1, 3, 2, 6, 1, 2]
n = 6
k = 3
def divisibleSumPairs(n, k, ar):
    arr_len = (len(ar)-1)
    i1 = 0
    matches = 0

    while i1 < arr_len:
        i2 = i1+1
        while i2 < len(ar):
            sum_total = (ar[i1] + ar[i2])
            if sum_total%k == 0:
                matches += 1
            i2 += 1
        i1 += 1
    print(matches)
    # return matches

divisibleSumPairs(n, k, ar)