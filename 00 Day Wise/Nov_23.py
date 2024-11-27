#Remove pentuations in string
def remove_pencuation(str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in str:
        if char in punctuations:
            str = str.replace(char, "")
    return str

#Remove digits
def remove_digits(str):
    for char in str:
        if char.isdigit():
            str = str.replace(char,"")
    return str

user_str = input("Enter a string: ")
print(remove_pencuation(user_str))
print(remove_digits(user_str))


