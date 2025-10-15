'''def addtwo(a, b):
    added = a + b
    return a

x = addtwo(22, 7)
print(x)
'''
'''
 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
 Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
 Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
 The function should return a value.
 Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
 You should use input to read a string and float() to convert the string to a number.
 Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
 Do not name your variable sum or use the sum() function.'''

'''hours = input("Enter Hours: ")
rateperhour = input("Enter Rate per hour: ")

def computepay (hours, rateperhour):
    hoursF = float(hours)
    ratesF = float(rateperhour)
    if hoursF <= 40:
        salaryPay = hoursF * ratesF
    else:
        extraHours = hoursF - 40
        extraPay = extraHours * (ratesF * 1.5)
        salaryPay = (40 * ratesF) + extraPay
    return salaryPay

p = computepay(hours, rateperhour)
print("Pay", p)

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done!")'''


largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)

smallest_so_far = None      # "None" is used as a flag value
# It is a data type of null class. It is used to say a variable is an empty data set.
print("Before", smallest_so_far)
for the_num in [9, 4, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("After", smallest_so_far)