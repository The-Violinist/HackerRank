n = 3 #prisoners
m = 7 #candies
s = 3 #starting
# n = 4
# m = 8
# s = 2
def saveThePrisoner(n, m, s):
    prisoners = n
    candies = m
    starting = s
    if candies + starting <= prisoners + 1:
        return candies + starting - 1
    else:
        # Remove candies from round 1 (possibly partial round of prisoners)
        candies -= (prisoners - starting + 1)
        if candies <= prisoners:
            return candies
        # Find the remainder after dividing candies by prisoners
        elif candies > prisoners:
            candies = candies % prisoners
        # if there is no remainder, that means the last prisoner gets the last piece of candy
        if candies == 0:
            candies = prisoners
    return candies
print(saveThePrisoner(n, m, s))