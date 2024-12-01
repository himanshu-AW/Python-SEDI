from tkinter import *
from PIL import ImageTk,Image

# fun to calculate simple_interest
def calculate_si():
    # clear previous result
    result_box.delete(1.0, END)
    #main logic
    principal = float(E1.get())
    rate = float(E3.get())
    time = float(E2.get())
    if(principal and rate and time):
        si = (principal * rate * time) / 100
        result_box.insert(END, f"Simple Interest: {si:.2f}")
    else:
        result_box.delete(1.0, END)
        result_box.insert(END, "Invalid Input! Please enter numeric values...")
   

# fun to calculate compund_interest
def calculate_ci():
    # clear previous result
    result_box.delete(1.0, END)
    #main logic
    principal = float(E1.get())
    rate = float(E3.get())
    time = float(E2.get())
    if(principal and rate and time):
        ci=principal*(((1+rate)/100)**time)
        result_box.insert(END, f"Compound Interest: {ci:.2f}\n")
    else:
        result_box.delete(1.0, END)
        result_box.insert(END, "Invalid Input! Please enter numeric values...")

# fun to clear the result
def clear_all():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    result_box.delete(1.0, END)

# Main Window
B = Tk()
B.title("Interest Calculator")

# Background image
img = Image.open('./img.png')
#resized_img = img.resize((300, 500), Image.LANCZOS)
image = ImageTk.PhotoImage(img)
panel= Label(B, image=image)
panel.place(x=0,y=0)

# Result Box
result_box = Text(B,height=1 ,width=30, font=("aerial", 20), bg="lightgrey", fg="black", bd=10,pady=10)
result_box.grid(row=0, column=0,columnspan=2)

# Entry for Principal Amount
Label(B, text="PA : ", font=("aerial", 20, "bold"), fg="green").grid(row=1, column=0)
E1 = Entry(B, font=("aerial", 20), bg="pink", fg="blue", bd=10, width=14)
E1.grid(row=1, column=1)

# Entry for Time (Years)
Label(B, text="Time (Years) : ", font=("aerial", 20, "bold"), fg="green").grid(row=2, column=0, padx=10, pady=5)
E2 = Entry(B, font=("aerial", 20), bg="pink", fg="blue", bd=10, width=14)
E2.grid(row=2, column=1, padx=10, pady=5)

# Entry for Rate of Interest
Label(B, text="Rate (%) : ", font=("aerial", 20, "bold"), fg="green").grid(row=3, column=0, padx=10, pady=5)
E3 = Entry(B, font=("aerial", 20), bg="pink", fg="blue", bd=10, width=14)
E3.grid(row=3, column=1, padx=10, pady=5)

# Frames
F1=Frame(B)
F1.grid(columnspan=3)

# Buttons for Calculation
Button(F1, text="SI", font=("aerial", 18, "bold"), bg="yellow", fg="black",bd=6,width=8, command=calculate_si).grid(row=5, column=0)
Button(F1, text="Clear", font=("aerial", 18, "bold"), bg="red", fg="white",bd=6,width=8, command=clear_all).grid(row=5, column=2,)
Button(F1, text="CI", font=("aerial", 18, "bold"), bg="orange", fg="black",bd=6,width=8, command=calculate_ci).grid(row=5, column=1)
