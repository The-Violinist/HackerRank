# Taum and B'day
# https://www.hackerrank.com/challenges/taum-and-bday
# Calculate the total cost to by b*bc gifts and w*wc gifts
# Gifts of one color can be converted to the other at the cost of z
# Return the least cost

b = 3                                           # Number of black gifts
w = 5                                           # Number of white gifts
bc = 3                                          # Cost for black gifts
wc = 4                                          # Cost for white gifts
z = 1                                           # Conversion price

def taumBday(b, w, bc, wc, z):
    white_total = w*wc                          # Total cost of buying white gifts
    black_total = b*bc                          # Total cost of buying black gifts
    w_to_b = (b*wc) + (z*b)                     # Total cost of purchasing white gifts and converting to black
    b_to_w = (w*bc) + (z*w)                     # Total cost of purchasing clack gifts and converting to white
    if w_to_b < black_total:                    # Determine if white to black conversion is cheaper
        black_total = w_to_b
    if b_to_w < white_total:                    # Determine if black to white conversion is cheaper
        white_total = b_to_w
    lowest_price = black_total + white_total
    return lowest_price                         # Return the lowest cost

print(taumBday(b, w, bc, wc, z))

