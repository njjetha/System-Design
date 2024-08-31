from LowLevelDesign.TicTacToe.CustomException.PlayerException import PlayerException
from LowLevelDesign.TicTacToe.models.Game import Game


class GameBuilder:
    def __init__(self):
        self.dimension = None
        self.player = None
        self.winning_strategies = None

    def set_dimension(self, dimension):
        self.dimension = dimension
        return self
    
    def set_player(self, player):
        self.player = player
        return self

    def set_winning_strategies(self, winning_strategies):
        self.winning_strategies = winning_strategies
        return self
    
    def validate(self):
        if len(self.player) > self.dimension:
            raise PlayerException()
    
    def build(self):
        self.validate()
        return Game(self.dimension, self.player, self.winning_strategies)
