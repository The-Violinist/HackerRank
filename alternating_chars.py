# HackerRank Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem
# find the minimum number of deletions to create alternating characters in a string

# the string in question
s = "ABBABA"

def alternatingCharacters(s):
    counter = 0                                 # Number of letters that don't need to be changed
    ltr = "!"                                   # A random starting letter
    for letter in s:                            # Loop thru the string
        if letter != ltr:
            counter += 1                        # Increment the counter if the letter is different than the previous letter
            ltr = letter                        # Change the ltr variable to the current letter
    return len(s) - counter                     # Subtract the number of characters that do not need to be changed from the total length of the string

answer = alternatingCharacters(s)
print(answer)