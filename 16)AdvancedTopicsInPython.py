print("### Iterators for Dictionaries ###")
my_dict = {
  'name': 'Alex',
  'age':  19,
  'city': 'Grodno',
}

print(my_dict.items())

print("### keys() and values() ###")
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print(my_dict.keys())
print(my_dict.values())

print("### The 'in' Operator ###")
my_dict = {
  'name': 'Max',
  'age':  19,
  'auto': 'Audi',
}

for key in my_dict:
  print(key, my_dict[key])

print("### Building Lists ###")
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

print("### List Comprehension Syntax ###")
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print(doubles_by_3)

even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print(even_squares)

print("### Now You Try! ###")
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print(cubes_by_four)

print("### List Slicing Syntax ###")
l = [i ** 2 for i in range(1, 11)]

print(l[2:9:2])