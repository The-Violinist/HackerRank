# Cut the sticks challenge
# Remove the value of the shortest stick from each stick then remove the shortest sticks(s)
# Return the number of sticks at each iteration
arr = [5, 4, 4, 2, 2, 8]

def cutTheSticks(arr):
    total = []
    while True:
        if len(arr) == 0:
            break
        i = 0
        smallest = min(arr)
        total.append(len(arr))
        while i < len(arr):
            if arr[i] >= smallest:
                # Subtract the shortest stick from each array item
                arr[i] = (arr[i] - smallest)
                i += 1
        # Remove all 0's
        while 0 in arr: arr.remove(0)
    return total
print(cutTheSticks(arr))