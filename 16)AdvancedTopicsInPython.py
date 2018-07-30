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