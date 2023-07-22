# This program is intended to display a table of temperatures in Celsius in one column, and convert them to Fahrenheit in the second column.

# conver_to_fahrenheit(celsius) will use the Fahrenheit formula to convert Celsius to Fahrenheit and then assign it to a variable.
def convert_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32 #Fahrenheit formula
    return fahrenheit

# main() will create the headers for the table (Celsius, Fahrenheit), and will then create the range for convert_to_fahrenheit to be called through.
def main():
    print()
    print("\tCelsius\t\t\t\tFahrenheit") #Table headers
    print("--------------------------------------------------------") # For formatting
    for celsius in range(10, 51, 5): # the first value in the range will be 10 and the last will be 50; 5 is the step value
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"\t{celsius}\t\t\t\t{fahrenheit}")
        print()

# Call the main() to start the program that will first create the table headers and then call on convert_to_fahrenheit
main()
