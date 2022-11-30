print("Welcome to my Home Energy Practice Quiz!")

player_authentication = input("Would you like to Play? ")

if player_authentication.lower() != "yes":
    quit()

points = 0

ans = input("1. What does HRV stand for? ")
if ans.lower() != "heat recovery ventilator":
    print("Sorry, that is incorrect.")
else:
    print("That is Correct!")
    print("You have been awarded ", points + 1, "point(s)")
