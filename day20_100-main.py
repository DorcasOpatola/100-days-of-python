print("      === LIST GENERATOR ===")
print()

print("Welcome to my number list generator.")
print("This program uses the 'for loop' to generate a list of numbers.")
print("You are to provide a number to start the loop, a number to end before, and the increment.")
print()

start_value = int(input("Start at > "))
end_before = int(input("End before > "))
diff = int(input("How many should be added (or removed) each time? > "))
print()

for i in range (start_value, end_before, diff):
    print(i)
