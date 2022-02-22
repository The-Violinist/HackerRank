# Chocolate Feast
# https://www.hackerrank.com/challenges/chocolate-feast
# A store has a promotion on chocolate; customers can redeem wrappers for more chocolate
# Find total bars that can be eaten based on an initial amount of money and total wrappers redeemed

n = 15                                              # Money to spend
c = 3                                               # Cost per bar
m = 2                                               # Wrappers needed to redeem a bar

def chocolateFeast(n, c, m):
    eaten = int(n / c)                              # Initial number of chocolate bars which can be eaten
    wrappers = int(n / c)                           # Wrappers left
    while True:                                     # Keep redeeming wrappers to get more bars
        if wrappers < m:
            return eaten                            # Stop loop if there are not enough wrappers to redeem
        new_bars = int(wrappers / m)                # Number of bars which can be redeemed with wrappers
        eaten += new_bars                           # Add to total bars eaten
        wrappers = (wrappers % m) + new_bars        # Wrappers left over at redemption

print(chocolateFeast(n,c,m))