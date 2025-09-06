print("=== ANIMAL SOUNDS ===")
print()
print()

exit = "no"
while exit != "exit":
  
  
  animal2 = input("What animal sound do you want?: ")
  if animal2 == "cat":
    print("A CAT goes mew.") 
  elif animal2 == "cow":
    print("A Cow goes moo.")
  elif animal2 == "dog":
    print("A Dog goes woof.")
  elif animal2 == "duck":
    print("A Duck goes quack.")
  elif animal2 == "sheep":
    print("A Sheep goes baa.")
  elif animal2 == "pig":
    print("A Pig goes oink.")
  elif animal2 == "chicken":
    print("A Chicken goes cluck.")
  elif animal2 == "horse":
    print("A Horse goes neigh.")
  elif animal2 == "goat":
    print("A Goat goes bleat.")
  elif animal2 == "snake":
    print("A Snake goes hiss.")
  elif animal2 == "rooster":
    print("A Rooster goes cock-a-doodle-doo.")
  elif animal2 == "turkey":
    print("A Turkey goes gobble.")
  elif animal2 == "elephant":
    print("A Elephant goes toot.")
  else:
    print("Give me a domestic animal, not wild animal.")

  
  exit = input("Do you want to exit? Type exit to exit: ")
  print()
  