###FUNCTIONS###
#Get a positive, non-zero number from the user
def get_number():
    while True:
        c0 = int(input("Please enter an integer:\n>>>"))
        if c0 > 0:
            return c0
        else:
            print("Please enter a positive, non-zero integer.")

#Run the Collatz formula
def collatz(c0):
    #Iterator for the collatz function
    i = 0
    #Loop until c0 == 1
    while True:
        if c0 == 1:
            break
        else:
            #Check if even
            if c0 % 2 == 0:
                c0 = c0 // 2
                print(c0)
            #Check if odd
            elif c0 % 2 == 1:
                c0 = 3 * c0 + 1
                print(c0)
        i += 1
    print(f"This took {i} iterations.")
### MAIN ###
user_number = get_number()
collatz(user_number)
###END###