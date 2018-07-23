print("### Introduction to Lists ###")
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"];

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])

print("### Access by Index ###")
numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")
print(numbers[1] + numbers[3])

print("### New Neighbors ###")
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena"
print(zoo_animals)

print("### Late Arrivals & List Length ###")
suitcase = []
suitcase.append("passport")
suitcase.append("sunglasses")
suitcase.append("camera")
suitcase.append("hat")

list_length = len(suitcase)

print("There are %d items in the suitcase." % (list_length))
print(suitcase)