p = [5,2,1,3,4]
def permutationEquation(p):
    y = []
    i = 1
    for item in p:
        index1 = p.index(i) + 1
        index2 = p.index(index1) + 1
        y.append(index2)
        i += 1
    return y
print(permutationEquation(p))