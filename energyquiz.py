# This is my Home Energy Practice Quiz
# This program was written to further enhance my knowledge in Home Energy Improvement and the python language
# I guess you could say I killed two birds with one stone here

# Player Authentication
print("Welcome to my Home Energy Practice Quiz!")
player_authentication = input("Would you like to Play? ")
if player_authentication.lower() != "yes":
    quit()
# Scoring System ( Increments +1 point for eery correct answer and remains the same for every incorrect answer).
points = 0
print("Each Correct Answer is Worth One Point")
# Questions ( The input function is used to store the user input as our "ans" variable, .lower() ensures every string entered by the user is transformed to all lowercase.  This is because
# my answers are stored in all lowercase letters, this avoids creating a case-sensitive issue.)
ans = input("1. What does HRV stand for? ")
if ans.lower() == "heat recovery ventilator":
    print("That is Correct!")
    points += 1
    print("You now have ", points, "/20 points")
else:
    print("That is Incorrect!")
    print("You now have ", points, "/20 points")

ans = input("1. What does ERV stand for? ")
if ans.lower() == "energy recovery ventilator":
    print("That is Correct!")
    points += 1
    print("You now have ", points, "/20 points")
else:
    print("That is Incorrect!")
    print("You now have ", points, "/20 points")
