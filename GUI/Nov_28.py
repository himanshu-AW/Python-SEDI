from tkinter import *

# instance of Tk class
root = Tk()

# add a title
root.title("Hello World!")

label = Label(text="Hii, this is python gui demo.",fg="white",bg="black",width=25, height=1)
entry = Entry()
label.pack()
entry.pack()

# Start the event loop
root.mainloop()
