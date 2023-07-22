import time 

def turn_down_thermo(Merc1237):
    Merc1237 = float(input("Please enter Merc1237 temperature in Celsius: "))
    while Merc1237 > 107.5:
        print()
        print("WARNING: Temperature exceeds 107.5 Celsius; please turn down thermostat, wait 10 minutes and check the temperature again.")
        print("Entering 10 minute waiting period...") 
        print()
        time.sleep(10) # 'time.sleep() being used to force user to wait the specified timeframe before next imput 10 seconds being used for program testing purposes.
        Merc1237 = float(input("Waiting period has ended, Please enter Merc1237 temperature again: "))
        
    print()
    print(f"The current temperature of {Merc1237} degrees celsius is acceptable. Please check temperature again in 20 minutes.")
    print()

    return Merc1237

def main():
    print()
    Merc1237 = float()
    turn_down_thermo(Merc1237)

main()
