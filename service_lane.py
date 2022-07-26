# Service Lane Challenge
# https://www.hackerrank.com/challenges/service-lane
# Find the narrowest width of a specific section of the service lane
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
n = 8
def serviceLane(n, cases):
    min_widths = []                                     # List for the minimum width for each case
    for case in cases:                                  # Loop thru all cases
        widths = []                                     # List for the widths for each case
        for item in range(case[0],(case[1] + 1)):       # Loop thru and append widths for each case
            widths.append(width[item])
        min_widths.append(min(widths))                  # Append the min width for each case
    return min_widths                                   # Return the final list of all min widths

print(serviceLane(n, cases))