show = input("What is your favourite show? ")
if show == "lupin":
  print("Thank you.")
  
  favShow = input("Are you a Superfan? ")
  if favShow == "yes":
    print("REALLY!!")
    
    superfan = input("Where was the pricipal location of the show? ")
    if superfan == "london, new york, barcelona, florence, rome" :
      print("You're NOT a superfan.")
    elif superfan == "paris":
      print("\033[33m", "You're a superfan.", "\033[0m")
    else:
      print("You've definiely never watched the show 🙄.")
      
  else: 
    print("What are you doing with your life?")
    print("You should watch Lupin.")
    
elif show == "killing eve":
  print("That's a violent show.")

else:
  print("What's that?")
  print("You should watch Lupin.")
