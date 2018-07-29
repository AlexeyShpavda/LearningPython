# Contents:
# is_even
# is_int
# digit_sum
# factorial
# is_prime
# reverse
# anti_vowel
# scrabble_score
# censor
# count
# purify
# product
# remove_duplicates
# median

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

print("### scrabble_score ###")
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        for leter in score:
            if letter == leter:
                total = total + score[leter]
    return total

print("### censor ###")
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    for i in words:
        if i == word:
            result += stars
        else:
            result += i
        result += ' '

    return result

print("### count ###")
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

print("### purify ###")
def purify(lst):
    result = []
    for elem in lst:
        if elem % 2 == 0:
            result.append(elem)
    return result

print("### product ###")
def product(list):
  total = 1
  for num in list:
    total = total * num
  return total

print("### remove_duplicates ###")
def remove_duplicates(inputlist):
    if inputlist == []:
        return []

    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]

    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)

    return outputlist

print("### median ###")
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        index = len(sorted_list) // 2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        index_1 = len(sorted_list) / 2 - 1
        index_2 = len(sorted_list) / 2
        mean = (sorted_list[index_1] + sorted_list[index_2]) / 2.0
        return mean

print(median([2, 4, 5, 9]))
