'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.
'''

hrs = input("Enter Hours:")
rph = input("Enter rph:")

h = float(hrs)
rate = float(rph)

if h <= 40:
    regular_pay = rate * h
    total_pay = regular_pay
else:
    regular_pay = rate * 40
    overtime_hours = h - 40
    overtime_pay = overtime_hours * rate * 1.5
    total_pay = regular_pay + overtime_pay

# Print result
print( total_pay)