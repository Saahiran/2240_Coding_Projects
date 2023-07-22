# This program is designed to add numbers and be able to ask how many numbers to add

print()
def additionNum():
    total = 0 #Ensures total cannot be negative
    count_total = int(input("How many numbers do you want to add? ")) #Using an integer because you can only ask for whole numbers.
    print()
    for i in range(count_total):
        number = float(input("Enter a number: "))
        total += number

    return total

# Call the function to add numbers and print the total result
result = additionNum()
print()
print(f"The total of your number set is: {result:.2f}")    
print()