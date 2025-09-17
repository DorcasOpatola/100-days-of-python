import random

print("                    === IT'S RANDOM GUESSING GAME TIME !!! ===")
print("                        Totally Random One-Million-to-One")
print()
var = random.randint(1, 1000000)
counter = 1

while True:
    print("I have picked a number in my mind. Can you guess it?")
    print()
    var1 = int(input("It's a number between 1 and 1,000,000. GUESSSSS >> "))

    if var1 < 0:
        print("Wrong move pal!")
        exit()
    if var1 < var:
        print("Too low 😏")
        counter += 1
        continue
    elif var1 > var:
        print("Too high 🧐😵‍💫😵‍💫")
        counter += 1
        continue
    else:
        print()
        print("YOU'VE GUESSED THE RIGHT ANSWER !🏆🎖️🏆🎖️🏆🎖️🏆🎖️🏆🎖")
        print()
        counter += 1
        break

print("It took you", counter, "guesses to get the correct number.")
print("Click 'RUN' to try again with a different number.")



'''
## This code generates 10 random numbers between 1 and 100 and prints them to the console.

import random

for i in range(10):
    myNumber = random.randint(1, 100)
    print(myNumber)
'''