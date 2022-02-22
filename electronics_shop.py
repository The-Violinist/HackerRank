# Electrontics Shop
# https://www.hackerrank.com/challenges/electronics-shop
# Calculate the highest priced combo which can be purchased under "b" amount

b = 60                                              # Money available to spend
keyboards = [70,50,60]                              # Prices of keyboards
drives = [9,5,12]                                   # Prices of USB drives

def getMoneySpent(keyboards, drives, b):
    totals = []
    for keyboard in keyboards:                      # Loop through all combinations of keyboards and drives
        for drive in drives:
            totals.append(keyboard + drive)         # Append all possible combinations to the totals array
    totals.sort()                                   # Sort the array
    totals.reverse()                                # Reverse to descending order
    totals.append(-1)                               # Add a value that will be a catch all in the event that there are no other matching values
    while True:
        for item in totals:                         # Loop through the array and test totals against the dollar amount to spend
            if item > b:                            # Keep going if the item (combo from array) is greater than the amount to spend
                continue
            else:                                   # Return the item if it is <= the amount to spend
                return item                         # -1 will be returned if it is not possible to purchase any combination

print(getMoneySpent(keyboards, drives, b))