# WAP to find the length of strings
str = "Demo string"


# Q2:WAP to count the frequency of each characters
def count_frequency(str):
    # frequency_str = {}
    # for char in str:
    #     # if char.isalpha():
    #     if 65 <= ord(char.upper()) <= 90:
    #         frequency_str[char] = frequency_str.get(char, 0) + 1
    # return frequency_str
    return {item : str.count(item) for item in str}

# str = "Hello, Welcome to pyhton programming"
# print(f"Frequency: {count_frequency(str)}")

        
# Q3.WAP to get a string from a given string where all the occurance of its 1st char have been changed to $, except the 1st char itself.
# Sample string: restart
# output: resta$t

def replace_char(str):
    # return str[0] + str[1:].replace(str[0], '$')
    char = 'r'
    # result = str()

    return

str = "restart"
print(f"New String: {replace_char(str)}")
str="characterstic"
print(f"New String: {replace_char(str)}")



