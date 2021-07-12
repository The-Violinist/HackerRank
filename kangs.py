x1 = 0
v1 = 3
x2 = 4
v2 = 1

def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        result = "YES"
        return result
    else:
        if x1 > x2:
            diff1 = x1 - x2
            while True:
                if x2 > x1:
                    result = "NO"
                    return result
                    break
                elif x1 == x2:
                    result = "YES"
                    return result
                    break
                else:
                    x1 += v1
                    x2 += v2
                    diff2 = x1 - x2
                    if diff2 > diff1 or diff1 == diff2:
                        result = "NO"
                        return result
                        break
        else:
            diff1 = x2 - x1
            while True:
                if x1 > x2:
                    result = "NO"
                    return result
                    break
                elif x1 == x2:
                    result = "YES"
                    return result
                    break
                else:
                    x1 += v1
                    x2 += v2
                    diff2 = x2 - x1
                    if diff2 > diff1 or diff1 == diff2:
                        result = "NO"
                        return result
                        break

print(kangaroo(x1,v1,x2,v2))
