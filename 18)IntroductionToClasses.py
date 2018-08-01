print("### Class Syntax ###")
# class Animal(object):
#   pass

print("### Classier Classes ###")
# class Animal(object):
#   def __init__(self):
#     pass

print("### Let's Not Get Too Selfish ###")
# class Animal(object):
#   def __init__(self, name):
#     self.name = name

print("### Instantiating Your First Object ###")
# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#
# zebra = Animal("Jeffrey")
#
# print(zebra.name)

print("### More on __init__() and self ###")
# class Animal(object):
#   """Makes cute animals."""
#   def __init__(self, name, age, is_hungry):
#     self.name = name
#     self.age = age
#     self.is_hungry = is_hungry
#
# zebra = Animal("Jeffrey", 2, True)
# giraffe = Animal("Bruce", 1, False)
# panda = Animal("Chad", 7, True)
#
# print(zebra.name, zebra.age, zebra.is_hungry)
# print(giraffe.name, giraffe.age, giraffe.is_hungry)
# print(panda.name, panda.age, panda.is_hungry)

print("### Class Scope ###")
# class Animal(object):
#   """Makes cute animals."""
#   is_alive = True
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# zebra = Animal("Jeffrey", 2)
# giraffe = Animal("Bruce", 1)
# panda = Animal("Chad", 7)
#
# print(zebra.name, zebra.age, zebra.is_alive)
# print(giraffe.name, giraffe.age, giraffe.is_alive)
# print(panda.name, panda.age, panda.is_alive)

print("### A Methodical Approach ###")
# class Animal(object):
#     """Makes cute animals."""
#     is_alive = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         print(self.name)
#         print(self.age)
#
# hippo = Animal("Anderson", 36)
# hippo.description()

print("### They're Multiplying! ###")
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal('Anderson', 36)
sloth = Animal('Dale', 15)
ocelot = Animal('Fuzzy', 7)

print(hippo.health)
print(sloth.health)
print(ocelot.health)

print("### It's Not All Animals and Fruits ###")
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

my_cart = ShoppingCart("Eric")
my_cart.add_item("Ukelele", 10)

print("### Warning: Here Be Dragons ###")
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

print("### Inheritance Syntax ###")
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

print("### Override! ###")
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

print("### This Looks Like a Job For... ###")
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee('Milton')
print(milton.full_time_wage(10))

print("### Class Basics ###")
class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

print("### Class It Up ###")
class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False