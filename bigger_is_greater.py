# HackerRank Bigger is Greater challenge
# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# Determine the next greater string (if any) based off of ascii values

w = "imllmmcslslkyoegymoa"

def biggerIsGreater(w):
    string_char = []                                            # List for the string input
    final = []                                                  # List for the final string output
    find_least_change = {}                                      # Dictionary for the starting index and number of indices to change
    answer = "no answer"
    changed = len(w)
    for item in w:
        string_char.append(ord(item))                           # Create list of ASCII values
    string_char.reverse()                                       # Reverse the list
    len_str = len(string_char)
    i = 0
    endpoint = 1000000
    while i < len_str - 1:
        if i >= endpoint:
            break
        ii = i + 1
        while ii < len_str:
            if string_char[i] > string_char[ii]:                # If the number in question is greater than the current index iteration, stop inner loop
                endpoint = ii                                   # Change the stopping point to ii
                find_least_change[i] = endpoint                 # Create dictionary entry with the starting index (k) and the number of indexes different
                break
            ii += 1
        i += 1
    if find_least_change == {}:                                 # If there were no changes, return "no answer"
        return "no answer"
    to_move = min(find_least_change, key=find_least_change.get)
    move = find_least_change[to_move]                           # Number of indexes to move

    string_char.insert((move + 1), string_char[to_move])        # Move the item to the next highest place
    del string_char[to_move]
    changed = len(string_char) - move                           # The dividing point for list items to reorder
    for item in string_char:
        final.append(chr(item))                                 # Turn the ASCII values back into a list of strings
    final.reverse()                                             # Reverse back to the correct order
    unchanged = final[:changed]                             # Sort all of the letters beyond the point of change
    changing = final[changed:]
    changing.sort()
    combined = unchanged + changing
    answer="".join(map(str,combined))                       # Join the list back into a single string
    return answer

print(biggerIsGreater(w))