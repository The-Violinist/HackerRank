#Hacker_rank: Electrontics Shop
#Calculate the highest combo which can be purchased under "b" amount

b = 60
keyboards = [70,50,60]
drives = [9,5,12]

def getMoneySpent(keyboards, drives, b):
    totals = []
    for keyboard in keyboards:
        for drive in drives:
            totals.append(keyboard + drive)
    print(totals)
    totals.sort()
    totals.reverse()
    print(totals)
    totals.append(-1)
    while True:
        for item in totals:
            print(item)
            if item > b:
                continue
            else:
                return item

x = getMoneySpent(keyboards, drives, b)
print(x)