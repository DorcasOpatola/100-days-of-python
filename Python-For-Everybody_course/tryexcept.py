astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
print("First", istr)
astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)
print("Done")


'''
The "try" and "except" function is used to avoid code crashing when an error is encountered.
You can use it to check if a user input is valid or not.
It can be used to check if a file exists or not before trying to open it.

Also, you can put your whole code in a try block, 
and if any error occurs, it will be caught by the except block.
'''


rawstring = input("Enter a number: ")
try:
    ival = int(rawstring)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print("Not a valid number")

print("Done")
