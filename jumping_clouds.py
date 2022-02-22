# Jumping on the Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds

# Character can jump 1 or 2 clouds at a time but cannot land on a 1
# Calculate the fewest number of jumps
c = [0,0,0,0,1,0]

def jumpingOnClouds(c):
    jumps = 0
    index = 0
    while index <= (len(c) - 1):                        # Loop through 'c' until getting to the end of the array
        if index == len(c) - 1:                         # End the loop if on the last index
            return jumps                                # return the total number of jumps
        elif index == len(c) -2:                        # End the loop if on the 2nd to last index
            return jumps + 1                            # Move the index forward to the last index (which must be a value of 0), and return jumps + 1
        elif c[index + 2] == 0:                         # Jump 2 if the landing value is 0
            index += 2                                  # Move the index forward 2
            jumps += 1                                  # Increment the number of jumps by 1
        else:                                           # Otherwise, jump 1
            index += 1                                  # Move the index forward 1
            jumps += 1                                  # Increment the number of jumps by 1
    return jumps                                        # Return jumps if the index has gone out of the given range 
print(jumpingOnClouds(c))