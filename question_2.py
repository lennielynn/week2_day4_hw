



# Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

class String:
    def __init__(self):
        self.string = " "

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())



string_class = String()
string_class.get_String()
string_class.print_String()