# Sherlock and the Beast
# https://www.hackerrank.com/challenges/sherlock-and-the-beast

# Based on the length of a number, include only 5s and 3s to create the largest number possible based on:
    # 5s must be in multiples of 3
    # 3s must bne in multiples of 5
    # if not possible, return -1

def decentNumber(n):
    if n % 3 == 0:                                  # Determine if it is possible to have only 5's
        return int("5" * n)
    else:                                           # Determine if it is possible to have a 5/3 combination
        fives = n
        while fives > 3:                            # Perform the loop until it returns or is determined not possible
            fives -= 5                              # Subtract groups of 5 for 3's
            if fives % 3 == 0:                      # If the rest can be divided by 3, return the highest possible value
                threes = "3" * (n - fives)          # Total 3's
                fives = "5" * fives                 # Total 5's
                return int(fives+threes)            # Append the groups of 3's and 5's then convert to an integer
               
    if n % 5 == 0:                                  # If possible to have only 3s 
        return int("3" * n)
    return -1                                       # If no combination is possible, return -1


# Test a few numbers to check desired outcome
li = [1,3,5,11]
for item in li:
    print(decentNumber(item))