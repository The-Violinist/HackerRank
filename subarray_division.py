s = [1, 2, 1, 3, 2]
d = 3
m = 3
def birthday(s, d, m):
    correct = 0
    length = (len(s)-m)
    i = 0
    while i <= length:
        total = (sum(s[i:i+m]))
        i +=1
        if total == d:
            correct += 1
    return correct
birthday(s, d, m)