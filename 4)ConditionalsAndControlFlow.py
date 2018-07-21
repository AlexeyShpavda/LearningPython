print("### Compare Closely! ###")
# Assign True or False as appropriate on the lines below!
# True if 17 < 328 or to False if it is not.
bool_one = True
print(bool_one)
# True if 100 == (2 * 50) or to False otherwise.
bool_two = True
print(bool_two)
# True if 19 <= 19 or to False if it is not.
bool_three = True
print(bool_three)
# True if -22 >= -18 or to False if it is not.
bool_four = False
print(bool_four)
# True if 99 != (98 + 1) or to False otherwise.
bool_five = False
print(bool_five)

print("### Compare... Closelier! ###")
# Assign True or False as appropriate on the lines below!
# (20 - 10) > 15
bool_one = False
print(bool_one)
# (10 + 17) == 3**16
bool_two = False
print(bool_two)
# 1**2 <= -1
bool_three = False
print(bool_three)
# 40 * 4 >= -4
bool_four = True
print(bool_four)
# 100 != 10**2
bool_five = False
print(bool_five)

print("### How the Tables Have Turned ###")
# Create comparative statements as appropriate on the lines below!
# Make me true!
bool_one = 3 < 5
print(bool_one)
# Make me false!
bool_two = 99 == "a"
print(bool_two)
# Make me true!
bool_three = 99 / 3 <= 45
print(bool_three)
# Make me false!
bool_four = "hello" != "hello"
print(bool_four)
# Make me true!
bool_five = "alex" == "alex"
print(bool_five)

print("### And ###")
bool_one = False and False
print(bool_one)
bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5
print(bool_two)
bool_three = 19 % 4 != 300 / 10 / 10 and False
print(bool_three)
bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2
print(bool_four)
bool_five = True and True
print(bool_five)

print("### Or ###")
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
print(bool_one)
bool_two = True or False
print(bool_two)
bool_three = 100**0.5 >= 50 or False
print(bool_three)
bool_four = True or True
print(bool_four)
bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
print(bool_five)

print("### Not ###")
bool_one = not True
print(bool_one)
bool_two = not 3**4 < 4**3
print(bool_two)
bool_three = not 10 % 3 <= 10 % 2
print(bool_three)
bool_four = not 3**2 + 4**2 != 5**2
print(bool_four)
bool_five = not not False
print(bool_five)

print("### This and That (or This, But Not That!) ###")
bool_one = False or not True and True
print(bool_one)
bool_two = False and not True or True
print(bool_two)
bool_three = True and not (False or False)
print(bool_three)
bool_four = not not True or False and not True
print(bool_four)
bool_five = False or not (True and True)
print(bool_five)

print("### Mix 'n' Match ###")
# Use boolean expressions as appropriate on the lines below!
# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"
print(bool_one)
# Make me true!
bool_two = True and True
print(bool_two)
# Make me false!
bool_three = False and True
print(bool_three)
# Make me true!
bool_four = not False
print(bool_four)
# Make me true!
bool_five = True or True
print(bool_five)

print("### Conditional Statement Syntax ###")
answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

print("### If You're Having... ###")
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print(using_control_once())
print(using_control_again())

print("### Else Problems, I Feel Bad for You, Son... ###")
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False

print("### I Got 99 Problems, But a Switch Ain't One ###")


def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))