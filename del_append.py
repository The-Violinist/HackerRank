# Append and Delete
# https://www.hackerrank.com/challenges/append-and-delete
# Determine if string 's' can be converted to string 't' through deletion and appending using the exact number of edits 'k'

s = "aaa"
t = "a"
k = 5

def appendAndDelete(s, t, k):
    same = 0
    i = 0
    if len(s) > len(t): len_str = len(t) - 1
    else: len_str = len(s) - 1

    for x in range(0, len_str):
        if s[0] != t[0]:
            same = 1
            break
        elif t[x] == s[i]: i += 1
        elif t[x] != s[i]: break

    if same == 1: same = 0
    else: same = i

    total_appends = (len(s) - same) + (len(t) - same)
    if total_appends > k: return "No"
    elif len(s) + len(t) <= k: return "Yes"
    elif total_appends == k: return "Yes"
    elif len(s) == len(t) and total_appends <= k: return "Yes"
    elif total_appends < k and (k - total_appends) % 2 == 0: return "Yes"
    elif s == "" and len(t) <= k: return "Yes"
    elif total_appends < k and (k - total_appends) % 2 == 1: return "No"
    elif s == t and total_appends <= k: return "Yes"
    else: return "No"
print(appendAndDelete(s,t,k))