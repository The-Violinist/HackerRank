# HackerRank Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem
# Make the fewest changes possible to have no instances of 010

b = "0101010"

def beautifulBinaryString(b):
    str_lst = []
    for item in b:                                          # Create a list of the numbers in the string
        str_lst.append(item)
    i = 0
    counter = 0
    while i < len(str_lst) - 2:                             # Loop through the string up to 2 indices before the end of the string
        if (str_lst[i:i+3]) == ['0', '1', '0']:             # Check for instances of the series 010
            str_lst[i + 2] = '1'                            # If present, change the 3rd number to 1
            counter += 1                                    # Increment the number of changes made
        i += 1
    return counter
print(beautifulBinaryString(b))