class Board:
    def __init__(self,width=3,height=3):
        self.board = [[False]*3,
                      [False]*3,
                      [False]*3]

    def as_str(self):
        rv = ''
        for row in self.board:
            rv += ''.join('.0'[c] for c in row)
            rv += '\n'
        return rv



test = Board()
print(test.as_str())