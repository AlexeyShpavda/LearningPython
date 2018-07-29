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

print("### is_prime ###")
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x / 2):
            if x % n == 0:
                return False
        return True

print("### reverse ###")
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

print("### anti_vowel ###")
def anti_vowel(text):
    t = ""
    for c in text:
        for i in "ieaouIEAOU":
            if c == i:
                c = ""
            else:
                c = c
        t = t + c
    return t