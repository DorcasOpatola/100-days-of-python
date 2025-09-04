print("=== Your Food Receipe Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
food, totally something delious!""")
print()
food = input("Name a food: ")
plant = input("Name a plant: ")
cooking = input("Name a cooking method: ")
burnFood = input("What word describes burned food?: ")
item = input("Name a DIY item: ")
print()
print("=== MENU ===")
print(cooking, food, "with", burnFood, plant, "on a bed of", item)
