steps = 8
path = "UDDDUDUU"
def countingValleys(steps, path):
    level = 0
    total_count = 0
    for item in path:
        if item == "U":
            level += 1
            if level == 0:
                total_count += 1
        elif item == "D":
            level -= 1
    return total_count
print(countingValleys(steps, path))