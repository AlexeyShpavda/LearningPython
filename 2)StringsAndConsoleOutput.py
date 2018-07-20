print("### Strings ###")
name = "Alex"
age = "19"
city = "Grodno"

print("### Practice ###")
caesar = "Graham"
praline = "John"
viking = "Teresa"

print(caesar)
print(praline)
print(viking)

print("### Escaping characters ###")
# print('This isn't flying, this is falling with style!')
print('This isn\'t flying, this is falling with style!')

print("### Access by Index ###")
fifth_letter = "MONTY"[4]
print(fifth_letter)

print("### String methods ###")
parrot = "Norwegian Blue"
print(parrot)
print(len(parrot))
print(parrot.lower())
print(parrot.upper())


print("### str() ###")
pi = 3.14
print(str(pi))

print("### Printing Strings ###")
print("Monty Python")

print("### Printing Variables ###")
the_machine_goes = "Ping!"
print(the_machine_goes)

print("### String Concatenation ###")
print("Spam " + "and " + "eggs")

print("### Explicit String Conversion ###")
print("The value of pi is around " + str(3.14))

print("### String Formatting with %, Part 1 ###")
month = 7
print("%s - 20 - 2018" % (month))
print("%02d - 20 - 2018" % (month))

print("### String Formatting with %, Part 2 ###")
name = input("What is your name? ")
color = input("What is your favorite color? ")
print("Ah, so your name is %s, " \
"and your favorite color is %s." % (name, color))