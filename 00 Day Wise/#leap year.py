#leap year
year = int(input("Enter the year: "))
if year % 100 == 0:
    if year%400:
        print ("Leap year")
    else:
        print("Not leap year")
else:
    if year % 4 == 0:
        print ("Leap year")
    else:
        print("Not leap year")
    
# accept any city from the user and display monument that city