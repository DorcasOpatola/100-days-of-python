import os
import random
import time

counter = 0
winner = None

def rollDice(side):
    result = random.randint(1, side)
    return result

def character_type():
    print("Legend type? (Human, Elf, Wizard, Orc) ")
    userType = input("> ")
    time.sleep(1)
    print("Your legend is Chief", userType + ".")
    return userType

# "\n" don't forget this guy, to help you move to the next line.

def healthGenerator():
    roll10_6 = rollDice(6)
    roll10_12 = rollDice(12)
    health = int(((roll10_6 * roll10_12) /2) + 10)
    return health

def strengthGenerator():
    roll12_6 = rollDice(6)
    roll12_8 = rollDice(8)
    strength = int(((roll12_6 * roll12_8) /2) + 12)
    return strength


print("                     === ⚔️⚔️ ", "\033[35m", "CHARACTER BUILDER", "\033[0m", " ⚔️⚔️ ===")
print()
time.sleep(0.2)
print("                              ::GAME CONTROLS:: ")
print("Create your legend by naming it, choosing its type, and generating its health and strength stats.")
time.sleep(1)
print()
print()

#   Character #1 -- name and type
username1 = input("Name your legend: \n")
time.sleep(0.5)
type1 = character_type()
print()

#   Character #1 -- health status and strength
print("\033[1;31m", username1, "of the almightyy!!", "\033[0m")
time.sleep(1)
health1 = healthGenerator()
print("HEALTH: ", health1)
time.sleep(0.5)
strength1 = strengthGenerator()
print("STRENGTH: ", strength1)
print()
time.sleep(1)

#Character #2 -- name and type
print("Who are they battling?")
username2 = input("Name your legend: \n")
time.sleep(0.5)
type2 = character_type()
print()

#   Character #2 -- health status and strength
print("\033[1;31m", username2, "of the magnificents!!", "\033[0m")
time.sleep(1)
health2 = healthGenerator()
print("HEALTH: ", health2)
time.sleep(0.5)
strength2 = strengthGenerator()
print("STRENGTH: ", strength2)
print()
time.sleep(1)
print(health2)
os.system("clear")


while True:
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print("The battle begins!")
    # battle()

    # to find the difference between the strengths of the characters
    difference = abs(strength1 - strength2) + 1
    # 'abs' means ABSOLUTE, to always get a positive number.

    char1 = rollDice(6)
    char2 = rollDice(6)
    if char1 == char2:
        counter += 1
        print("There is no winner for round", counter, "! Their swords clash and both take minor damage.")
        print()
    elif char1 > char2:
        counter += 1
        health2 = health2 - difference
        print(username1, "01 wins round", counter)
        print()
    elif char2 > char1:
        counter += 1
        health1 = health1 - difference
        print(username2, "02 owns round", counter)
        print()


    print(username1, "health is now:", health1)
    print(username2, "health is now:", health2)
    print()
    time.sleep(0.2)

    if health1 <= 0:
        print(username1, "has died!")
        print(username2, "the chief among", type2, "IS THE UNDISPUTED CHAMPION!")
        winner = username2
        break
    elif health2 <= 0:
        print(username2, "has died!")
        print(username1, "the chief among", type1, "IS THE UNDISPUTED CHAMPION!")
        winner = username1
        break
    else:
        print("The battle rages ooonnnn!!! They're bothe standing for the next round.")
        print()
        print()
        continue

time.sleep(1)
os.system("clear")
print()
print("⚔️ BATTLE TIME ⚔️")
print()
print("🏆🏆🏆 THE WINNER:", "\033[33m", winner, "🏆🏆🏆", "\033[0m", "won after", counter, "rounds.")


'''#   Game controls
userRequest = input("Press 1 to play again or press 2 to exit the game >> ")
if userRequest == "1":
    time.sleep(1)
    os.system("clear")
    continue
elif userRequest == "2":
    time.sleep(1)
    break
else:
    print("CHOOSE A VALID OPTION NEXT TIME !!!")'''


print()
print("Thanks for playing!")

print("\033[35m", "May your name go down in legend...", "\033[0m")
