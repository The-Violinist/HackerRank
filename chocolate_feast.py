# Total bars that can be eaten with initial money and total wrappers to redeem

# Money to spend
n = 15
# Cost per bar
c = 3
# Wrappers to get another bar
m = 2

def chocolateFeast(n, c, m):
    # Initial number of chocolate bars which can be eaten
    eaten = int(n / c)
    # Wrappers left
    wrappers = int(n / c)
    while True:
        if wrappers < m:
            return eaten
        # Number of bars which can be redeemed with wrappers
        new_bars = int(wrappers / m)
        eaten += new_bars
        # Wrappers left over at redemption
        wrappers = (wrappers % m) + new_bars

print(chocolateFeast(n,c,m))