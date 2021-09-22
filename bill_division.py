bill = [3, 10, 2, 9]
k = 1
b = 9

def bonAppetit(bill, k, b):
    total = 0
    for item in bill:
        total += item
    anna_minus = total - bill[k]
    anna = anna_minus/2
    if anna == b:
        print("Bon Appetit")
    else:
        print(int(b-anna))

bonAppetit(bill, k, b)