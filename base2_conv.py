# Purpose: Convert a single octet in base 2 to decimal notation
# This is not a HackerRank challenge, but rather one that I created to help with octet conversion

### Libraries ###
import re

### Functions ###
def check(inp):                                         # Take user input and determine if it is the correct type of characters
    reg = re.compile('[0-1]')                           # Create a regular expression check. Only 1 and 0 are allowed
    for item in inp:                                    # Check each character against regex check
        a = bool(reg.match(item))                       # Assign a boolean value to 'a' based on match
        if a == True:                                   # All characters match the regex requirement
            continue
        elif a == False:                                # If a character is not in the allowed list, end the loop and return 0
            print(f"{item} is not a valid character in base 2.")
            return 0
    return 1                                            # Return 1 if all match the regex check

def convert():
    while True:
        octet = input("Please enter a base 2 octet:\n") # Take user input in the form of a base 2 octet
        if len(octet) == 8:                             # Check if the input is the correct number of characters
            correct = check(octet)                      # Run the RE check to make sure that the input contains only 1 and 0
            if correct == 1:                            # If all matches check out, go to the actual conversion
                break
            else:
                continue
        else:                                           # If there are not 8 characters, return to the top of the loop
            print("That is not the correct number of characters for an octet.")
    decimal_number = int(octet, base=2)                 # Take the sanitized input and convert base 2 to base 10
    print(f"{octet} in base 10 is {decimal_number}")

### Main ###
convert()
### End ###