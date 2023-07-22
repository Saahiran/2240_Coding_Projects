# The purpose of this program is to create a function that will convert the temperature from Celsius to Fahrenheit.

# Creat the temperature converter function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5 + 32) 
    return fahrenheit

# Create the "celsius" variable that will be used in the function above. Must be able to take user input.
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print("The temperature in Fahrenheit is: " , fahrenheit , "degrees")