#This finds the ratio of positive, negative, and zero numbers

arr = (1, 3, 0, -4, 3)
def plusMinus(arr):
    plus = 0
    minus = 0
    n = (len(arr))
    zero = abs(plus - minus)
    for i in arr:
        if (i > 0):
            plus += 1
        elif (i < 0):
            minus += 1
    formatted_plus = "{:.6f}".format(plus / n)
    formatted_minus = "{:.6f}".format(minus / n)
    formatted_zero = "{:.6f}".format((n - plus - minus) / n)
    print(f"{formatted_plus}\n{formatted_minus}\n{formatted_zero}")

plusMinus(arr)