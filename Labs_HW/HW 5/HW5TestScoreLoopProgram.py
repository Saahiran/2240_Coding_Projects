# The purpose of this program is to accept 3 test scores as input via user and then display them.

count = 0
total = 0
print()
count_total = int(input("Please enter the total amount of test scores you would like calculated: "))
print()

# while count < count_total: would increase further scalability

# Create a while loop statement to accept three test scores Using a while loop enables scalability.
while count < count_total:
    score = float(input("Please enter test score: "))
    print("Test score: ", score)
    print()

    # Total will be added to the score
    total += score 
    count += 1

    # Calculate the avg. By dividing by the "count" variable; this enables scalability.
avg = round(total/count, 2)
print("Your average test score is:", avg)
print()