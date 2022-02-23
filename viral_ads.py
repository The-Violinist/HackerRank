# Viral Advertising
# https://www.hackerrank.com/challenges/strange-advertising
# Determine how many people will have liked an ad after n days
# Advertisements are shared with 5 people on day 1 and floor(5/2) like the ad. The resluting likes (2) share the ad with 3 friends each.
# This same pattern occurs each day until 'n'

n = 5

def viralAdvertising(n):
    total = 0                                   # Initial total likes
    shared = 5                                  # Initial shares
    if n == 0:                                  # If there are 0 days return 0
        return 0
    for day in range(n):                        # Loop through days until n
        liked = int(shared/2)                   # The number of recipients who like the ad
        shared = liked * 3                      # Each person who likes the ad shares it with 3 friends
        total += liked                          # Add 'liked' to the total number of likes
    return total

print(viralAdvertising(n))