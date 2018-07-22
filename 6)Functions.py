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