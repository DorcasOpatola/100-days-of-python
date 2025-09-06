print("=== NAME THE LYRICS ===")
print()
print()

print("You have to figure out the correct song lyrics in as few attempts as possible.")
print("Good luck!")
print()

print("Fill in the blank lyrics! (Type in the blank lyrics and see if you are as cool as me.)")
print()

counter = 1
while True:
  answer = input("Never going to _____ you up. ")
  if answer != "give":
    print("Nope, too bad. Try again!")
    counter +=1
  else:
    print()
    print("WELL DONE!!!")
    break

print("You are a music guru!")
print()
print("You got the correct lyrics in", counter, "attempts.")
