# The purpose of this program is to output a table that provides ranges of temperature conversions of Celsius and Fahrenheit within a specified range, and step 

# Print statement provides the headers for the table
print()
print("Fahrenheit\tCelsius")
print("-------------------------")
#
for celsius in range (10, 51, 5):
    fahrenheit = (9/5 ) * celsius + 32

# The f-string
#The \t is used to add values to each column 
    print(f"{fahrenheit:.2f}\t\t{celsius}")
    print()