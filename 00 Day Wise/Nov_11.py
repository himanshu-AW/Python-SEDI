age = int(input("Enter you age: "))

'''if age >= 18:
    print("Yes, you can drive")

print("remaining body.")'''


'''if age >= 18:
    print("Yes, you can Drive.")
else :
    print("No, you can't Drive.")'''


'''if age < 18 :
    print("No, you can Drive.")
elif age > 70:
    print("No, you can't Drive.")
else :
    print("Yes, you can Drive.")'''

if age > 18:
    if age < 70 :
        print("Yes, you can Drive")
if age < 18:
    print("No, you can't Drive.")
if age > 70:
    print("No, you can't Drive.")

print("----------remaining body------------")

#if the 1dt condition is true and the inner if condition will also be check otherwis else part will be executed
#if elif statement: if the if part not true then the else if part will be check at the end else block added which is perform if none of the above if elif statemnet is true
