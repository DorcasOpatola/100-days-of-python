print(" === IT'S GUESSING GAME TIME !!! ===")

var = 600000
counter = 0

while True:
    var1 = int(input("Choose a number between 0 and 1,000,000. >> "))

    if var1 < 0:
        print("Wrong move pal!")
        exit()
    if var1 < var:
        print("Too low _")
        print()
        counter += 1
        continue
    elif var1 > var:
        print("Too high !")
        print()
        counter += 1
        continue
    else:
        print("YOU'VE GUESSED THE RIGHT ANSWER !")
        print()
        counter += 1
        break

print("You guessed the right answer in", counter, "takes.")
