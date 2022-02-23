###FUNCTIONS###
#Get a positive, non-zero number from the user
def get_number():
    while True:
        c0 = int(input("Please enter an integer:\n>>>"))
        if c0 > 0:                                                  # Check to sanitize the input
            return c0
        else:
            print("Please enter a positive, non-zero integer.")     # If no a positive number, repeat the request for input

def collatz():
    c0 = get_number()                                               # Get a number from the user
    i = 0                                                           # Iterator for the collatz function
    while True:                                                     # Loop until c0 == 1
        if c0 == 1:
            break
        else:
            if c0 % 2 == 0:                                         # Check if c0 is even
                c0 = c0 // 2                                        # If so, divide by 2
            else:                                                   # If the number is odd
                c0 = 3 * c0 + 1                                     # Multiply the number by 2 and add 1
        i += 1                                                      # Increment the counter for the number of iterations
    print(f"This took {i} iterations.")

### MAIN ###
collatz()
###END###