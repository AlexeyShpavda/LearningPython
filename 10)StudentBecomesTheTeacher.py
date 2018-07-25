print("### Lesson Number One ###")
# lloyd = {
#   "name" : "Lloyd",
#   "homework" : [],
#   "quizzes" : [],
#   "tests" : []
# }
#
# alice = {
#   "name" : "Alice",
#   "homework" : [],
#   "quizzes" : [],
#   "tests" : []
# }
#
# tyler = {
#   "name" : "Tyler",
#   "homework" : [],
#   "quizzes" : [],
#   "tests" : []
# }

print("### What's the Score? ###")
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

print("### Put It Together ###")
students = [lloyd, alice, tyler]

print("### For the Record ###")
for student in students:
  print(student["name"])
  print(student["homework"])
  print(student["quizzes"])
  print(student["tests"])

print("### It's Okay to be Average ###")
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

print("### Just Weight and See ###")
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

    total = homework * .1 + quizzes * .3 + tests * .6
    return total