# Utopian Tree
# https://www.hackerrank.com/challenges/utopian-tree
# Calculate the height of a tree which grows and an alternating rate of doubling (spring) and adding 1 (summer)

n = 5                                           # Number of growth cycles

def utopianTree(n):
    i = 0                                       # Growing season iterator
    height = 1                                  # Starting height
    if n == 0:                                  # If there are no growing seasons
        return height
    while i < n:                                # Loop through growth cycles
        if i % 2 == 0:                          # Spring season growth
            height *= 2                         # Double height
            i += 1
        else:                                   # Summer season growth
            height += 1                         # Increment height by 1
            i += 1
    return height

print(utopianTree(n))