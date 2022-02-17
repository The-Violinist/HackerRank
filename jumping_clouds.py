# Jumping on the Clouds challenge
# Jump at interval k number of indexes
# Subtract 1 for each jump and an additional 2 if value is 1

'''
c = [0,0,1,0,0,1,1,0]
k = 2
'''
c = [1,1,1,0,1,1,0,0,0,0]
k = 3

def jumpingOnClouds(c, k):
    cloud = 0
    energy = 100
    while cloud < len(c):
        if c[cloud] == 1:
            energy -= 2
        cloud += k
        energy -= 1
    return energy

print(jumpingOnClouds(c, k))