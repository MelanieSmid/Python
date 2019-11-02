# Functions
def print_welcome():
    """This function prints two lines of texts"""
    print("Welcome to my program")
    print("I hope you like it")

print_welcome()
print()
print("To say it again")
print()
print_welcome()

def print_value(value):
    """This function prints the value passed in"""
    print ("Your value is:", value)

print_value(5)
print_value("number")

name = "Pat"
print_value(name)

def change_value(value):
    """This function changes the value passed in to 1"""
    print("Inside, value is: ", value)
    value = 1
    print("Inside, value is changed to:", value)

number = 5
print ("Outside, number is", number)
change_value(number)
print("Outside, number is now: ", number)

def change_number():
    """This function changes the value passed into 1 (global)"""
    global number
    number = 1

number = 5
print("Outside, number is: ", number)
change_number()
print("Outside, number is now: ", number)