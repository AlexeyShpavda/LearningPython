# Contents:
# The datetime Library
# Getting the Current Date and Time
# Extracting Information
# Hot Date
# Pretty Time
# Grand Finale

print("### The datetime Library ###")
from datetime import datetime

print("### Getting the Current Date and Time ###")
now = datetime.now()
print(now)

print("### Extracting Information ###")
print(now.year)
print(now.month)
print(now.day)

print("### Hot Date ###")
# print the current date as mm/dd/yyyy
print('%02d/%02d/%04d' % (now.month, now.day, now.year))

print("### Pretty Time ###")
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

print("### Grand Finale ###")
print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))