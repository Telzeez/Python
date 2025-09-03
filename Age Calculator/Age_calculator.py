import datetime

try:
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    year, month, day = map(int, date_of_birth.split("-"))
    
    birth_date = datetime.date(year, month, day)
    current_date = datetime.date.today()
    
    # Calculate age in years
    age_years = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age_years -= 1
    
    # Calculate total months
    total_months = age_years * 12 + (current_date.month - birth_date.month)
    if current_date.day < birth_date.day:
        total_months -= 1
    
    # Calculate total days (simple and accurate!)
    total_days = (current_date - birth_date).days
    
    print(f"You are {age_years} years old.")
    print(f"You are {total_months} months old.")
    print(f"You are {total_days} days old.")

except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")