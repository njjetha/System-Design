from LowLevelDesign.TicTacToe.models.Board import Board
from LowLevelDesign.TicTacToe.models.PlayerType import PlayerType
from LowLevelDesign.TicTacToe.models.Players import Player
from LowLevelDesign.TicTacToe.models.Symbol import Symbol


class Bot(Player):
    def __init__(self, name, symbol: Symbol, type: PlayerType, difficulty) -> None:
        super().__init__(name, symbol, PlayerType.BOT)
        self.difficulty = difficulty

    def decide_cell(self, board: Board):
        return super().decide_cell(board)