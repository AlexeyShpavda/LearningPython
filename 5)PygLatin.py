print("### Ahoy! (or Should I Say Ahoyay!) ###")
print("Pig Latin")

print("### Input! ###")
original = input("Enter a word: ")

print("### Check Yourself! ###")
# if len(original) > 0:
#   print(original)
# else:
#   print("empty")

print("### Check Yourself... Some More ###")
if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")
