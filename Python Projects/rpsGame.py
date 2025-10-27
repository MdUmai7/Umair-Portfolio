import random

# two variables one for user wins and one for computer wins
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to quit: ").lower()
    # taking user input and converting it to lowercase

    if user_input == "q":
        # quit()
    # if user types q the program will quit
        break
    # breaking the loop if user wants to quit

    if user_input not in options:
        # created a list of valid options and checking if user input is in that list
        # if user input exists in the list we proceed further ...if user_input in ["rock", "paper", "scissors"]:

        # here used not in to check if user input is not in the list
        continue
    # continue will skip the rest of the loop and start from the beginning again

# generating computer choice
    random_number = random.randint(0, 2)
    # generating a random number between 0 and 2 for computer choice
    # here 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        # and condition checks if both conditions are true
        # or condition checks if at least one condition is true
        print("You win!")
        user_wins += 1
        continue        
    elif user_input == "paper" and computer_pick == "rock":
        # using elif to check multiple conditions\
        # used elif instead of multiple if statements to avoid checking all conditions once one condition is met
        print("You win!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue
    else:
        print("You lose!")
        computer_wins += 1

print("You won " + str(user_wins) + " times.")
print("Computer won " + str(computer_wins) + " times.")
print("Goodbye!")

    