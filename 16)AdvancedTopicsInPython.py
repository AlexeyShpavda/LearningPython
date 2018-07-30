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

print("### Omitting Indices ###")
to_five = ['A', 'B', 'C', 'D', 'E']

print(to_five[3:])
# prints ['D', 'E']

print(to_five[:2])
# prints ['A', 'B']

print(to_five[::2])
# print ['A', 'C', 'E']

print("### Reversing a List ###")
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])

print("### Stride Length ###")
to_one_hundred = [i for i in range(101)]

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

print("### Practice Makes Perfect ###")
to_21 = [i for i in range(1, 22)]
print(to_21)

odds = to_21[::2]
print(odds)

middle_third = to_21[7:14]
print(middle_third)

print("### Anonymous Functions ###")
my_list = [i for i in range(16)]
print(filter(lambda x: x % 3 == 0, my_list))

print("### Lambda Syntax ###")
languages = ["HTML", "CSS", "JavaScript", "Python"]
print(filter(lambda x: x == "Python", languages))