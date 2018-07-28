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
