'''Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.'''

largeNumber = None
smallNumber = None

while True: 
    userInput = input("Enter a number: ")
    if userInput == "done":
        break
    try:
        number = int(userInput)
    except:
        print("Invalid input")
        continue

    if largeNumber is None:
        largeNumber = number
    elif number > largeNumber:
        largeNumber = number
    
    if smallNumber is None:
        smallNumber = number
    elif number < smallNumber:
        smallNumber = number
    
# print("All Done!!")
print("Maximum is", largeNumber)
print("Minimum is", smallNumber)
