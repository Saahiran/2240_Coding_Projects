# The purpose of this program is to use mathmatical calculations to compute a user's training heart rate

def main():
    item = "ketchup"
    Current_Price(item)

def Current_Price(item):
    regularPrice = float(1.80)
    discount = float(.27)
    sale_price = round(regularPrice - discount, 2) 
    print()
    print(f"{sale_price} is the price of", item)
    print()

main()