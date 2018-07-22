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