print("             === 🎲🎲🎲", "\033[35m", "INFINITY DICE GAME", "\033[0m", "🎲🎲🎲 ===")
print()
print()
print("The Rules are simple, you choose how many sides the dice will have, and then you roll it.")
print("You can roll it as many times as you want.")


import random

def dices():
  print()
  choose_dice = int(input("How many sides?🧐 (Natural numbers only) > "))
  dice = random.randint(1, choose_dice)
  print("You rolled", dice)
  print()
dices()

while True:
  roll_dice_again = input("Roll again? (y/n) > ")
  if roll_dice_again == "y":
    dices()
  elif roll_dice_again == "n":
    print()
    print("🎲🎲")
    print("Thanks for playing!")
    exit()


'''
THIS CODE ASKS FOR TWO PIZZA TOPPINGS AND COMMENTS ON THEM.
A SUBROUTINE IS CREATED, CALLED pizza_order, WHICH TAKES TWO PARAMETERS, topping1 AND topping2.

def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than", topping1)

topping1 =  input("Name a pizza topping > ")
topping2 = input("Name a second pizza topping > ")

pizza_order(topping1, topping2)
'''

'''
THIS CODE PRINTS OUT THE BIGGER OF TWO NUMBERS

def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")
biggerNumber (1800,332)
'''


'''
THIS CODE SHOWS HOW TO USE FUNCTIONS, PARAMETERS AND ARGUMENTS

def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)
'''