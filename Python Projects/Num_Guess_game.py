import random
# ///////////////
# importing random module to generate random numbers
# r=random.randrange(-5, 11)
# generates a random number between -5 and 10 like -5,-4,-3,...9,10

# random_number = random.randint(-5, 10)
# generates a random integer between -5 and 10 (both inclusive)
# /////////////


# top_of_range variable to set the upper limit for random number generation 
top_of_range = input("type a number: ")
# asking uiser how long they wanna number should be generated

if top_of_range.isdigit():
    # checking if the input is a digit
    # if it is digit then we can convert it to integer

    top_of_range = int(top_of_range)
    # converting string input to integer

    guesses = 0
    # initializing guesses variable to count the number of attempts

# checking if the number is less than or equal to 0
    if top_of_range <= 0:
        print("please type a number larger than 0 next time.")
        quit()
else:
        print("you have to type a number next time.")
        quit()

random_number = random.randint(0,top_of_range)
# if used random.randint() should include both 0 and top_of_range
# generating random number between 0 and the number they typed i.e. top_of_range

# print(random_number)  # for testing purpose, to see the generated random number

# guess for a number until the user guesses it correctly

# /////while loop is used to repeatedly prompt the user for a guess until they get it right///////
# while True:
#     print("Tim")
#     break
# above code when tim is printed once the loop will break
# this will help us when user input correct number we can break the loop
# /////////

while True:
    guesses += 1
    # incrementing guesses by 1 for each attempt
    user_guess = input("make a guess: ")
     # asking user to make a guess
    if user_guess.isdigit():
         # checking if the input is a digit
         user_guess = int(user_guess)
         # converting string input to integer
    else:
         print("please type a number next time.")
         continue
         # continue will skip the rest of the loop and start from the beginning again
        #  continue differs from break as break will exit the loop completely
    if user_guess == random_number:
        print("you got it! ")
        print("you guessed " + str(user_guess) + " and the number was " + str(random_number))
        break
        # break will exit the loop when user guesses the correct number 
    else:
        # print("you got it wrong! ")
        if user_guess >  random_number:
            print("you were above the number " )
        else:
            print("you were below the number " )


print("you got it in " + str(guesses) + " guesses")
