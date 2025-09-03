print("=== HOW MANY SECONDS ARE IN A YEAR? ===")
print()
print()


year = int(input("how many days are in a year?: "))
if year == 365:
  print("This is a normal year.")
  secYear = year * 12 * 24 * 60 * 60
  print("There are", secYear, "seconds in this year.")

elif year == 366:
  print("This is a leap year.")
  secLeapYear = year * 12 * 24 * 60 * 60
  print("There are", secLeapYear, "seconds in this year.")

else:
  print("This is not a valid year.")
