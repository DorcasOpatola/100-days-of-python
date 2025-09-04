print(' ==="WELCOME TO ALCARIS FANTANCY WORLD!!!"=== ')
print("Please answer the following questions truthfully and we will give you the best experience.")
print()

protein = input("Do you eat meat or fish?: ")
if protein == "fish":
  print("Great! We have the best fish in the world!")
  print("Follow the signs to the fish counter.")
else:
  print("Okay, but you should try our fish, you won't be disappointed!")
  print("Follow the signs to the meat counter.")
print()

drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")
print()

spice = input("Spice level 0 or 10?: ")
if spice == "10":
  print("We have a spicy option for you.")  
else:
  print("We have a mild option for you.")
print()

print("You have been assigned to table 10. You ordered a", "\033[36m", "spice level", spice, protein, "dish", "\033[0m", "with a calabash of", drink, ".")
print("Thank you for your order.")
print()
print()
print("Enjoy your meal and our fantasy fair!")
