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