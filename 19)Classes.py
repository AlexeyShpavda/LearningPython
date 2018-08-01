print("### Create an instance of a class ###")
# class Car(object):
#   pass
#
# my_car = Car()

print("### Class member variables ###")
class Car(object):
  condition = "new"

my_car = Car()

print(my_car.condition)