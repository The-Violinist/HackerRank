a = [3,4,5]
k = 1 # number of rotations
queries = [1,2] # indeces of number queries after rotations

def circularArrayRotation(a, k, queries):
    # Find the relative placement difference in the array
    if k % len(a) == 0:
        diff = 0
    elif k < len(a):
        diff = k
    else:
        diff = k % len(a)
    
    # Create list of the query results
    query_results = []
    for item in queries:
        num = item - diff
        query_results.append(a[num])
    return query_results

print(circularArrayRotation(a, k, queries))
