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
ALSO A SIMPLE GAME - THE CONTINUE COMMAND IS USED TO JUMP TO THE START OF A LOOP.
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