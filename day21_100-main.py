print("            === MULTIPLICATION TABLE GENERATOR ===")

print("                      Math Game! 🥁🥁🥁")
print("You will give me a number, and I will give you the multiplication table (math facts) to solve.")
print("For each correct answer you get, you will get a point.")
multiple_table = int(input("Name your multiples : "))
print()
counter_correct_answer = 1
counter = 0

for i in range(1, 11, 1):
  print(i, "x", multiple_table, "=",)
  answer = int(input("Your answer : "))
  if i*multiple_table == answer:
    print("You got it right! Good job!!! 🥳🎉")
    counter_correct_answer += 1
    counter += 1
    
    if counter_correct_answer == 11:
      print()
      print("BADASS MOVE! 🙌🥁")
      break
    continue
    
  elif i*multiple_table != answer:
    print("You got it wrong. The answer was", i*multiple_table, ".")
    continue

print("You scored", counter, "out of 10.")
