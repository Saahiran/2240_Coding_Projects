# This is a simple payroll program to calculate an employee's gross pay

# Create a function to calculate the regular pay
def calc_regular_pay(hours_worked,hourly_pr):
    reg_pay = hours_worked * hourly_pr
    print(f"Your gross pay this week is {reg_pay:.2f}")
    print()

# Create a function to calculate the pay with overtime
def calc_pay_with_OT(hours_worked,hourly_pr):
    OT_pay = hours_worked * (hourly_pr * 1.5)
    print()
    print(f"Your gross pay this week with the overtime pay differential is: ${OT_pay:.2f}")
    print()

# Function to be called upon program commencement; will return the # of hours worked and hourly pay rate as input from user.
print()
def main():
    hours_worked = float(input("Please enter the number of hours worked this week: "))
    hourly_pr = float(input("Please enter the hourly pay rate: $"))

# Create if-else statement to return either the OT pay or the Regular Pay calculation depending if the total hours worked in a week exceeds 40.
    if hours_worked >= 41:
        return calc_pay_with_OT(hours_worked,hourly_pr)
    else:
        return calc_regular_pay(hours_worked,hourly_pr)
    
main()