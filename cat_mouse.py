# Hacker Rank: Cats and a Mouse
# https://www.hackerrank.com/challenges/cats-and-a-mouse
# Calculate which cat (x,y) will reach the mouse (z) first.
# The cat's move at the same rate and the mouse is stationary

x = 2                                       # Cat A starting position
y = 5                                       # Cat B starting position
z = 4                                       # Mouse's position

def calc_cat(cat, mouse):
    i = 0
    if cat < mouse:                         # Determine if the cat needs to increase it's position
        while cat < mouse:
            cat += 1                        # Move the cat's position forward by one place until reaching the mouse
            i += 1
    elif cat > mouse:                       # Determine if the cat needs to decrease it's position
        while cat > mouse:
            cat -=1                         # Move the cat's position back by one place until reaching the mouse
            i +=1
    return i

def catAndMouse(x, y, z):
    cat_a = calc_cat(x, z)                  # The number of moves it takes for cat A to reach the mouse
    cat_b = calc_cat(y, z)                  # The number of moves it takes for cat B to reach the mouse
    if cat_a < cat_b:                       # Return which cat arrives first. If it is a tie, the mouse wins
        return "Cat A"
    elif cat_a > cat_b:
        return "Cat B"
    else:
        return "Mouse C"

print(catAndMouse(x, y, z))