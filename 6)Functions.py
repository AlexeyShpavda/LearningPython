# Contents:
# Function Junction
# Call and Response
# Parameters and Arguments
# Practice Makes Perfect
# Generic Imports
# Function Imports
# Universal Imports
# Here Be Dragons
# On Beyond Strings
# max()
# min()
# abs()
# type()
# Review: Functions
# Review: Modules
# Review: Built-In Functions

print("### Function Junction ###")
def spam():
  """Prints 'Eggs!'"""
  print("Eggs!")

spam()

print("### Call and Response ###")
def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print
    "%d squared is %d." % (n, squared)
    return squared

square(10)

print("### Parameters and Arguments ###")
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)

print("### Functions Calling Functions ###")
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

print("### Practice Makes Perfect ###")
def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

print("### Generic Imports ###")
import math
print(math.sqrt(25))

print("### Function Imports ###")
from math import sqrt
print(sqrt(25))

print("### Universal Imports ###")
from math import *
print(sqrt(25))

print("### Here Be Dragons ###")
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!

print("### On Beyond Strings ###")
def biggest_number(*args):
    print(max(args))
    return max(args)

def smallest_number(*args):
    print(min(args))
    return min(args)

def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print("### max() ###")
maximum = max(-1, 20, 13)
print(maximum)

print("### min() ###")
minimum = min(-1, 20, 13)
print(minimum)

print("### abs() ###")
absolute = abs(-42)
print(absolute)

print("### type() ###")
print(type(14))
print(type(1.4))
print(type('alex'))

print("### Review: Functions ###")
def shut_down(s):
  if(s == 'yes'):
    return "Shutting down"
  elif(s == 'no'):
    return "Shutdown aborted"
  else:
    return "Sorry"

print("### Review: Modules ###")
import math
print(math.sqrt(13689))

print("### Review: Built-In Functions ###")
def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"