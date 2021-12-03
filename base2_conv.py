### Libraries ###
import re
### Functions ###
# Take user input and determine if it is the correct type and number of characters
def check(inp): #'inp' becomes 'octet' in the next function
    # Create regular expression check
    reg=re.compile('[0-1]')
    for item in inp:
        #Assign a boolean value to 'a'
        a = bool(reg.match(item))
        if a == True:
            continue
        #if a character is not in the allowed list, end the loop and return 0
        elif a == False:
            print(f"{item} is not a valid character in base 2.")
            return 0
    #Return 1 if all is correct
    return 1
def convert():
    while True:
        #Take user input in the form of a base 2 octet
        octet = input("Please enter a base 2 octet:\n")
        #Check if the input is the correct number of characters
        if len(octet) == 8: #'octet' replaces 'inp' as the function argument
            #Run the RE check to make sure that the input contains only 1 and 0
            correct = check(octet)
            if correct == 1:
                break
                #Go to the actual conversion
            else:
                continue
        else:
            #If there are not 8 characters, return to the top of the loop
            print("That is not the correct number of characters for an octet.")
    #Take the sanitized input and convert base 2 to base 10
    decimal_number = int(octet, base=2)
    print(f"{octet} in base 10 is {decimal_number}")
### Main ###
convert()
### End ###