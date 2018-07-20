print("### The datetime Library ###")
from datetime import datetime

print("### Getting the Current Date and Time ###")
now = datetime.now()
print(now)

print("### Extracting Information ###")
print(now.year)
print(now.month)
print(now.day)