#Hacker Rank: Cat and Mouse
#Calculate which cat (x,y) will reach the mouse (z) first.

x = 2
y = 5
z = 4

def calc_cat(cat, mouse):
    i = 0
    if cat < mouse:
        while cat < mouse:
            cat += 1
            i += 1
    elif cat > mouse:
        while cat > mouse:
            cat -=1
            i +=1
    return i

def catAndMouse(x, y, z):
    cat_a = calc_cat(x, z)
    cat_b = calc_cat(y, z)
    if cat_a < cat_b:
        return "Cat A"
    elif cat_a > cat_b:
        return "Cat B"
    else:
        return "Mouse C"

print(catAndMouse(x, y, z))