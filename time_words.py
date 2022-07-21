# Time in words
# https://www.hackerrank.com/challenges/the-time-in-words
# Convert the time in numerals to words

### Input data ###
h = 5
m = 45

num_strings = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"quarter",
    16:"sixteen",
    17:"seventeen",
    18:"eightteen",
    19:"nineteen",
    20:"twenty",
    30:"half"
}

def timeInWords(h, m):
    earlier = "past"                                                            # The word to use in reference to the hour
    if m > 30:                                                                  # If more than halfway thru the hour, countdown to the next hour
        h += 1                                                                  # Increment the hour by 1
        m = 60 - m                                                              # Count down the minutes
        earlier = "to"
    
    # Set the wording to be used for the time
    if m == 0:                                                                  # If 0 minutes
        minutes_word = "o' clock"
        return f"{num_strings[h]} {minutes_word}"
    elif m == 1:                                                                # If 1 minute
        minutes_word = "minute "
    elif m % 15 == 0:                                                           # If 15, 30, or 45
        minutes_word = ""
    else:                                                                       # All other times use 'minutes'
        minutes_word = "minutes "

    # Get the word for the minutes
    if m % 10 == 0:                                                             # If the time is on a 10
        minutes = num_strings[m]
    elif m > 20:                                                                # Concatenate the wording for the 20s
        minutes = f"{num_strings[int((m)/10) * 10]} {num_strings[m % 10]}"
    else:                                                                       # All other times are in the dictionary
        minutes = num_strings[m]
    
    return f"{minutes} {minutes_word}{earlier} {num_strings[h]}"
print(timeInWords(h, m))