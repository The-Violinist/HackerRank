# Hurdle Race
# https://www.hackerrank.com/challenges/the-hurdle-race
# Find the additional height over k that is needed for highest hurdle

height = [1,6,3,5,2]                        # Hurdle heights
k = 4                                       # Character's max jumping ability

def hurdleRace(k, height):
    potions = 0
    highest = max(height)                   # Highest hurdle
    if highest > k:                         # If the highest hurdle is greater than the jumping ability
        potions += highest - k              # Set potions to be the difference between highest hurdle and the jumping ability 
    return potions                          # Returns 0 if no potion is needed or the difference between the highest hurdle and k if highest is greater

print(hurdleRace(k, height))