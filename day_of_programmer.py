year = int(input("Enter a year:\n"))

#HackerRank Day of the Programmer
#Determine what calendar day is number 256 in Russia in years ranging from 1700-2700


###FUNCTIONS###
def is_year_leap(year):
    #Leap years in the Julian Calendar
    if year <= 1917:
        if year % 4 == 0:
            return 29
        else:
            return 28
    #Leap years in the Gregorian Calendar
    else:
        if year % 4 != 0:
            return 28
        elif year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        else:
            return 29

def dayOfProgrammer(year):
    total_days = 256
    i = 1
    #Months listed by same number of days
    long_month = [1,3,5,7,8,10,12]
    short_month = [4,6,9,11]
    #Number of days in February based on year
    feb = is_year_leap(year)
    while total_days > 28:
        #1918 was the switch over and last a few days from the calendar
        if year == 1918:
            total_days = 26
            i = 9
            break
        #Subtract days from the total (256) based on the month
        elif year != 1918:
            if i in long_month:
                total_days = total_days - 31
            elif i in short_month:
                total_days = total_days - 30
            else:
                total_days = total_days - feb
            i += 1
    return (f"{total_days}.0{i}.{year}")

print(dayOfProgrammer(year))