# The purpose of this program is to compute the average of three numbers.

# Assign variables to the three numbers requesting user input()
number_1 = float(input("Enter the first number: "))

number_2 = float(input("Enter the second number: "))

number_3 = float(input("Enter the third number: "))

# Assign the formula calculating the average of three numbers to the "average" variable.
average = float((number_1 + number_2 + number_3) / 3)

#Convert the "average" variable into a string
average = str(average) 

# Print statement to allow proper commas and spacing between the user input values.
print('The average of ' + str(number_1) + ', ' + str(number_2) + ', ' + str(number_3) + ' is: ' + average)