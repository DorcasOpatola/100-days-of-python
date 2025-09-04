print("===CUSTOM AFFIRMATION GENERATOR===")
print()
print("Hi!")

name = input("What's your name? ")
print()
print(name,"you look nice today!")
print()
date = input("What's today's date? (monday, tuesday, wednesday, thursday, friday, saturday, or sunday) ")
favThing = input("What's your favorite thing about today? ")

if date == "monday" or date == "Monday":
  print("Today is",date,"and",favThing,"is really cool!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")
    
elif date == "Tuesday" or date == "tuesday":
  print("Today is",date,"and",favThing,"is badass!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")

elif date == "wednesday" or date ==  "Wednesday":
  print("Today is",date,"and",favThing,"sounds really nice!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")

elif date == "thursday" or date == "Thursday":
  print("Today is",date,"and",favThing,"is also one of my favourite things!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")

elif date == "friday" or date == "Friday":
  print("Today is",date,"and",favThing,"makes you a cool person!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")

elif date == "saturday" or date == "Saturday":
  print("Today is",date,"and",favThing,"is a great thing to have on the weekend!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")

elif date == "sunday" or date == "Sunday":
  print("Today is",date,"and",favThing,"is a great thing to have today!")

  reason = input("Are you happy? YES or NO? ")
  if reason == "Yes" or reason == "yes":
    print("Wonderful!")
  elif reason == "No" or reason == "no":
    print("I'm sorry to hear that.")
    print("I hope your day doesn't get any worse!")
  else:
    print("I don't understand that.")

else:
  print("Incorrect date format")

print()
print(name, "today is a great day to be you!")
