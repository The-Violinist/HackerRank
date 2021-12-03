def is_year_leap(year):
    if year < 1900:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif is_year_leap(year) == False:
        return 28
    elif is_year_leap(year) == True:
        return 29

def day_of_year(year, month, day):
    if year < 1900:
        return None
    if month > 12 or month < 1:
        return None
    if day > days_in_month(year, month) or day < 1:
        return None

    total_days = day
    month = month - 1
    while month > 0:
        total_days += days_in_month(year, month)
        month -= 1

    return total_days



print(day_of_year(2001, 12, 31))