print("### While you're here ###")
count = 0

if count < 10:
  print("Hello, I am an if statement and count is", count)

while count < 10:
  print("Hello, I am a while and count is", count)
  count += 1

print("### Condition ###")
loop_condition = True

while loop_condition:
  print("I am a loop")
  loop_condition = False

print("### While you're at it ###")
num = 1

while num <= 10:
  print(num ** 2)
  num += 1

print("### Simple errors ###")
choice = input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
  choice = input("Sorry, I didn't catch that. Enter again: ")

print("### Infinite loops ###")
count = 0
while count < 10:
  print(count)
  # Increment count
  count += 1

print("### Break ###")
count = 0

while True:
  print(count)
  count += 1
  if count >= 10:
    break

print("### While / else ###")
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")

print("### Your own while / else ###")
from random import randint

random_number = randint(1, 10)
guesses_left = 3

# Start your game!
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")

print("### For your health ###")
print("Counting...")

for i in range(20):
  print(i)

print("### For your hobbies ###")
hobbies = []

for num in range(3):
  hobby =  input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print(hobbies)

print("### For your strings ###")
thing = "spam!"

for c in thing:
  print(c)

word = "eggs!"

for character in word:
  print(character)

print("### For your A ###")
phrase = "A bird in the hand..."

for char in phrase:
  if char == "A" or char == 'a':
    print('X')
  else:
    print(char)

print

print("### For your lists ###")
numbers = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
  print(num)

for num in numbers:
  print(num ** 2)

print("### Looping over a dictionary ###")
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print(key, d[key])

print("### Counting as you go ###")
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index + 1, item)

print("### Multiple lists ###")
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  print(max(a, b))

print("### For / else ###")
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!')
    break
  print('A', f)
else:
  print('A fine selection of fruits!')

print("### Change it up ###")
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!')
  print('A', f)
else:
  print('A fine selection of fruits!')