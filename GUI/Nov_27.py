'''from tkinter import *
from PIL import ImageTk,Image

Container = Tk()
Container.title("Image in Tkinter")
img=Image.open('./img.png')

image = ImageTk.PhotoImage(img.resize())

panel=Label(Container,image=image)
panel.place(x=0,y=0)'''



from tkinter import *
from PIL import ImageTk, Image

# Create the main Tkinter window
Container = Tk()
Container.title("Image in Tkinter")
#Container.geometry("400x400")  # Set the window size (adjust as needed)

# Open and resize the image
img = Image.open('./img.png')
new_size = (700, 400)  # Define the new size (width, height)
resized_img = img.resize(new_size, Image.LANCZOS)

# Convert the resized image to a format compatible with Tkinter
image = ImageTk.PhotoImage(resized_img)

# Display the image in a Label widget
panel = Label(Container, image=image)
panel.pack()  # Adjust placement as needed

# Run the Tkinter event loop
Container.mainloop()



#Container.title("Himanshu Chauhan")
#Container.minsize(60,60)
#Container.maxsize(400,400)
#Container.geometry("600x600")
#Container.config(bg="#a569bd")

#l1=Label(Container,text="Enter your Name: ")
#l1.pack()
#l1.place(x=12,y=23)
#l1.grid(2,2)
#E1 = Entry(Container)
#E1.pack()



