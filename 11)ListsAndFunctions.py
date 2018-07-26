print("### List accessing ###")
n = [1, 3, 5]
print(n[0])

print("### List element modification ###")
n = [1, 3, 5]
n[1] = n[1] * 5
print(n)

print("### Appending to a list ###")
n = [1, 3, 5]
n.append(7)
print(n)

print("### Removing elements from lists ###")
n = [1, 3, 5]
n.pop(0)
# n.remove(1)
# del(n[0])
print(n)

print("### Changing the functionality of a function ###")
number = 5
def my_function(x):
    return x * 3

print(my_function(number))

print("### More than one argument ###")
d = 14
m = 12
def add_function(num1, num2):
  return num1 + num2

print(add_function(d, m))

print("### Strings in functions ###")
word = 'Hello'
def string_function(s):
  return s + ' World'

print(string_function(word))

print("### Passing a list to a function ###")
def list_function(x):
    print(x)

n = [3, 5, 7]
list_function(n)

print("### Using an element from a list in a function ###")
def list_index_function(list, index):
    print(list[index])

n = [3, 5, 7]
list_index_function(n, 0)

print("### Modifying an element of a list in a function ###")
def list_modifying_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print(list_modifying_function(n))

print("### List manipulation in functions ###")
n = [3, 5, 7]
def list_extender(list):
  list.append(9)
  return list

print(list_extender(n))

print("### Printing out a list item by item in a function ###")
n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print(x[i])

print_list(n)

print("### Modifying each element in a list in a function ###")
n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print(double_list(n))

print("### Passing a range into a function ###")
n = [3, 5, 7]
def my_function(n, x):
  for i in range(0, x):
      print(n[i])

my_function(n, 3)

print("### Iterating over a list in a function ###")
n = [3, 5, 7]
def total(numbers):
  result = 0
  for i in range(0, len(numbers)):
    result += numbers[i]
  return result

print(total(n))

print("### Using strings in lists in functions ###")
n = ["Michael", "Lieberman"]
def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print(join_strings(n))