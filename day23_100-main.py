from getpass import getpass


print("                        === REPLIT USER LOGIN SYSTEM ===")
print("                Welcome to Replit 100 Days of Python Challenge!")
print()

print("You have to create a username and password to use this service.")
def userLoginDetails():
    userName = input("Enter your username: ")
    userPassword = getpass("Enter your password: ")
    print("Welcome,", userName)
    print()
    return userName, userPassword
userName, userPassword = userLoginDetails()

while True:
    print()
    print("Login to your account to proceed.")
    nameLogin = input("What is your username? >> ")
    passwordLogin = getpass("What is your password? >> ")

    if nameLogin != userName and passwordLogin != userPassword:
        print("Whoops! I don't recognize that username or password. Try again!")
        continue
    elif nameLogin == userName and passwordLogin != userPassword:
        print("Incorrect password. Try again!")
        continue
    elif nameLogin != userName and passwordLogin == userPassword:
        print("I don't recognize that username. Try again!")
        continue
    else:
        print("Welcome to Replit!")
        break

print("                        ", "\033[36m", "Login Successful!", "\033[0m")





'''
THIS CODE ROLLS A DICE 10 TIMES, AND 


def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)
rollDice() --- This line of code is only needed if you want to roll the dice just once.

for i in range(10):
  rollDice()

'''