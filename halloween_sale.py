# Halloween sale
# https://www.hackerrank.com/challenges/halloween-sale
# Determine how many games can be purchased for 's' dollars, starting at 'p' dollars, incrementing down by 'd' dollars to a minimum of 'm' dollars
# Return the number of games which can be purchased

p = 20
d = 3
m = 6
s = 80

def howManyGames(p, d, m, s):
    counter = 0
    if s < p:
        return counter                  # Return 0 if there is not enough money for 1 game
    while s > 0:
        s = s - p                       # Subtract the cost of a game from s
        if p - d <= m:                  # If the downward incrementing number will bring the cost to the minimum, set p to the minimum
            p = m
        else:
            p = p - d                   # Otherwise, reduce the cost by d
        counter += 1                    # Count this purchase
        if s < p:                       # If the money left is less than the cost of the next game, stop the loop
            break
    return counter                      # Return the final count
print(howManyGames(p, d, m, s))