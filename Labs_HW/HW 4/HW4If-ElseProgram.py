# The purpose of this program is to create an income tax calculator. 

# Assign a float input from the user.
income = float(input("Please enter your gross income: "))

# If income is less than or equal to $85,528, then user will be taxed at .18% of their income subtracted $550.02
if income <= 85528:
    tax = (income * 0.18) - 550.02
 # Otherwise, user will be taxed $14, 840.02 + however much they made over $85,528  multiplied by 0.35
else: 
    tax = 14840.02 + ((income-85528) * 0.35) 

# Ensure that tax can't equal a negative number
tax = max(tax, 0) 

print("The calculated tax is: ", round(tax, 2), "dollars. ")
