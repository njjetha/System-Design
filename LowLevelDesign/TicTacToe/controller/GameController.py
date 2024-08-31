class GameController:
    def __init__(self, gameService):
        self.gameService = gameService
    
    def start_game(self, size, player, winning_stg):
        return self.gameService.start_game(size, player, winning_stg)

    def display_board(self, game):
        self.gameService.display_game(game)
    
    def take_move(self, game):
        self.gameService.take_move(game)
    
    def undo_move(self, game):
        self.gameService.undo_move(game)