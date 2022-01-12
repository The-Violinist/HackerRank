import math

a = 24
b = 121

def squares(a, b):
    # Find the lower square root number
    start = int(math.sqrt(a))
    if start * start < a:
        start += 1
    # Find the upper square root number
    end = int(math.sqrt(b)) + 1
    if end * end > b:
        end -= 1
    # List to append all possible square roots
    num_list = []
    for num in range(start, end + 1):
        num_list.append(num)
    return num_list
x = squares(a, b)
print(f"There are {len(x)} numbers between (inclusive) {a} and {b} which have integers square roots.\nThe square roots are: ", end = "")
for item in x:
    print(f"{item}  ", end = "")