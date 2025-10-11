import datetime

day=int(input("Enter the day of your birth:"))

month=int(input("Enter the month of your birth:"))

year=int(input("Enter the year of your birth:"))

a=datetime.date(year, month, day)

print("dob", a)

current_date=datetime.date(2025,9,7)

days_lived=(current_date-a).days

print(days_lived)
