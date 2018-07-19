print("### Hello World! ###")
print("Hello, world!")

print("### Print Statements ###")
print("Hello, Alex!")

print("### Strings ###")
print("Hello, " + "Python!")

print("### Handling Errors ###")
# print("How do you make a hot dog stand?')
print("How do you make a hot dog stand?")
# print(You take away its chair!)
print("You take away its chair!")

print("### Variables ###")
todays_date = "19.07.2018"
print(todays_date)

print("### Arithmetic ###")
mirthful_addition = 12381 + 91817
print(mirthful_addition)
amazing_subtraction = 981 - 312
print(amazing_subtraction)
trippy_multiplication = 38 * 902
print(trippy_multiplication)
happy_division = 540 / 45
print(happy_division)
sassy_combinations = 129 * 1345 + 120 / 6 - 12
print(sassy_combinations)

print("### Updating Variables ###")
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
annual_rainfall += september_rainfall

october_rainfall = 7.20
annual_rainfall += october_rainfall

november_rainfall = 5.06
annual_rainfall += november_rainfall

december_rainfall = 4.06
annual_rainfall += december_rainfall
print(annual_rainfall)

print("### Comments ###")
city_name = "Grodno"
print(city_name)
# inhabitants
city_pop = 365610
print(city_pop)

print("### Numbers ###")
cucumbers = 1
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)

print("### Two Types of Division ###")
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers/num_people
print(whole_cucumbers_per_person)

float_cucumbers_per_person = float(cucumbers)/num_people
print(float_cucumbers_per_person)

print("### Multi-line Strings ###")
haiku = """The old pond,
A frog jumps in:
Plop!"""
print(haiku)

print("### Booleans ###")
# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.
age_is_12 = False
print(age_is_12)
name_is_maria = True
print(name_is_maria)

print("### ValueError ###")
float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
big_string = "The product was " + str(product)

print("### Review ###")
skill_completed = "Python Syntax"
exercises_completed = 13
# The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise

print("I got " + str(point_total) + " points!")