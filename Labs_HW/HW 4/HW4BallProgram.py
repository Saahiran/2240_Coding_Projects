#The purpose of this program is to provide information on the height of a ball.

# Create a function that gets the input for "h" (initial height of the ball in feet) and "v" (the initial velolcity of the ball in feet per second)
def getInput():
    h = float(input("Enter the initial height of the ball (in feet): ")) 
    v = float(input("Enter the initial velocity of the ball (in feet per second): "))   
    return h, v 

# Create a function to calculate the height based on the user inputs in the previous function. Gives final height based on the inputs given.
def calculate_height(h, v, t):
    height = h + v * t - 16 * t**2 
    return height 

# Create a function that takes the input from the first function "getInput" and with those inputs, do additional calculations for the max height, and max height at 0.1 seconds.
def main():
    h, v = getInput()
    # Calculating the maximum height
    max_height_time = v / 32 
    max_height = calculate_height(h, v, max_height_time)   
    # Calculate height at 0.1 seconds.
    height_at_01_sec = calculate_height(h, v, 0.1) 
    print("The max height of the ball is: ", round(max_height, 2), "feet. ")
    print("The height of the ball at 0.1 seconds is: ", round(height_at_01_sec, 2), "feet. ")

# Call on main() to run
main()    
