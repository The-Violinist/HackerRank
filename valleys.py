# Counting Valleys
# https://www.hackerrank.com/challenges/counting-valleys
# A valley is constituted as any point below the starting point, even if there are sub valleys within that.
# This function tracks how many times the starting level is crossed from being below it

steps = 8                                           # Number of total steps
path = "UDDDUDUU"                                   # Ups and Downs as a string
def countingValleys(steps, path):
    level = 0                                       # Starting level
    total_count = 0                                 # Counter for number of valleys starting and ending at 'level'
    for item in path:
        if item == "U":                             # Increment 'level' up
            level += 1
            if level == 0:                          # If 'level' == 0 when going up, increment total_count
                total_count += 1
        elif item == "D":                           # Increment 'level' down
            level -= 1
    return total_count                              # Return total valleys starting and ending at 0
print(countingValleys(steps, path))