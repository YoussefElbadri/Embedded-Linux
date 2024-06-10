#01-Import the Calender
import calendar

#02-Input the year from the user
inputYear=int(input("Enter the Year: "))

#03-Input the month from the user
inputMonth=int(input("Enter the Month: "))

#04-Print the Calender
print(calendar.month(inputYear,inputMonth, w=0, l=0))