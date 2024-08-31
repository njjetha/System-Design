from LowLevelDesign.TicTacToe.helper.GameBuilder import GameBuilder
from LowLevelDesign.TicTacToe.models.Board import Board
from LowLevelDesign.TicTacToe.models.GameStatus import GameStatus


class Game:
    def __init__(self, dimension, player, winning_stg) :
        self.players = player
        self.winning_stg = winning_stg
        self.Board = Board(dimension)
        self.moves = []
        self.next_turn = 0
        self.winner = None
        self.gameStatus = GameStatus.INPROGRESS
    
    @staticmethod
    def gameBuilder():
        return GameBuilder()