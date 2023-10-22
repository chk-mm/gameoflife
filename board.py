class Board:
    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.board = self.create_board(width, height)
        self.new_board = self.create_board(width, height)

    def create_board(self, width, height):
        board = []
        for i in range(height):
            board.append([False] * width)
        return board

    def __str__(self):
        s = ''
        for row in self.board:
            s += ''.join('.0'[i] for i in row)
            s += '\n'
        return s

    def place_cell(self, row, col):
        self.board[row][col] = True

    def next(self):
        for row in range(self.height):
            for col in range(self.width):
                n = self.get_num_neighbors(row, col)

                if self.board[row][col] is False:
                    if n == 3:
                        self.new_board[row][col] = True  # birth
                    else:
                        self.new_board[row][col] = False  # empty

                if self.board[row][col] is True:
                    if n == 2 or n == 3:
                        self.new_board[row][col] = True  # survive
                    else:
                        self.new_board[row][col] = False  # dead

        tmp = self.board
        self.board = self.new_board
        self.new_board = tmp

    def get_num_neighbors(self, row, col):
        counter = 0
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                if r == c and r == 0:
                    continue
                if self.is_alive(row + r, col + c):
                    counter += 1
        return counter

    def is_alive(self, row, col):
        if 0 <= row < self.height:
            if 0 <= col < self.width:
                return self.board[row][col]
        return False

    def toggle_cell(self, row, col):
        self.board[row][col] = True