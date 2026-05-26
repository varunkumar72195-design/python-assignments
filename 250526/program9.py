#Program 9
#Write a Python program to display calendar.
import calendar
year=int(input("enter year:"))
month=int(input("enter month:"))
cal=calendar.month(year,month)
print(cal)
