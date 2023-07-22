# This program's function is to calculate the average of three user provided inputs.

# While there are many ways to calculate the average of a set of numbers, I found it simnpler and more readable to use the mean() function.
# Here we import the mean function from the "statistics" Python library. 

from statistics import mean

# Assign the three user inputs to the following variables: first, second, third.

first = float(input("Enter first number: "))

second = float(input("Enter second number: "))

third = float(input("Enter third number: "))

# Here the float inputs are being put into lists
list = [first,second,third]

# In this print statement, we convert the variables containing the float inputs into strings and add our mean() function to calculate the average of our inputs
print("This average of " + str(first) + ', ' + str(second) + ', ' + str(third) + " is: " + str(mean(list))) 