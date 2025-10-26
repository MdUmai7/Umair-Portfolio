print("welcome to my computer quiz!")

playing = input("do you want to play? ")
# we can give input a prompt message
# output for above line will be: do you want to play?
if playing.lower() != "yes":
    quit()
    # above quit() function will stop the program if user types anything other than "yes"
print("okay! let's play :) ")
score = 0
# initialize score variable to keep track of correct answers

# ask user some questions

answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
    # increment score by 1 for correct answer

else:
    print("incorrect!")
    print("the correct answer is 'central processing unit'")
    # quit()
    # dont quit the game on incorrect answer, let user continue
answer = input("what does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("the correct answer is 'graphics processing unit'")
    # quit()  
answer = input("what does ram stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("the correct answer is 'random access memory'")
    # quit()
answer = input("what does rom stand for? ")
if answer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    print("the correct answer is 'read only memory'")
    

print("you got " + str(score) + " questions correct!")
# used str() function to convert score (int) to string for concatenation
# because we cannot concatenate string with int directly
# example: "you got " + 3 + " questions correct!" will give error
# but "you got " + str(3) + " questions correct!" will work fine
print("you got " + str((score / 4) * 100) + "%")
# calculate percentage score
