# The purpose of this program is to return a first and last name via user inputs utilizing functions.

# Creating the function to retreive the last name.
def get_last_name():
    last_name = input("Enter your last name: ")
    return last_name 

# Creating the function to return the first name
def get_first_name():
    first_name = input("enter your first name: ")
    return first_name

# Assignging the functions to their respective variables: "first_name" and "last_name".
first_name = get_first_name()

last_name = get_last_name()

print(f"First name: {first_name}" )

print(f"Last name: {last_name}" )