'''
SUBROUTINES IN PYTHON

- a block of reusable code with the 'def' keyword is called "FUNCTION".
- a block of reusable code with the 'class' keyword is called "CLASS".

A subroutine is a set of instructions designed to perform a frequently used operation within a program.
In Python, subroutines are implemented using functions, I.E., the def keyword.
Functions can take inputs, called parameters, and can return outputs using the return statement.

Example: Create a function that generates a random pin number of a given length --- here, it is 5.
'''

#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = ""  #this is the empty string
  for i in range(number):  #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9))  #we want a string of random numbers between 0-9
  return pin

myPin = pinPicker(5)  #5 means we want 5 random numbers
print(myPin)


'''
SCOPE is a variable only available from inside the region it was created.
Variables that are created for the first time in a subroutine are only available inside that subroutine.
We cannot call the variable area outside the subroutine.
We need to create the variable area inside the subroutine.
'''
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
# print(area) #This will raise an error because 'area' is not defined outside the function.
#To fix the error, we can print the area inside the function or return it and print it outside.

peace = areaOfTriangle (5, 22)
print(peace) #This will work because we are printing the returned value of the function.
