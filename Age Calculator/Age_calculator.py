import datetime
from calendar import isleap

try:
    def is_leap_year(year):
        return isleap(year)

    def days_in_month(month, leap_year):
        if month == 2:
            return 29 if leap_year else 28
        return 30 if month in [4, 6, 9, 11] else 31

    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    year, month, day = map(int, date_of_birth.split("-"))
    
    birth_date = datetime.date(year, month, day)
    print(f"Your date of birth is: {birth_date}")
    current_date = datetime.date.today()
    
    def cal_age(year, month, day):
        age = current_date.year - year
        # Check if birthday hasn't occurred yet this year
        if (current_date.month, current_date.day) < (month, day):
            age -= 1
        return age
    
    def age_in_months(year, month, day):
        age_years = cal_age(year, month, day)
        age_months = age_years * 12 + (current_date.month - month)
        if current_date.day < day:
            age_months -= 1
        return age_months
    
    def age_in_days():
        return (current_date - birth_date).days
    
    

    print(f"You are {cal_age(year, month, day)} years old.")
    print(f"You are {age_in_months(year, month, day)} months old.")
    print(f"You are {age_in_days()} days old (using datetime).")

except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
except Exception as e:
    print(f"An error occurred: {e}")