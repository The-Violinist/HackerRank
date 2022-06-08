s = "abc"
def compare(string):
    comps = []
    len_char = len(string) - 1
    i = 0
    while i < len_char:
        ii = i + 1
        comps.append(abs(string[i] - string[ii]))
        i += 1
    return comps
def funnyString(s):
    forward = []
    for item in s:
        forward.append(ord(item))
    for_comp = compare(forward)
    forward.reverse()    
    rev_comp = compare(forward)
    if for_comp == rev_comp:
        return "Funny"
    else:
        return "Not Funny"
x = funnyString(s)
print(x)
