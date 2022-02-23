# Calculate library fines based on the following rates:
# 1 day = 15
# 1 month = 500
# 1 year = 10000
# Fines are given as the highest of the 3 rates and not an accumulation

# Return date:
d1 = 2
m1 = 7
y1 = 2014
# Due date:
d2 = 1
m2 = 1
y2 = 2015

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Calculate differences
    d_diff = d1 - d2
    m_diff = m1 - m2
    y_diff = y1 - y2
    if y_diff < 0:                                      # If the book was return in a previous year
        return 0                                        # No fine
    elif y_diff > 0:                                    # If the book was returned in a later year
        return 10000 * y_diff                           # Return late years multiplied by rate
    elif m_diff > 0:                                    # If the book was returned in a later month
        return 500 * m_diff                             # Return late months multiplied by rate
    elif d_diff > 0 and m_diff == 0:                    # If the book was returned in the same month on a later date
        return 15 * d_diff                              # Return late days multiplied by rate
    else:                                               # All other early returns
        return 0                                        # No fine
        
print(libraryFine(d1, m1, y1, d2, m2, y2))