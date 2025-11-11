import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()


def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    music_pause = input("Press 2 to stop the music:  ")
    if music_pause == "2":
      pause()
      return
    else:
      continue


# Start taking user input and doing something with it.

while True:
  # clear the screen 
  time.sleep(1)
  os.system("clear")
  print()
  print()
  print("==========    🎸🎶  MyPOD Music Player  🎶 🥁   ==========")
  # Show the menu
  print()
  print("    Controls for your MyPOD Music Player    ")
  print()
  print("-  Press 1 to Play")
  print("-  Press 3 to Exit")
  print("-  Press anything else to see the menu again.")
  print()
  # take user's input
  pressRequest = input("Your selection >  ")
  # check whether you should call the play() subroutine depending on user's input
  if pressRequest == "1":
    print("Playing some proper tunes!")
    time.sleep(1)
    print("🎶🎶🥁🎸")
    print()
    play()
  elif pressRequest == "3":
    print("Goodbye!")
    break
  else:
    print("Showing the menu options again!")
    time.sleep(1)
    os.system("clear")
    continue

print("Thanks for listening, goodbye!")

'''
MyPOD Music Player

--pause for 2 seconds--

Press 1 to Play
Press 2 to Exit
Pres anything else to see the menu again.

1 (remember to colour code input to a different colour)

Playing some proper tunes!



# DAY 26 --- USE OF PYTHON LIBRARIES 'os' AND 'time'.

import os   # The os library allows us to interact with the operating system.
import time     # The time library allows us to work with time-related tasks, like pausing the program for a certain duration.

for i in range(1,10):
  print(i)
  time.sleep(0.01)
  os.system("clear")

print("Welcome")
print("to")
print("Replit")

time.sleep(10)
os.system("clear")

username = input("Username: ")

'''