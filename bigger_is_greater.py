# HackerRank Bigger is Greater challenge
# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# Determine the next greater string (if any) based off of ascii values

### Work in progress

w = "imllmmcslslkyoegymoa"
infile = "testCase.txt"
inControl = "testOut.txt"
with open(infile, "r") as read_file:
    lines = read_file.readlines()
read_file.close()

def biggerIsGreater(w):
    end_loop = 0
    string_char = []
    final = []
    answer = "no answer"
    changed = len(w)
    for item in w:
        string_char.append(ord(item))
    string_char.reverse()
    len_str = len(string_char)
    i = 0
    while i < len_str - 1:
        ii = i + 1
        while ii < len_str:
            if string_char[i] > string_char[ii]:
                string_char.insert((ii + 1), string_char[i])                # Move the item to the next highest place
                del string_char[i]
                end_loop = 1
                changed = len(string_char) - ii                             # The dividing point for list items to reorder
                break
            ii += 1
        if end_loop == 1:
            break
        i += 1
    for item in string_char:
        final.append(chr(item))
    final.reverse()
    if changed == len(w):
        answer = "no answer"
    else:
        unchanged = final[:changed]
        changing = final[changed:]
        changing.sort()
        combined = unchanged + changing
        answer="".join(map(str,combined))
    return answer

# Control group output
ctrlOut = []
with open(inControl, "r") as read_file:
    sample_out = read_file.readlines()
read_file.close()
for line in sample_out:
    outlines = line.strip()
    ctrlOut.append(outlines)

# Test group output
testOut = []
for line in lines:
    eachl = line.strip()
    out_str = biggerIsGreater(eachl)
    testOut.append(out_str)

i = 0
for item in ctrlOut:
    if item != testOut[i]:
        print(f"Input:   {lines[i].strip()}\nControl: {item}\nTest:    {testOut[i]}\n")
    i += 1
