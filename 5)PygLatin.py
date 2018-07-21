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
# if len(original) > 0 and original.isalpha():
#   print(original)
# else:
#   print("empty")

print("### Ay B C ###")
pyg = 'ay'

print("### Word Up ###")
# if len(original) > 0 and original.isalpha():
#   word = original.lower()
#   first = word[0]
# else:
#     print('empty')

print("### Move it on Back ###")
# if len(original) > 0 and original.isalpha():
#   word = original.lower()
#   first = word[0]
#   new_word = word + first + pyg
# else:
#     print('empty')

print("### Ending Up ###")
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print('empty')
