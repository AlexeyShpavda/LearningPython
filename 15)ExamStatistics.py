# Contents:
# Print those grades
# The sum of scores
# Computing the Average
# The Variance
# Standard Deviation

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

print("### Computing the Average ###")
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

print(grades_average(grades))

print("### The Variance ###")
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

print(grades_variance(grades))

print("### Standard Deviation ###")
def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print(grades_std_deviation(variance))