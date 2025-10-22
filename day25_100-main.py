'''
SUBROUTINES IN PYTHON

A subroutine is a set of instructions designed to perform a frequently used operation within a program.
In Python, subroutines are implemented using functions, I.E., the def keyword.
Functions can take inputs, called parameters, and can return outputs using the return statement.

Example: Create a function that generates a random pin number of a given length --- here, it is 5.
'''

def pinPicker(number):
  import random
  pin = ""
  for i in range(number):
    pin += str(random.randint(0,9))
  return pin

myPin = pinPicker(5)
print(myPin)
