from LowLevelDesign.TicTacToe.models.Cell import Cell


class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.grid = [[Cell(i,j) for j in range(self.board_size)]for i in range(self.board_size)]

    def print_board(self):
        for row in self.grid:
            for cell in row:
                cell.display()
            print()