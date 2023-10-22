from board import Board

board = Board(3, 3)

# init
board.place_cell(0, 1)
board.place_cell(1, 1)
board.place_cell(2, 1)

# start
board.next()

print(board)