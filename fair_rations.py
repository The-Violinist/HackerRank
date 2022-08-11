# Fair Rations
# https://www.hackerrank.com/challenges/fair-rations/problem
# Determine how many loaves of bread need to be added to have all even values in the list
# When adding a loaf to one index, must also add to the index before and after as well

# B = [4,5,6,7]
B = [2,3,4,5,6]
def fairRations(B):
    forward = B.copy()                      # Copy the list for checking forwards calculations
    reversed = B.copy()                     # Copy list for backwards calculations then reverse
    reversed.reverse()
    i = 0
    counter1 = 0                            # Counter for the loaves given (forward)
    while i < len(forward) - 1:
        if forward[i] % 2 == 0:             # If the number is even, do nothing
            i += 1
            continue
        else:                               # If odd, add one to that index and the next index
            forward[i] += 1
            forward[i+1] += 1
            counter1 += 2
        i += 1
    if forward[-1] % 2 != 0:                # If it is not possible, return NO
        return "NO"

    i = 0
    counter2 = 0                            # Counter for the loaves given (reverse)
    while i < len(B) -1:                    ### Perform all the same steps on the reversed list
        if reversed[i] % 2 == 0:
            i += 1
            continue
        else:
            reversed[i] += 1
            reversed[i+1] += 1
            counter2 += 2
    i += 1
    if counter1 < counter2:                 # Determine which direction returns a lower number and return as a string
        return str(counter1)
    else:
        return str(counter2)
    
print(fairRations(B))