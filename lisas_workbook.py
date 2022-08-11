# Lisa's Workbook
# https://www.hackerrank.com/challenges/lisa-workbook/problem
# Find "Special Problems" such that the index of a problem in a chapter is the same as the page number. Indices start at 1.

# arr = [3,8,15,11,14,1,9,2,24,31]                         # problems in each chapter
# k = 5                               # number of problems which can be on one page

arr = [4,2,6,1,10]
k = 3
n = len(arr)

def workbook(n, k, arr):
    page = 0                        # Page number index
    counter = 0                     # Counter for Special Problems
    for item in arr:                # For each chapter of problems
        page += 1                   # Increment page number for the beginning of each chapter
        i = 0                       # Start each chapter at index 0
        # num = arr[item]           # Number of problems in this chapter
        while item > 0:             # Until there are no more problems in the chapter
            i += 1                  # Increment the problem index by 1
            item -= 1               # Subtract items per page from 
            if i == page:           # Counter if the problem index == the page number
                counter += 1
            if item == 0:           # Stop the loop once all problems are placed on pages
                break
            elif i % k == 0:        # Increment the page if it is full
                page += 1           # Increment the page number if the page is full
    return counter
print(workbook(n, k, arr))