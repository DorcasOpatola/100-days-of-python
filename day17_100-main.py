# BREAK --- to stop a loop and continue with the next line of code after the loop
# CONTINUE --- to skip the rest of the loop and jump to the start of the same loop again
# EXIT --- to end the program (both loop and the rest of the code) completely


from getpass import getpass as input

print("            === Welcome to Rock Paper Scissors! ===")
print()

print("The rules of the game are as follows:")
print()
print("->   Rock beats Scissors || Scissors beats Paper || Paper beats Rock")
print("->   If both players choose the same move, it's a tie!")
print()

print("ROCK can be represented by '1'.")
print("PAPER can be represented by '2'.")
print("SCISSORS can be represented by '3'.")
print("Let's play!")
print()

counter1 = 3
counter2 = 3

while True:
    player1 = int(input("Player 1, make your move: "))
    player2 = int(input("Player 2, make your move: "))
    if player1 == player2:
        print("It's a tie!")
        continue
    elif player1 == 1 and player2 == 3 or player1 == 2 and player2 == 1 or player1 == 3 and player2 == 2:
        print("Player 1 wins!")
        counter1 -= 1
        if counter1 == 0:
            print()
            print("Player 1 wins the game!")
            exit()
    elif player2 == 1 and player1 == 3 or player2 == 2 and player1 == 1 or player2 == 3 and player1 == 2:
        print("Player 2 wins!")
        counter2 -= 1
        if counter2 == 0:
            print()
            print("Player 2 wins the game!")
            exit()
    else:
        print()
        print("Invalid input! You have not entered rock, paper or scissors, try again.")




'''
A SIMPLE GAME - THE "BREAK" COMMAND IS USED TO EXIT A LOOP. 

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    print("You have found the treasure!")
    break
  else:
    print("You MUST go left or right!")
'''


'''
ALSO A SIMPLE GAME - THE CONTINUE COMMAND IS USED TO JUMP TO THE START OF THE LOOP.
The game only breaks (i.e. ends) when left is selected.

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won") 
'''


'''
HERE IS A COMBINATION OF BOTH BREAK AND CONTINUE.
For as long as the player selects "right", the game continues.
If the player won, the game ends with exit().
If the player loses, the game ends with break and a message.

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
'''
