# HackerRank Funny String
# https://www.hackerrank.com/challenges/funny-string/problem?h_r=internal-search
# Determines the absolute difference between adjacent list items and determines if the differences are the same forwards and backwards

# Sample string
s = "abc"

# Compare the absolute differences
def compare(string):
    comps = []
    len_char = len(string) - 1
    i = 0
    while i < len_char:                                     # Loop through and append the absolute differences of the values to a new list
        ii = i + 1                                          # i is the first index to consider and ii is the second
        comps.append(abs(string[i] - string[ii]))
        i += 1
    return comps

# Compare the ascii values to determine the numerical difference
def funnyString(s):
    forward = []
    for item in s:                                          # Create a list of ascii values
        forward.append(ord(item))
    for_comp = compare(forward)                             # Create variables for the forward and reverse lists
    forward.reverse()    
    rev_comp = compare(forward)
    if for_comp == rev_comp:                                # Compare lists
        return "Funny"
    else:
        return "Not Funny"
x = funnyString(s)
print(x)
