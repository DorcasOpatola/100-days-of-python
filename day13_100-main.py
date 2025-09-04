print("          ===GRADE GENERATOR===")
print()

testSubject = input("What course test score do you want to record?: ")
maxScore = int(input("How many possible points is obtainable for this course?:  "))
print()
score = int(input("How many points did you get?: "))
print()

dpPercent = float(round(score/maxScore*100, 2))
if dpPercent >=90 or dpPercent ==100 :
  print("Congratulations! You got an A+")
elif dpPercent >=80 or dpPercent ==89:
  print("You got an A in" , testSubject, ".")
elif dpPercent >=70:
  print("You got a B in" , testSubject, ".")
elif dpPercent >=60:
  print("You got a C in" , testSubject, ".")
elif dpPercent >=50:
  print("You didn't put in alot of effort. You got a D in" , testSubject, ".")
elif dpPercent <=49:
  print("You failed" , testSubject, ". You are to resit for this course.")
else:
  print("Enter a valid score.")

print()
print()

print("Your test score for", testSubject, "subject is", score, "and your percentage is", dpPercent, "%.")
