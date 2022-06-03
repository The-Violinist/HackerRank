import os

def ordinal(n):
    s = ('th', 'st', 'nd', 'rd') + ('th',)*10
    print(f"s = {s}")
    v = n%100
    if v > 13:
        print(f"v = {v%10}")
        return f'{n}{s[v%10]}'
    else:
        return f'{n}{s[v]}'

while True:
    number = (input())
    os.system("cls")
    if number == "":
        break
    else:
        number = int(number)
    print(ordinal(number))
