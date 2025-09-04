from getpass import getpass as input

print("            === Welcome to Rock Paper Scissors! ===")
print()

print("The rules of the game are as follows:")
print()
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("If both players choose the same move, it's a tie!")
print()

print("ROCK can be represented by 'r', 'R', or '1'.")
print("PAPER can be represented by 'p', 'P', or '2'.")
print("SCISSORS can be represented by 's', 'S', or '3'.")
print("Let's play!")
print()

player1 = int(input("Player 1, make your move: "))
player2 = int(input("Player 2, make your move: "))
if player1 == player2:
    print("It's a tie!")
elif player1 == 1 and player2 == 3 or player1 == 2 and player2 == 1 or player1 == 3 and player2 == 2:
    print("Player 1 wins!")
elif player2 == 1 and player1 == 3 or player2 == 2 and player1 == 1 or player2 == 3 and player1 == 2:
  print("Player 2 wins!")
else:
  print("Invalid input! You have not entered rock, paper or scissors, try again.")
