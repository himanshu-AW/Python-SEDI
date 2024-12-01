# File handling



# f = open("demo.txt", "w")
# print(f"File name: {f.name} ")
# print(f"File mode: {f.mode} ")
# print(f"is file readable: {f.readable()}")
# print(f"is file writeable: {f.writable()}")
# print(f"is file closed: {f.closed}")

# f = open("demo.txt", "w")
# f.write("This is new text in the file")
# f.write("\nThis is another text in the same file")

# f = open("demo.txt", "w")
# f.writelines("Note: In the above program, data present in the file will be overridden everytime if we run the program. Instead of overriding if we want append operation then we should open the file as follows. ")

# f=open("demo.txt", "r")
# print(f.read())

# f = open("demo.txt", "a")
# f.write("  hii, this is appended to file")

# f=open("demo.txt", "r+")
# print(f.read())
# f.write("This is r+ opeartion")

f=open("demo.txt", "w+")
data = f.write("This is w+ opeartion")
f.seek(0,0)
print(f.read())

# f=open("demo.txt", "r")
# print(f.read())

# f = open("demo.txt", "a+")
# f.write(". this is appended to file")
# print(f.read())

# f = open("demo.txt", "x")
# f.write("x  To open a file in exclusive creation mode for write operation.")
# f = open("demo_2.txt", "x")
# f.write("x  If the file already exists then we will get FileExistsError.")
# f = open("demo.txt", "r")


# f = open("demo.txt", "r")
# print(f.read())
# print(f.read(5))
# print(f.read(5))