# Contents:
# Getting Our Feet Wet
# Make a List
# Check it Twice
# Custom Print
# Printing Pretty
# Hide...
# ...and Seek!
# You win!
# Danger, Will Robinson!!!
# Bad Aim
# Not Again!
# Play It, Sam
# Game Over
# A Real Win

print("### Getting Our Feet Wet ###")
board = []

print("### Make a List ###")
for i in range(5):
  board.append(['O'] * 5)

print("### Check it Twice ###")
# for i in board:
#   print(i)

print("### Custom Print ###")
# def print_board(board_in):
#     for row in board_in:
#         print(row)
#
# print_board(board)

print("### Printing Pretty ###")
def print_board(board_in):
    for row in board_in:
        print(" ".join(row))

print_board(board)

print("### Hide... ###")
from random import randint

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

print("### ...and Seek! ###")
# guess_row = int(input("Guess Row: "))
# guess_col = int(input("Guess Col: "))

print("### You win! ###")
# if guess_row == ship_row and guess_col == ship_col:
#   print("Congratulations! You sank my battleship!")

print("### Danger, Will Robinson!!! ###")
# if guess_row == ship_row and guess_col == ship_col:
#   print("Congratulations! You sank my battleship!")
# else:
#   print("You missed my battleship!")
#   board[guess_row][guess_col] = "X"
#   print_board(board)

print("### Bad Aim ###")
# if guess_row == ship_row and guess_col == ship_col:
#   print("Congratulations! You sank my battleship!")
# else:
#   if guess_row not in range(5) or \
#     guess_col not in range(5):
#     print("Oops, that's not even in the ocean.")
#   else:
#     print("You missed my battleship!")
#     board[guess_row][guess_col] = "X"
#   print_board(board)

print("### Not Again! ###")
# if guess_row == ship_row and guess_col == ship_col:
#   print("Congratulations! You sank my battleship!")
# else:
#   if guess_row not in range(5) or \
#     guess_col not in range(5):
#     print("Oops, that's not even in the ocean.")
#   elif (board[guess_row][guess_col] == 'X'):
#     print("You guessed that one already.")
#   else:
#     print("You missed my battleship!")
#     board[guess_row][guess_col] = "X"
#   print_board(board)

print("### Play It, Sam ###")
# for turn in range(4):
#   print("Turn", turn + 1)
#   guess_row = int(input("Guess Row: "))
#   guess_col = int(input("Guess Col: "))
#
#   if guess_row == ship_row and guess_col == ship_col:
#     print("Congratulations! You sank my battleship!")
#   else:
#     if guess_row not in range(5) or \
#       guess_col not in range(5):
#       print("Oops, that's not even in the ocean.")
#     elif board[guess_row][guess_col] == "X":
#       print("You guessed that one already.")
#     else:
#       print("You missed my battleship!")
#       board[guess_row][guess_col] = "X"
#     print_board(board)

print("### Game Over ###")
# for turn in range(4):
#   print("Turn", turn + 1)
#   guess_row = int(input("Guess Row: "))
#   guess_col = int(input("Guess Col: "))
#
#   if guess_row == ship_row and guess_col == ship_col:
#     print("Congratulations! You sank my battleship!")
#   else:
#     if guess_row not in range(5) or \
#       guess_col not in range(5):
#       print("Oops, that's not even in the ocean.")
#     elif board[guess_row][guess_col] == "X":
#       print("You guessed that one already.")
#     else:
#       print("You missed my battleship!")
#       board[guess_row][guess_col] = "X"
#     if (turn == 3):
#       print("Game Over")
#     print_board(board)

print("### A Real Win ###")
for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print("Game Over")
    print_board(board)