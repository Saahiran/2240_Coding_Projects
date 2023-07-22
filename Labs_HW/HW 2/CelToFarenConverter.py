# This program converts Celsius temperatures to Farenheit

# Assign the "celsius" variable in a float input() function to be able to use the input in a mathematical formula.
celsius = float(input("Enter the temperature in Celsius: \n")) 

# Assign the celsius to fahrenheit temperature conversion formula to the "fahrenheit" variable.
fahrenheit = float(9 / 5 * celsius + 32)

# Convert the "farenheit" variable into a string to be able to concat in the print statement.
fahrenheit = str(fahrenheit)

# Create the print statement so that it will read: "The temperature in Fahrenheit is ___ degrees"
print("The temperature in Fahrenheit is " + fahrenheit + " degrees")