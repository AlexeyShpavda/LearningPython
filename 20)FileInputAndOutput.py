print("### See It to Believe It ###")
my_list = [i ** 2 for i in range(1, 11)]

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

print("### The open() Function ###")
my_file = open("output.txt", "r+")

print("### Writing ###")
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("writing.txt", "w")

for value in my_list:
    my_file.write(str(value) + "\n")

my_file.close()