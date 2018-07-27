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