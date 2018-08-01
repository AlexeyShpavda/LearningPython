print("### Create an instance of a class ###")
# class Car(object):
#   pass
#
# my_car = Car()

print("### Class member variables ###")
# class Car(object):
#   condition = "new"
#
# my_car = Car()
#
# print(my_car.condition)

print("### Initializing a class ###")
# class Car(object):
#   condition = "new"
#   def __init__(self, model, color, mpg):
#     self.model = model
#     self.color = color
#     self.mpg = mpg
#
# my_car = Car("DeLorean", "silver", 88)

print("### Referring to member variables ###")
# class Car(object):
#   condition = "new"
#   def __init__(self, model, color, mpg):
#     self.model = model
#     self.color = color
#     self.mpg = mpg
#
# my_car = Car("DeLorean", "silver", 88)
#
# print(my_car.model)
# print(my_car.color)
# print(my_car.mpg)

print("### Creating class methods ###")
# class Car(object):
#     condition = "new"
#
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#
#     def display_car(self):
#         print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
#
# my_car = Car("DeLorean", "silver", 88)
#
# my_car.display_car()

print("### Modifying member variables ###")
class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)