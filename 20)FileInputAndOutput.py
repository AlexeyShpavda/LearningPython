print("### See It to Believe It ###")
my_list = [i ** 2 for i in range(1, 11)]

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

print("### The open() Function ###")
my_file = open("output.txt", "r+")

