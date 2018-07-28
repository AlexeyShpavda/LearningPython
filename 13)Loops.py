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