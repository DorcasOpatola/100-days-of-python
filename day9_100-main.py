print("===GENERATION GENERATOR===")
print("This program will tell you what generation you are based on your year of birth!")
print("")
print()

myAge = int (input("What is your year of birth? "))
if myAge == 1925 or myAge < 1947 :
  print("Traditionalist, the revered Silent Generation!🙂‍↕️ 🙂‍↕️")
elif myAge == 1947 or myAge < 1965 :
  print("Baby Boomers generation, the generation that built the world!🫡 🫡")
elif myAge == 1965 or myAge < 1982 :
  print("Generation X , the generation that grew up with computers!🥸 🥸")
elif myAge == 1982 or myAge < 1996 :
  print("Millenial darling, generation internet geng!😎 😎")
elif myAge == 1996 or myAge < 2016:
  print("Generation Z, the smartphones generation!😍 😍")
else:
    print("You make me feel old😭")
