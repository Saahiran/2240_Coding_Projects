#
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) +32
    return celsius_to_fahrenheit

#
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print("The temperature in Fahrenheit is: ", fahrenheit)