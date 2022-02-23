# Number Line Jumps
# https://www.hackerrank.com/challenges/kangaroo

# 2 Kangaroos start at different positions and jump at different rates
# Return "Yes" if they can arrive at the same location or "No" if not

x1 = 0                                                          # Kangaroo 1 start position
v1 = 2                                                          # Kangaroo 1 jump distance
x2 = 5                                                          # Kangaroo 2 start position
v2 = 3                                                          # Kangaroo 2 jump distance

def kangaroo(x1, v1, x2, v2):
    if x1 == x2:                                                # If the starting location is the same return "Yes"
        return "YES"
    else:                                                       # If the starting locations are different, continue
        if x1 > x2 and v1 < v2:                                 # Run this loop if Kangaroo 1 is further forward and kangaroo 2 has the ability to catch up
            while True:
                if x2 > x1:                                     # If Kangaroo 2 passes 1, return "No"
                    return "NO"
                elif x1 == x2:                                  # If they land at the same spot, return "Yes"
                    return "YES"
                else:                                           # Kangaroos jump their respective distances
                    x1 += v1
                    x2 += v2
        elif x2 > x1 and v2 < v1:                               # Run this loop if Kangaroo 2 is further forward and kangaroo 1 has the ability to catch up
            while True:
                if x1 > x2:                                     # If Kangaroo 1 passes 2, return "No"
                    return "NO"
                elif x1 == x2:                                  # If they land at the same spot, return "Yes"
                    return "YES"
                else:                                           # Kangaroos jump their respective distances
                    x1 += v1
                    x2 += v2
        else:
            return "NO"                                         # If it is not possible for 1 or 2 to catch up, return "No"
print(kangaroo(x1,v1,x2,v2))
