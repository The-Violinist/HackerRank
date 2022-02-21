# Bon Appetit
# https://www.hackerrank.com/challenges/bon-appetit
# Calculate the splitting of a bill between Anna and Brian
# Return 'Bon Appetit' if the split is fair. Otherwise, return the amount that Brian owes Anna

bill = [3, 10, 2, 9]                        # Cost of each item ordered
k = 1                                       # Index of items not eaten by Anna
b = 9                                       # Amount that Anna contributed

def bonAppetit(bill, k, b):
    total = 0
    for item in bill:                       # Sum the items ordered
        total += item
    anna_minus = total - bill[k]            # Subtract the items that Anna did not eat
    anna = anna_minus/2                     # Half of the shared bill items
    if anna == b:                           # If 'anna' == the amount that Anna paid, print 'Bon Appetit'
        print("Bon Appetit")
    else:                                   # Otherwise, print the amount that Brian owes Anna
        print(int(b-anna))

bonAppetit(bill, k, b)