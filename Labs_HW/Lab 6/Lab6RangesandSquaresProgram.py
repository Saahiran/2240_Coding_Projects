# Create a program that uses a "for loop" in a function to display numbers 1-10 and their squares. Also using the range()

print()
print("Numbers and Their Squares List")
print("-------------------------------")
def display_numbers_and_squares():
    for number in range(1,11):
        square = (number**2)
        print(f"Number: {number} ------ Square: {square}")
        print()

display_numbers_and_squares()