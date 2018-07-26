print("### List accessing ###")
n = [1, 3, 5]
print(n[0])

print("### List element modification ###")
n = [1, 3, 5]
n[1] = n[1] * 5
print(n)

print("### Appending to a list ###")
n = [1, 3, 5]
n.append(7)
print(n)

print("### Removing elements from lists ###")
n = [1, 3, 5]
n.pop(0)
# n.remove(1)
# del(n[0])
print(n)