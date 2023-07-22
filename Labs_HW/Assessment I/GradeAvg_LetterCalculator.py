# The purpose of this program is to accept an amount of test scores via user input and then return the average and letter grade based off of the input.
# The intent is to output the student's inputted name + "Grade Calculation"

def main():
    print()
    student_name = input("Please enter the Student's first and last name: ")
    print()
    average_score(student_name)

# grade_level(avg) evalulates the avg passed as an argument and returns the corresponding letter grade using an if-else statement to output the letter grade based off of the calculated average (avg)
def grade_level(avg):
    if avg >= 90:
        return "A"

    elif avg >= 80:
        return  "B"

    elif avg >= 70:
       return "C"

    elif avg >= 60:
        return "D"

    else:
        return "F"
    
# Create a while loop statement to accept at least three test scores. 
# Using a while loop enables scalability.
# Create a function that requests a # of test scores, computes the average, prints the average, and calls on def grade_level(avg): 
def average_score(student_name):    
    num_scores = 0
    score_total = 0
    
    count_total = int(input("Please enter the number of test scores to be calculated: "))
    print()
# Stores the scores in a list
    scores = []
# Create a while loop to accept at least three test scores.  
    while num_scores < count_total:
        score = float(input(f"Please enter test score {num_scores+1}: "))
# Adds inputted score to the "scores" list and uses the append() method to add the "score" to the end of the list after each input.
        scores.append(score)
# Total will be added to the score
        score_total += score 
        num_scores += 1
# Create a print statement that will vertically list the test scores after the "num_scores" has been reached.    
    print() #Create a space for formatting
    print(student_name, "'s Test Scores are: ")
    print("---------------------------------")
    for score in scores:
        print(score)
    print() # Create a space for formatting
# Calculate the avg. By dividing by the "count" variable; this enables scalability.
    avg = round(score_total/num_scores, 2)
    grade = grade_level(avg)
    print("The test score average is:", avg)
    print()
    print("The average letter grade is:", grade)
    print()
    print("Grade Calculation Summary:")
    print("--------------------------")
    print(f"The average of this student's", count_total , "test scores is:", avg, "resulting in a letter grade of:", grade)
    print()

main()

