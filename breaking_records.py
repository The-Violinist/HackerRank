# Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records
# Given a set of scores, determine how many times the lowest and highest records are broken

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]              # List of scores

def breakingRecords(scores):
    low_score = scores[0]                                   # Set the first score as the starting lowest
    high_score = scores[0]                                  # Set the first score as the starting highest as well
    lowest = 0
    highest = 0
    for score in scores:
        if score > high_score:                              # Increment the high score counter if 'score' breaks the highest record
            high_score = score                              # Set this score as the new highest
            highest += 1
        if score < low_score:                               # Increment the low score counter if 'score' breaks the lowest record
            low_score = score                               # Set this score as the new lowest
            lowest += 1
    records = [highest, lowest]                             # Create an array with the number of times the highest and lowest records get broken
    return records
print(breakingRecords(scores))