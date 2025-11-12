import os
import random
import time


def character_type():
    print("Legend type? (Human, Elf, Wizard, Orc) ")
    userType = input("> ")
    time.sleep(1)
    print("Your legend is Chief", userType + ".")
    return userType

#   "\n" don't forget this guy, to help you move to the next line.

def healthGenerator():
    roll10_6 = random.randint(1,6)
    roll10_12 = random.randint(1,12)
    health = int(((roll10_6 * roll10_12) /2) + 10)
    return health

def strengthGenerator():
    roll12_6 = random.randint(1,6)
    roll12_8 = random.randint(1,8)
    strength = int(((roll12_6 * roll12_8) /2) + 12)
    return strength

while True:
    print("             === 👾🎰🦸", "\033[35m", "CHARACTER BUILDER", "\033[0m", "🦸🎰👾 ===")
    print()
    time.sleep(0.2)
    print("Create your legend by naming it, choosing its type, and generating its health and strength stats.")
    time.sleep(1)
    print()
    print()

    #   Character name and type
    username = input("Name your legend: ")
    time.sleep(0.5)
    character_type()
    print()

    #   Character health status and strength
    print(username, "the almightyy!!")
    time.sleep(1)
    print("HEALTH: ", healthGenerator())
    time.sleep(0.5)
    print("STRENGTH: ", strengthGenerator())
    print()
    time.sleep(1)
    print("\033[35m", "May your name go down in legend...", "\033[0m")
    print()

    #   Game controls
    userRequest = input("Press 1 to play again or press 2 to exit the game >> ")
    if userRequest == "1":
        time.sleep(1)
        os.system("clear")
        continue
    elif userRequest == "2":
        time.sleep(1)
        break
    else:
        print("CHOOSE A VALID OPTION NEXT TIME !!!")

print("Thanks for playing!")


'''
#   REPLIT SOLUTION

def rollDice(side):
    result = random.randint(1, side)
    return result

def health():
    healthStat = int(((rollDice(6) * rollDice(12)) /2) + 10)
    return healthStat

print(health(), "okay")
'''