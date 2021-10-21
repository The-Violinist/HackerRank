scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

def breakingRecords(scores):
    low_score = scores[0]
    high_score = scores[0]
    lowest = 0
    highest = 0
    for score in scores:
        if score > high_score:
            high_score = score
            highest += 1
        if score < low_score:
            low_score = score
            lowest += 1
    records = [highest, lowest]
    return records
print(breakingRecords(scores))