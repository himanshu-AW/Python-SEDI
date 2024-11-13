#student grade 
marks = int(input("Enter the number of students: "))
if marks > 90:
    print("Grade A")
elif marks > 80 and marks <= 90:
    print("Grade B")
elif marks > 60 and marks <= 80:
    print("Grade C")
elif marks <= 60 :
    print("Grade D")
else :
    print("Grade E")
