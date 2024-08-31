
from LowLevelDesign.TicTacToe.models.Board import Board
from LowLevelDesign.TicTacToe.models.CellStatus import CellStatus
from LowLevelDesign.TicTacToe.models.PlayerType import PlayerType
from LowLevelDesign.TicTacToe.models.Symbol import Symbol

class Player:
    def __init__(self, name, symbol:Symbol, type:PlayerType) -> None:
        self.name = name
        self.symbol = symbol
        self.id = id
        self.type= type
    
    def decide_cell(self, board:Board):
        while True:
            row = int(input("Enter row:"))
            col = int(input("Enter col:"))

            if row >=0 and row<=board.board_size and col >=0 and col<=board.board_size:
                if board.grid[row][col] == CellStatus.EMPTY:
                    return board.grid[row][col]
            print("Invalid row or col or cell is filled")



