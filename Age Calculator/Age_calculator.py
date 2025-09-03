import time
from calendar import isleap

def is_leap_year(year):
    return isleap(year)
def days_in_month(month, leap_year):
    if month == 2:
        return 29 if leap_year else 28
    return 30 if month in [4, 6, 9, 11] else 31
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
year, month, day = map(int, date_of_birth.split("-"))
def cal_age(year, month, day):
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday

    age = current_year - year
    if (current_month, current_day) < (month, day):
        age -= 1 # Decrement age if birthday hasn't occurred yet
    return age
print("Your age is:", cal_age(year, month, day))