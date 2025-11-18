import os
import random
import time

counter = 0

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

def battle():
    char1 = rollDice(6)
    char2 = rollDice(6)
    if char1 == char2:
        print("It's a tie!")
    elif char1 > char2:
        print("Character 1 wins!")
    else:
        print("Character 2 wins!")
    return char1, char2
    

while True:
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

    #Character #2
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
    
        char1 = rollDice(6)
        char2 = rollDice(6)
        if char1 == char2:
            print("It's a tie!")
            print("There is no winner!")
            counter = +1
            print()
        elif char1 > char2:
            print("Character 1 wins!")
            print(username1, "wins this round!")
            counter = +1
            print()
        elif char2 > char1:
            print("Character 2 wins!")
            print(username2, "owns this round!")
            counter = +1
            print()
    
        strength1 = int(strength1 - char1)
        strength2 = int(strength2 - char2)
    
        # losers strength reduction
        characterOneWins = (strength1 - strength2) +1
        strength2 = strength2 - characterOneWins
        characterTwoWins = (strength2 - strength1) +1
        strength1 = strength1 - characterTwoWins
        #char1 = username1
        #char2 = username2
      
        if counter == 3:
            break
        elif strength1 <= 0:
            print(username2, "the chief among", type1, "IS THE UNDISPUTED CHAMPION!")
            break
        elif strength2 <= 0:
            print(username1, "the chief among", type2, "IS THE UNDISPUTED CHAMPION!")
        else:
            continue
    
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


print()
print("Thanks for playing!")

print("\033[35m", "May your name go down in legend...", "\033[0m")
