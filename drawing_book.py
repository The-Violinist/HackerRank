n = 100
p = 1

def down(n, p):
    even_odd = n % 2
    countdown = 0
    if even_odd == 0:
        while True:
            for i in range((n),-1,-2):
                if i <= p:
                    return countdown
                countdown += 1
    elif even_odd == 1:
        while True:
            for i in range(n,0,-2):
                if i <= p or i == p+1:
                    return countdown
                countdown += 1

def up(n, p):
    countup = 0
    while True:
        for i in range(0,n+1,2):
            if i >= p-1:
                return countup
            countup += 1

def pageCount(n, p):
    ups = up(n,p)
    downs = down(n,p)
    if ups <= downs:
        return ups
    else:
        return downs

print(pageCount(n,p))