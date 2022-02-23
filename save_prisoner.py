# Save the Prisoner
# https://www.hackerrank.com/challenges/save-the-prisoner
# Iterate around a group of prisoners passing out candy and find who will receive the last piece

from math import remainder


n = 3                                                   # Number of prisoners
m = 7                                                   # Number of candies
s = 3                                                   # Starting prisoner number for distributing candy

def saveThePrisoner(n, m, s):
    prisoners = n                                       # Reassign variables to be user friendly
    candies = m
    starting = s
    if candies + starting <= prisoners + 1:             # Determine if the candies will be distributed before getting to the end of the prisoner list once
        return candies + starting - 1
    else:
        candies -= (prisoners - starting + 1)           # Hand out candies to the end of the prisoner count for round 1
        if candies <= prisoners:                        # If there are not enough to do at least another full round, the last prisoner to get candy is 'candies'
            return candies
        elif candies > prisoners:                       # Find the remainder after dividing candies by prisoners
            remainder = candies % prisoners
            if remainder == 0:                          # If the remainder is 0, the last prisoner got the last piece
                return prisoners
            else:                                       # Otherwise, the remainder == the prisoner who gets the last piece
                return remainder

print(saveThePrisoner(n, m, s))