from getpass import getpass as input

print("            === WELCOME TO ROCK PAPER SCISSORS! ===")
print()

print("The rules of the game are as follows:")
print("->   Rock beats Scissors || Scissors beats Paper || Paper beats Rock")
print("->   If both players choose the same move, it's a tie!")
print("->   ROCK is represented by '1'.")
print("->   PAPER is represented by '2'.")
print("->   SCISSORS is represented by '3'.")
print()
print("\033[36m", "            L E T ' S   P L A Y !", "\033[0m")
print()

counter1 = 0
counter2 = 0

while True:
  player1 = int(input("Player 1, make your move > "))
  player2 = int(input("Player 2, make your move > "))

  if player1 == player2:
    print("It's a tie!")
    print()
    continue
  elif player1 == 1 and player2 == 3 or player1 == 2 and player2 == 1 or player1 == 3 and player2 == 2:
    print("Player 1 wins!")
    counter1 += 1
  elif player2 == 1 and player1 == 3 or player2 == 2 and player1 == 1 or player2 == 3 and player1 == 2:
    print("Player 2 wins!")
    counter2 += 1
  elif player1 > 3 or player2 > 3 or player1 < 1 or player2 < 1:
    print("Invaid input.")
    print()
    continue
  
  print("Player 1 has", "\033[31m", counter1, "\033[0m", "wins.")
  print("Player 2 has", "\033[33m", counter2, "\033[0m", "wins.")
  print()

  if counter2 == 3:
    print("\033[33m", "       P L A Y E R  2    I S    T H E    W I N N E R   !", "\033[0m")
    print()
    print("Thanks for playing!")
    exit()
  elif counter1 == 3:
    print("\033[31m", "       P L A Y E R  1    I S    T H E    W I N N E R   !", "\033[0m")
    print()
    print("Thanks for playing!")
    exit()
  else:
    continue
