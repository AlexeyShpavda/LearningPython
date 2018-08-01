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
