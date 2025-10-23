import random

print("             === 🏈🏀🎲", "\033[35m", "CHARACTER STATS GENERATOR", "\033[0m", "🏈🏀🎲 ===")
print()
print("The Rules are simple, you set the dice number of sides, and then you roll it.")
print("You can roll it as many times as you want.")
print()

charName = input("Set your character's name >  ")
rollDice = int(input("How many sided dice do you want?🧐 (Natural numbers only) > "))

# Create a subroutine that rolls a dice of any size and returns that number.
def dices(rollDice):
  dice = random.randint(1, rollDice)
  print("You rolled", dice)
dices(rollDice)

# create a second subroutine that rolls one six-sided dice and one eight-sided dice.
def diceOfSix(rollSix=6, rollEight=8):
  sixSides = random.randint(1, rollSix)
  eightSides = random.randint(1,rollEight)
  return sixSides * eightSides
print(charName, "health status is", diceOfSix())
#(diceOfSix(rollSix))  #print --- you don need to prefix this line with 'print' because the subroutine already has a print statement.
# this line 28 only makes diceOfSix a global function/variable; at the same time, it is unnecesarry because the def diceOfSix already has a return statement.


while True:
  print()
  roll_dice_again = input("Roll again? (y/n) > ")
  if roll_dice_again == "y":
    charNameAlt = input("Name your character >  ")
    print(charNameAlt, "health status is", diceOfSix())
  elif roll_dice_again == "n":
    print()
    print("🎲🎲")
    print("Thanks for playing!")
    exit()

   

'''
ANSWER

import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result
def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")
'''


'''
SUBROUTINES IN PYTHON

- a block of reusable code with the 'def' keyword is called "FUNCTION".
- a block of reusable code with the 'class' keyword is called "CLASS".

A subroutine is a set of instructions designed to perform a frequently used operation within a program.
In Python, subroutines are implemented using functions, I.E., the def keyword.
Functions can take inputs, called parameters, and can return outputs using the return statement.

Example: Create a function that generates a random pin number of a given length --- here, it is 5.
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = ""  #this is the empty string
  for i in range(number):  #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9))  #we want a string of random numbers between 0-9
  return pin

myPin = pinPicker(5)  #5 means we want 5 random numbers
print(myPin)


###
SCOPE is a variable only available from inside the region it was created.
Variables that are created for the first time in a subroutine are only available inside that subroutine.
We cannot call the variable area outside the subroutine.
We need to create the variable area inside the subroutine.

def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
# print(area) #This will raise an error because 'area' is not defined outside the function.
#To fix the error, we can print the area inside the function or return it and print it outside.

peace = areaOfTriangle (5, 22)
print(peace) #This will work because we are printing the returned value of the function.
'''
