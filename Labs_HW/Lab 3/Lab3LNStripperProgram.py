# The purpose of this program is the strip the second and last letter from a last name

# Create an input() to prompt user to enter a last name; assign function to the "last_name" variable.
last_name = input("Please enter your last name: ")

# Strip the second and last letter from the last name and assign the function to the "stripper_last_name" variable.
stripper_last_name = last_name[1] + last_name[-1]

print(stripper_last_name)