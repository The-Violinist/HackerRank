# Based on the length of a number, include only 5s and 3s to create the largest number based on:
    # 5s must be in multiples of 3
    # 3s must bne in multiples of 5
    # if not possible, return -1

def decentNumber(n):
    num = -1
    # If possible to have only 5s
    if n % 3 == 0:
        return int("5" * n)

    # Find possible 5/3 combo
    else:
        fives = n
        while fives > 3:
            fives -= 5
            if fives % 3 == 0:
                threes = "3" * (n - fives)
                fives = "5" * fives
                return int(fives+threes)
    
    # If possible to have only 3s            
    if n % 5 == 0:
        return int("3" * n)
    return num

li = [1,3,5,11]
for item in li:
    print(decentNumber(item))