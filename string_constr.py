# Hacker Rank String Construction challenge
# https://www.hackerrank.com/challenges/string-construction/problem
# Reconstruct the string as variable p. Each letter costs 1 point unless it is already present in p. Return the total cost to recreate.
s = "abab"

def stringConstruction(s):
    p = s[:1]                           # First letter
    counter = 1                         # Cost starts at 1 since p was empty to begin with
    i = 1                               # Index to reference
    while True:
        if s[i] in p:                   # If the next letter is in p, add it at no cost
            p = p + s[i]
        else:
            p = p + s[i]                # Else, add the letter and increment the cost counter
            counter += 1
        i += 1
        if i == len(s):                 # Break at the end of s
            break
    return counter
print(stringConstruction(s))
