# The purpose of this program is to use mathmatical calculations to compute a user's training heart rate

print()
a = int(input("Please enter your age: "))
r = float(input("Please enter your resting heart rate: "))

# Training heart rate formula
tht = .7 * (220 - a) + .3 * r

print()
print(f"According to the American College of Sports Medicine, your training heart rate is: {tht:.0f} beats/min.")
print()