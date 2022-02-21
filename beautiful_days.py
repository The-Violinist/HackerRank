# Beautiful Days at the Movies
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

# Calculate the number of days in range(i,j) which, when subtracting the reverse of the number is divisible by k
import math
i = 20
j = 23
k = 6
def beautifulDays(i, j, k):
    total = 0
    for num in range(i,j+1):                    # Create a list of the digits in each number in the range
        li = [x for x in str(num)]              # Convert the integers to strings in order to join them
        li.reverse()                            # Reverse the order of the list
        rev_num = int(''.join(li))              # Join all items from the reversed list and convert the joined string to an integer
        if (num - rev_num) % k == 0:            # If the result of the number minus its reverse is divisible by k, increment the total by 1
            total += 1
    return total

print(beautifulDays(i,j,k))