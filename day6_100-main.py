print("SECURE LOGIN")
print()

username = input("Username > ")
password = input("Password > ")
print()

if username == "admin" and password == "00001":
  print("Welcome to Administrative Section")
elif username == "mark" and password == "password":
  print("Welcome to Marketing Group")
elif username == "simi" and password == "12345":
  print("Welcome to the Engineering Team!")
else:
  print("INVALID LOGIN DETAILS")
