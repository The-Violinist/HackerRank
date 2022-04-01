# Beautiful Triplets
# https://www.hackerrank.com/challenges/beautiful-triplets
# Finds all possible combinations where 3 items in the array fulfill the following:
    # b-a=c-b=d


d = 3
arr = [1, 2, 4, 5, 7, 8, 10]
def beautifulTriplets(d, arr):
    arr.reverse()
    i = 0
    beautifuls = 0
    if len(arr) < 3:                                    # If the array length is less than d, return no matches
        return 0
    while i < len(arr) - 2:                             # Loop thru using index i as the starting index
        ii = i + 1
        while ii < len(arr) - 1:                        # Loop thru using i + 1 as the starting index for matches
            if arr[i] - arr[ii] == d:                   # If index ii - i == d, run next loop
                iii = ii + 1
                while iii < len(arr):                   # Loop third index
                    if arr[ii] - arr[iii] == d:         # Once both conditions are met, increment the beautifuls variable by 1
                        beautifuls += 1
                    if arr[ii] - arr[iii] > d:          # Stop the loop once the difference is greater than d
                        break
                    iii += 1
            if arr[i] - arr[ii] > d:                    # Stop the loop once the difference is greater than d
                break
            ii += 1
        i += 1
    return beautifuls
print(beautifulTriplets(d, arr))