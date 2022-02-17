###*******Work in progress*******
# s = [1,7,2,4]
s = [278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]
k = 7


def nonDivisibleSubset(k, s):
    mod_list = [i % k for i in s]
    mod_list = list(mod_list)
    print(mod_list)
    count = 0
    while mod_list:
        num = mod_list.pop()
        print(num)
        diff = k - num
        print(diff)
        if diff not in mod_list:
            count += 1
            print(f"The total is {count}")
    return count
print(nonDivisibleSubset(k, s))