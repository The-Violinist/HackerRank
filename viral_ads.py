# 

n = 5

def viralAdvertising(n):
    # Starting day for the loop
    i = 1
    total = 2
    liked = 2
    # If there are 0 days
    if n == 0:
        return 0
    if n == 1:
        return 2
    # Days 2 - n
    while i < n:
        # Each person who likes the ad shares it
        shared = liked * 3
        # The number of recipients who like the ad are int(x/2)
        liked = int(shared/2)
        total += liked
        i += 1
    return total

print(viralAdvertising(n))