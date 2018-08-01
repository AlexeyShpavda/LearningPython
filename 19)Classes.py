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
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

my_car = Car("DeLorean", "silver", 88)