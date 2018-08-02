print("### See It to Believe It ###")
my_list = [i ** 2 for i in range(1, 11)]

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

print("### The open() Function ###")
# my_file = open("output.txt", "r+")

print("### Writing ###")
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("writing.txt", "w")

for value in my_list:
    my_file.write(str(value) + "\n")

my_file.close()

print("### Reading ###")
my_file = open("writing.txt", "r")
print(my_file.read())
my_file.close()

print("### Reading Between the Lines ###")
my_file = open("writing.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()

print("### PSA: Buffering Data ###")
write_file = open("text.txt", "w")

read_file = open("text.txt", "r")

write_file.write("Not closing files is VERY BAD.")

write_file.close()

print(read_file.read())

read_file.close()

print("### The 'with' and 'as' Keywords ###")
with open("textAS.txt", "w") as textfile:
  textfile.write("Success!")