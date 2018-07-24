print("### BeFOR We Begin ###")
names = ["Alex", "Mariah", "Martine", "Columbus"]
for name in names:
  print(name)

print("### This is KEY! ###")
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
for word in webster:
  print(webster[word])

print("### Control Flow and Looping ###")
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
  if number % 2 == 0:
    print(number)

print("### Lists + Functions ###")
def fizz_count(list):
  count = 0
  for item in list:
    if item == "fizz":
      count = count + 1
  return count

list = ["fizz", "fizz", "fizz" , "x", "y", "z"]
print(fizz_count(list))

print("### String Looping ###")
for letter in "AlexeyShpavda":
    print(letter)

# Empty lines to make the output pretty
print()
print()

word = "alt"

for letter in word:
    # Only print out the letter i
    if letter == "a":
        print(letter)