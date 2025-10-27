# go to terminal and install the required package
# pip install playsound or pip3 install playsound or python3 -m pip install playsound
# if facing issue use 
# pip install --upgrade setuptools wheel
# pip install playsound
# this will install the required package
# if still facing issue try
# pip install playsound==1.2.2

from playsound import playsound

# playsound('Alaram.mp3')
# you can use any mp3 file just change the name 'Alaram.mp3' to your file name
# make sure the mp3 file is in the same directory as this python script

import time


CLEAR ="\033[2J"
# ANSI escape sequence to clear the terminal screen
CLEAR_AND_RETURN ="\033[H"
# ANSI escape sequence to move the cursor to the top left corner of the terminal


# function to set alarm
def alarm(seconds):
    time_elapsed = 0
    # time_elapsed variable to keep track of time elapsed elapsed means how much time has passed
    while time_elapsed < seconds:
        # loop will run until time_elapsed is less than seconds
        time.sleep(1)
        # wait for 1 second and then increment time_elapsed by 1
        time_elapsed += 1

        # 
        print(CLEAR)
        # clear the terminal screen

        # 

        time_left = seconds - time_elapsed
        # calculate time left by subtracting time_elapsed from seconds
        minutes_left = time_left // 60
        # calculate minutes left by dividing time_left by 60
        seconds_left = time_left % 60
        # calculate seconds left by getting the remainder of time_left divided by 60
        # % is modulus operator which gives the remainder
        # for example 7 % 3 = 1 because 3 goes into 7 two times with a remainder of 1
        # // is floor division operator which gives the quotient without the remainder
        # for example 7 // 3 = 2 because 3 goes into 7

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: ({minutes_left:02d}):({seconds_left:02d})")
        # THE CLEAR_AND_RETURN will move the cursor to the top left corner of the terminal
        # formatted string to display time left in minutes and seconds
        # :02d means to display the number with at least 2 digits, if less than 2 digits then add leading zeros


        #    # when the loop ends it means the alarm time has reached
    playsound('Alaram.mp3')
    # play the alarm sound

minutes=int(input("Enter minutes to wait: "))
seconds=int(input("Enter seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
