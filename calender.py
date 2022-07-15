
import calendar
year=int(input('enter the year: '))
display=calendar.calendar(year)
print(display)
c=calendar.TextCalendar(calendar.MONDAY)
str=c.formatmonth(2018,1)
print (str)