
# Create a function that uses the formula to compute the balance in a savings account given the amount deposited (p), the annual rate of interest (r), the number of times interest is compounded per year (m), and the number of years that interest accrues (t). 
def futureValue(P, r, n, t):
    A = P * (1 + r/n)** (n*t)
    return A

def main():
    P = float(input("Enter the amount deposited: "))
    r = float(input("Enter the annual interest rate: "))
    n = int(input("Enter the the number of times interest is compounded per year: "))
    t = int(input("Enter the number of years: "))
    A = futureValue(P, r, n, t)
    print("The final deposit (A) is: ", A)


main()      