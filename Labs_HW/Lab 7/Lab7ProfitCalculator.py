# Profit Calculator

# profit_calc() will request input (the cost of the iPhone) and will use a while loop to verify if the cost is negative.
# If cost is negative, an error message will appear notifying user that cost cannot be negative
# User will then be prompted to enter a cost that is not a negative number; If positive number inputted, profit_calc() will calculate the profit (iPhone_cost*2.5) 
# 'profit' will the be 'returned' to end the loop and print the sale.
def profit_calc(iPhone_cost):
    iPhone_cost = float(input("Please enter iPhone cost: $"))
    while iPhone_cost < 0: 
        print()
        print("ERROR: Invalid input; cost cannot be negative.")
        iPhone_cost = float(input("Please enter a cost that is greater than 0: $"))
        
    profit = iPhone_cost*2.5
    print()
    print(f"The profit of this sale is: ${profit:.2f}") 
    print()

    return profit
        

# Main function will call on profi_calc() and then request if user wishes to continue (y/n).
# If "y" is selected, then profit_calc() will be called again. If "n" is selected, the program will stop
def main():
    choice = "y"
    while choice.lower() == "y":
        iPhone_cost = float()
        print()
        profit_calc(iPhone_cost)
        input("Do you wish to continue? (y/n): ")
        print()

# Call the main function to start the program which will call on profit_calc() and then request if user wishes to continue.
main()

