from LowLevelDesign.TicTacToe.models.CellStatus import CellStatus


class Cell:
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player
        self.status = CellStatus.EMPTY
    
    def display(self):
        if self.status == CellStatus.EMPTY:
            print("| - |", end="")
        else:
            print(f"| {self.player.symbol.symbol} |", end="")