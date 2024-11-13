import calendar
name=input("enter your name: ")
year=int(input("enter year: "))
month=int(input("enter month: "))
cal=calendar.month(year,month)
print("Hey",name,"Your required calendar is here")
print(cal)
