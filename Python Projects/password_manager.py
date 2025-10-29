# NOT COMPLETED YET


# pip install cryptography
# importing the required module from cryptography library
# cryptography is a library in python to perform encryption and decryption
from cryptography.fernet import Fernet

# key+password+text to encrypt=random text
# random text + key+password=text to decrypt
# the above two lines create a Fernet object with the generated key
# Fernet object is used to perform encryption and decryption
# without the key, we cannot decrypt the data

# .................create and after running this function just comment it out.................
# as we only need to create the key once

# load key fun at the start of the program
# as we need the key to encrypt and decrypt the passwords


# create a function to load the key from the current directory named `key.key`
def load_key():
    file=open("key.key","rb")
    # open the file key.key in read binary mode
    # rb mode is used to read binary data from the file
    key=file.read()
    # read the key from the file
    file.close()
    return key
# /////////////////////



master_pwd=input("What is the master password?")
# get the master password from the user

key=load_key()+master_pwd.encode()
# load the key from the file and combine it with the master password to create a new key
fer=Fernet(key)
# create a Fernet object with the loaded key

'''# create a function to write the key to a file
def write_key():
    key = Fernet.generate_key()
    # generate a key for encryption and decryption
    with open("key.key", "wb") as key_file:
        # open the file key.key in write binary mode
        # wb mode is used to write binary data to the file
        # if the file does not exist, it will be created
        key_file.write(key)
        # write the generated key to the file key.key
write_key()
# ..................................................................'''










# create two functions: one for adding a new password and one for viewing existing passwords
def view():
  with open("passwords.txt","r") as f:
    #  using r mode to read the file passwords.txt
    for line in f.readlines():
    #   syntax explanation:
    #   f.readlines() reads all the lines from the file passwords.txt and returns a list
    #  for line in <list> iterates over each line in the list
       data=line.rstrip()
    # rstrip() removes any trailing whitespace characters (like \n) from the line
       user, passw = data.split("|")
    # whenever we see | in the line, we split the line into two parts: user and pwd
    #  example "hello|umairyes2" will be changed to a list ["hello", "umairyes2"]
    # then user will be "hello" and passw will be "umairyes2"
       print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
    #    above line decrypts the password using the Fernet object and prints the user and password



def add():
    name=input("Account Name: ")
    pwd=input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

        # above code syntax explanation:
        # with statement is used to open the file passwords.txt in append mode
        # open("passwords.txt","a") opens the file passwords.txt in append mode
        # as f assigns the opened file to the variable f
        # the variable f can be used to read or write to the file passwords.txt


        # 'a' mode is used to append new data to the file
        # r mode is used to read the file
        # w mode is used to write to the file

        # benifit of using with statement is that it automatically closes the file after the block of code is executed
        # else can also use like this 
        # f=open("passwords.txt","a")
        # file.close()


        f.write(name + "|" + pwd + "\n")
        # above line writes the account name and password to the file passwords.txt
    

while True:
    
  mode=input("Would you like to add a new password or view existing ones (view, add)? ")
# ask the user if they want to add a new password or view existing ones
# mode can be either 'view' or 'add'
# is mode a valid input?
# answer should be either 'view' or 'add'
  if mode=="q":
    break
  # if user inputs 'q', break the loop and exit the program

  if mode=="view":
    view()
  if mode=="add":
    add()
  else:
    print("Invalid mode.")
    continue
  # if mode is invalid, print error message and continue to the next iteration of the loop
    
