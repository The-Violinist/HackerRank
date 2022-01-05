# Calculate library fines based on the following rate
# 1 day = 15
# 1 month = 500
# 1 year = 10000

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
    # If the book was return in a previous year
    if y_diff < 0:
        return 0
    # If the book was returned in a later year
    elif y_diff > 0:
        return 10000 * y_diff
    # If the book was returned in a later month
    elif m_diff > 0:
        return 500 * m_diff
    # If the book was returned in the same month on a later date
    elif d_diff > 0 and m_diff == 0:
        return 15 * d_diff
    # All other early returns
    else:
        return 0
        
print(libraryFine(d1, m1, y1, d2, m2, y2))