a = [3,4]
b = [24, 48]

def chk_arr_a(x):
    for item in range(0, len(a)):
        if x%(a[item]) != 0:
            return 0
    return 1

def chk_arr_b(x):
    for item in range(0, len(b)):
        if (b[item])%x != 0:
            return 0
    return 1

def create_arrays(a, b, c):
    for x in range(a[c], (b[0] + 1)):
        res1 = chk_arr_a(x)
        if res1 == 1:
            y_array.append(x)
        res2 = chk_arr_b(x)
        if res2 == 1:
            z_array.append(x)

def getTotalX(a, b):
    last_a = (len(a) - 1)
    global y_array
    y_array = []
    global z_array
    z_array = []
    final = []
    create_arrays(a, b, last_a)
    for item in y_array:
        if item in z_array:
            final.append(item)
    print(f"{final} are factors of the 2 arrays.")
    return len(final)


print(getTotalX(a, b))
