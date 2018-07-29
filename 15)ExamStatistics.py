print("### Print those grades ###")
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print(grade)

print_grades(grades)

print("### The sum of scores ###")
def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

print(grades_sum(grades))