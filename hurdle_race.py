# Find the additional height over k that is needed for highest hurdle

# Hurdle heights
height = [1,6,3,5,2]
# Character's max jump height
k = 4

def hurdleRace(k, height):
    potions = 0
    # Highest hurdle
    highest = max(height)
    if highest > k:
        # Find difference between highest hurdle and 
        potions += highest - k
    return potions

print(hurdleRace(k, height))