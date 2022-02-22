# Day of the Programmer
# https://www.hackerrank.com/challenges/day-of-the-programmer
# Determine what calendar day is the 256th calendar day in Russia in years ranging from 1700-2700
# Prior to 1917, leap years were calculated as every 4 years (Julian)
# Post 1918, leap years are calculated as every 4 years except (Gregorian)

###FUNCTIONS###
def is_year_leap(year):
    if year <= 1917:                                    ### Leap years in the Julian Calendar
        if year % 4 == 0:                               # If the year is divisible by 4 it is a leap year
            return 29
        else:                                           # Otherwise, it is not a leap year
            return 28
    else:                                               ### Leap years in the Gregorian Calendar
        if year % 4 != 0:                               # If not divisible by 4, year is not leap
            return 28
        elif year % 400 == 0:                           # If divisible by 400, leap
            return 29
        elif year % 100 == 0:                           # If divisible by other centuries, not leap
            return 28
        else:                                           # All other cases, the year is leap
            return 29

def dayOfProgrammer(year):
    total_days = 256                                    # Countdown to day 256
    i = 1                                               # Month iterator
    long_month = [1,3,5,7,8,10,12]                      # Months with 31 days
    short_month = [4,6,9,11]                            # Months with 30 days
    feb = is_year_leap(year)                            # Number of days in February based on is_year_leap function
    while total_days > 28:
        if year == 1918:                                # In 1918 September 26 was the 256th day of the year
            total_days = 26
            i = 9
            break
        else:                                           # Subtract days from the total (256) based on the month until arriving at the the 256th day
            if i in long_month:
                total_days = total_days - 31
            elif i in short_month:
                total_days = total_days - 30
            else:
                total_days = total_days - feb
            i += 1
    return (f"{total_days}.0{i}.{year}")                # Return the 256th day of the calendar in the format DD/MM/YYYY

### MAIN ###
year = int(input("Enter a year:\n"))                    # Take user input of a year for calculation
print(dayOfProgrammer(year))
### END ###