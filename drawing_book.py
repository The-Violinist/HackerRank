# Drawing Book
# https://www.hackerrank.com/challenges/drawing-book
# Determine if a given page is fewer page turns from the front of the back of the book
# Page 1 is always on the right

n = 100                                                 # Total book length
p = 1                                                   # Page to turn to

def down(n, p):                                         # Calculate page turns from the back of the book
    even_odd = n % 2                                    # Determine if there are an even or odd number of pages
    countdown = 0
    if even_odd == 0:                                   # Run this loop if there are an even number of pages
        while True:
            for i in range((n),-1,-2):                  # Start at the end of the range (-1) and increment backwards by 2 pages at a time
                if i <= p:                              # Stop the loop once arriving at the page 
                    return countdown
                countdown += 1                          # Increment the counter for the number of turns
    elif even_odd == 1:                                 # Run this loop if there are an odd number of pages
        while True:
            for i in range(n,0,-2):                     # Start at the end of the range and increment backwards by 2 pages at a time
                if i == p or i == p + 1:                # Stop the loop once arriving at the page 
                    return countdown
                countdown += 1                          # Increment the counter for the number of turns

def up(n, p):                                           # Calculate page turns from the front of the book
    countup = 0
    while True:
        for i in range(0,n+1,2):                        # Start at the beginning of the range and increment upwards by 2 pages at a time
            if i >= p - 1:                              # Stop the loop once arriving at the page
                return countup
            countup += 1                                # Increment the counter for the number of turns

def pageCount(n, p):
    ups = up(n,p)                                       # Run the up function
    downs = down(n,p)                                   # Run the down function
    if ups <= downs:                                    # Determine which is fewer turns
        return ups
    else:
        return downs

print(pageCount(n,p))