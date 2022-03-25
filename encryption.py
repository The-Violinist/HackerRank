# Hacker Rank: Encryption
# https://www.hackerrank.com/challenges/encryption
# This challenge takes a string, removes the spaces, then turns it into a square (or as close to a square as possible) of columns and rows.

import re
# s = "if man was meant to stay on the ground god would have given us roots"
# s = "chillout"
# s = "have a nice day"
# s = "feed the dog"
s = "iuo"
def encryption(s):

    spaceless = s.replace(" ", "")                                              # Remove all spaces
    length = len(spaceless)                                                     # Length of the string without spaces
    size = length ** 0.5                                                        # Square root of the length of the spaceless string
    floor = int(size)                                                           # Integer of the square root
    rows = []                                                                   # Array for the new words as rows
    encrypted = []                                                              # Array for the encrypted words
    if size == floor:                                                           # If size is a perfect square, then that equals the floor
        column = floor                                                          
    else:                                                                       # Otherwise round the number of colums up
        column = floor + 1
    start = 0                                                                   # Where to start creating the rows
    end = column                                                                # Where to end the first row
    while end <= length - 1:                                                    # Append words to the array until there are not enough characters for whole rows
        rows.append(spaceless[start:end])                                       # Add letters as joined strings in the lenght of the column variable
        start += column                                                         # Increment the starting point by the lenght of the row
        end += column                                                           # Increment the ending point by the lenght of the row
    if start <= length - 1:                                                     # Add any leftover letters as the last row
        rows.append(spaceless[start:])
    while len(rows[0]) > 0:
        print(len(rows[0]))
        word = []                                                               # Array to create each encrypted word
        i = 0                                                                   # Iterator for the 
        for item in rows:                                                       # Loop thru each word in the rows array
            if item == "":                                                      # If the item is empty, continue
                continue
            word.append(item[0])                                                # Add the first letter of each word to the word array
            rows[i] = item[1:]                                                  # Replace the item with the first letter removed
            i += 1                                                              # Increment to the next word in the array
        encrypted.append("".join(word))                                         # Add the combined letters for the encrypted word to the final array
    return " ".join(encrypted)
print(encryption(s))