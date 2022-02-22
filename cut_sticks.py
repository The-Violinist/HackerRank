# Cut the sticks
# https://www.hackerrank.com/challenges/cut-the-sticks
# Remove the value of the shortest stick from each stick (list item) then remove the shortest sticks(s)
# Return the number of sticks at each iteration
arr = [5, 4, 4, 2, 2, 8]

def cutTheSticks(arr):
    total = []
    while True:
        if len(arr) == 0:                                   # If there are no items in the array, break
            break
        i = 0
        smallest = min(arr)                                 # Find the shortest stick
        total.append(len(arr))                              # Add the length of the array to the 'total' array
        while i < len(arr):                                 # Loop if the array contains objects
            arr[i] = (arr[i] - smallest)                    # Subtract the shortest stick from each array item
            i += 1
        while 0 in arr: arr.remove(0)                       # If any objects in the list are '0', remove them
    return total
print(cutTheSticks(arr))