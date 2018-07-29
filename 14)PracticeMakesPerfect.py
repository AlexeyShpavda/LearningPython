print("### is_even ###")
def is_even(x):
  if(x % 2 == 0):
    return True
  else:
    return False

print("### is_int ###")
def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print("### digit_sum ###")
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print(x)
    return total

print("### factorial ###")
def factorial(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total