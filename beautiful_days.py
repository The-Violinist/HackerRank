# Calculate the number of days in range(i,j) which, when subtracting the revers of the number is divisible by k
import math
i = 20
j = 23
k = 6
def beautifulDays(i, j, k):
    total = 0
    for num in range(i,j+1):
        # Create a list of the digits in the number
        li = [x for x in str(num)]
        li.reverse()
        # Join all items from the reversed list
        rev_num = int(''.join(li))
        if (num - rev_num) % k == 0:
            total += 1
    return total

print(beautifulDays(i,j,k))