"""
This is the main file for the next date function. The next date function takes three integer values,
and return the next date
"""
def check_leap_year(year:int)-> bool:
    if (year % 4) == 0 and (year % 100) !=0:
        return True
    elif (year % 400) == 0:
        return True
    else:
        return False

def next_date(month: int, day:int, year:int):
    is_leap_year = check_leap_year(year)
    reset_month = False
    if year <= 2025 or year > 1900:
        if month > 0 and month < 13:
            "This is the logic for the date switching"
            if month == 2:
                """Logic for February"""
                if is_leap_year == True:
                    max_day = 29
                else:
                    max_day = 28
            elif month in [4,6,9,11]: #Logic for days with 30
                max_day = 30
            elif month in [1,3,5,7,8,10,12]: #Sets max day for months with 31 days
                max_day = 31
            if day > 0 and day < max_day: # checks if day is/will be valid
                day += 1
            elif day == max_day: 
                # resets day if above max
                day = 1
                reset_month = True
            if reset_month == True:
                #Month reset
                if month == 12:
                    #Year reset
                    month = 1
                    year += 1
                else:
                    month += 1
    return month,day,year


