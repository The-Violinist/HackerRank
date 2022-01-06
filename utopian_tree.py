# Calculate the height of a tree which grows and an alternating rate of doubling and adding 1

# Cycles
n = 5
def utopianTree(n):
    i = 0
    # Starting height
    height = 1
    # If there are no growing seasons
    if n == 0:
        return height
    while i < n:
        # Spring season growth
        if i % 2 == 0:
            height *= 2
            i += 1
        # Summer season growth
        else:
            height += 1
            i += 1
    return height

print(utopianTree(n))