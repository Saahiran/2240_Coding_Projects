# Program done in class below


def profit_calc(iPhone_cost):
    while iPhone_cost < 0:
        print("ERROR: Invalid input; iPhone cost cannot be negative.")
        iPhone_cost = float(input("Enter the iPhone cost: "))

    profit = iPhone_cost * 2.5
    return profit


def main():
    choice = "y"
    while choice.lower() == "y": # .lower() method converts all input to lowercase to avoid issues with intepreting captial v. lowercase inputs
        iPhone_cost = float(input("Enter the iPhone cost: "))
        profit = profit_calc(iPhone_cost)
        print("Profit: $", profit)

        choice = input("Do you wish to continue? (y/n): ")


# Call the main function to start the program
main()
