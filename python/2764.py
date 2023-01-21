from datetime import date

inputDate = input()
day, month, year = inputDate.split('/')

newDate = date(int(year), int(month), int(day))

print(date.strftime(newDate, "%m/%d/%y"))
print(date.strftime(newDate, "%y/%m/%d"))
print(date.strftime(newDate, "%d-%m-%y"))