# Modified Kaprekar Numbers
# https://www.hackerrank.com/challenges/kaprekar-numbers
# Finds numbers which when squared, split, then summed equal the starting number
# The squared number is split into l and r with r being d digits long
p = 100
q = 300
def kaprekarNumbers(p, q):
    kaprekars = []
    for num in range(p, q + 1):
        length = len(str(num))
        squared = num ** 2                                      # Find the square
        strung = str(squared)                                   # Turn the square into a string
        if len(strung) == 1:                                    # If the string is only 1 character long
            l = 0
            r = int(strung)
        elif len(strung) == 2:                                  # If the string is only 2 characters
            l = int(strung[0])
            r = int(strung[1])
        else:                                                   # Anything greater than 2 characters in length
            l = int(strung[0:-length])
            r = int(strung[-length:])
        if l + r == num:                                        # Add the left and right portions of the number together
            kaprekars.append(str(num))                          # If that equals the starting number, add to the list
    if kaprekars == []:                                         # If there are no matching numbers
        print("INVALID RANGE")
    else:                                                       # Otherwise, print the list
        kaprekars = " ".join(kaprekars)
        print(kaprekars)
kaprekarNumbers(p, q)