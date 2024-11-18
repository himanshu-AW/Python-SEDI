# Question 12- Write a Python program to display the current date and time.
import datetime, time

curr_time = datetime.datetime.now()
print(f"Current Date & Time : {curr_time}")
print(f"Year : {curr_time.year}")
print(f"Month : {curr_time.month}")
print(f"Day : {curr_time.day}")
print(f"Hour : {curr_time.hour}")
print(f"Minute : {curr_time.minute}")
print(f"Second : {curr_time.second}")
print(f"Microsecond : {curr_time.microsecond}")

curr_time = time.strftime("%H:%M:%S",time.localtime())
print(f"Current Time is :{curr_time}")