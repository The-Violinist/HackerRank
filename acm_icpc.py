# ACM ICPC Team
# https://www.hackerrank.com/challenges/acm-icpc-team
# Calculate combinations of 2 person teams which cover the most topics
# This scripts performs the function correctly but takes too long to complete the challenge in time
    # Work in progress 03/11/22

from collections import Counter
from itertools import count

topics = ['10101','11100','11010','00101']

def acmTeam(topic):
    arr_len = (len(topic)-1)                                            # Index for the lenght of the array
    item_length = len(topic[0])
    i1 = 0                                                              # Index to use for first number when determining 1's
    highest_count = 0
    highest_count_instance = 0
    while i1 < arr_len:
        i2 = i1+1                                                       # Initiate i2 to be one index greater than i1
        while i2 < len(topic):                                          # Loop until i2 gets to the end of the array
            counter_for_ones = 0                                        # Counts how many 1's there are total
            for letter in range(item_length):                           # Loop until geting to the end of the topic item
                if topic[i1][letter] == '1' or topic[i2][letter] == '1':# Determine if there is a 1 in either of the topic items
                    counter_for_ones += 1
            if counter_for_ones > highest_count:
                highest_count = counter_for_ones
                highest_count_instance = 1
            elif counter_for_ones == highest_count:
                highest_count_instance +=1
            i2 += 1                                                     # Increment the 2nd number of the pair until the end of the array
        i1 += 1                                                         # Increment the first number for the next iteration of the loop
    return [highest_count,highest_count_instance]
print(acmTeam(topics))