from LowLevelDesign.TicTacToe.helper.Strategy.BotStgy.BotStgy import BotStgy
from LowLevelDesign.TicTacToe.models.CellStatus import CellStatus


class Easy(BotStgy):
    def decide_move(self, board):
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None