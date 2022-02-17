# Jumping on the Clouds challenge
# Jump at interval k number of indexes
# Subtract 1 for each jump and an additional 2 if value is 1

c = [0,0,0,0,1,0]

def jumpingOnClouds(c):
    jumps = 0
    index = 0
    while index < (len(c) - 1):
        # Check to see if jumping 2 is safe
        if index == len(c) - 1:
            return jumps
        elif index == len(c) -2:
            return jumps + 1
        elif c[index + 2] == 0:
            index += 2
            jumps += 1
        # Otherwise jump 1
        else:
            index += 1
            jumps += 1
    return jumps
print(jumpingOnClouds(c))