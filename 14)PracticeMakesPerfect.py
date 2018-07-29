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