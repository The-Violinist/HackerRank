# Sales by Match
# https://www.hackerrank.com/challenges/sock-merchant
# Matching pairs of socks and totaling the number of pairs

n = 9                                                           # Length of the array
ar = [1,1,3,1,2,1,3,3,3]                                        # Individual socks

def find_pairs(n, ar):
    x = ar[0]                                                   # Sample number
    for item in range(1, n):                                    # Test objects in array to match the sample
        if ar[item] == x:                                       # If a match exists, remove the sample and the test object from the array and return a match
            del ar[item]
            del ar[0]
            return 1
        elif x not in ar[1:]:                                   # If there is no match remove the sample object and return no match
            del ar[0]
            return 0

def checkIfDuplicates(listOfElems):                             # Check if there are any duplicates
    if len(listOfElems) == len(set(listOfElems)):               # Run a generic check to see if there are any matches at all
        return False
    else:
        return True

def sockMerchant(n, ar):
    total_pairs = 0
    while True:
        if n == 0:                                              # If the array is empty, return no pairs
            return total_pairs
        else:                                                   # If there are items in the array, continue
            result = checkIfDuplicates(ar)                      # Check if there are any duplicates at all
            if result == True:                                  # If so, call the find_pairs function to calculate the number of pairs
                total_pairs += find_pairs(n,ar)
            else:                                               # If not, return no pairs
                return total_pairs

print(sockMerchant(n, ar))
