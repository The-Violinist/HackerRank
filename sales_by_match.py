#HackerRank: Sales by Match
#Matching pairs and totaling the number of pairs

#Required variable, which I didn't use. I checked the length each iteration instead
n = 10

#Test data
#ar = [10,20,20,10,10,30,50,10,20,11]
# ar = [1,1,3,1,2,1,3,3,3,3]
ar = [1,1,3,1,2,1,3,3,3]

def find_pairs(n, ar):
    #test number
    x = ar[0]
    for item in range(1,(len(ar))):
        if ar[item] == x:
            del ar[item]
            del ar[0]
            return 1
        elif x not in ar[1:]:
            del ar[0]
            return 0

#Check if there are any duplicates
def checkIfDuplicates(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def sockMerchant(n, ar):
    total_pairs = 0
    while True:
        if len(ar) == 0:
            break
        elif len(ar) > 1:
            result = checkIfDuplicates(ar)
            if result == True:
                total_pairs += find_pairs(len(ar),ar)
            else:
                break
        else:
            break
    return total_pairs

print(sockMerchant(n, ar))
