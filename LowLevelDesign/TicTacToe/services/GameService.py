

from LowLevelDesign.TicTacToe.models.CellStatus import CellStatus
from LowLevelDesign.TicTacToe.models.Game import Game
from LowLevelDesign.TicTacToe.models.GameStatus import GameStatus


class GameService:

    def start_game(self, size, player, winning_stg):
        game =  Game().gameBuilder().set_dimension(size).set_player(player).set_winning_strategies(winning_stg).build()
        return game

    def display_game(self, game:Game):
        game.Board.print_board()

    def take_move(self, game:Game):
       current_payer = game.players[game.next_turn]
       cell = current_payer.decide_cell(game.Board)
       cell.player = current_payer
       cell.status = CellStatus.FILLED
       game.moves.append(cell)
       if self.check_winner(game, cell):
           game.gameStatus = GameStatus.COMPLETED
           game.winner = current_payer
       elif len(game.moves) == game.Board.board_size * game.Board.board_size:
            game.gameStatus = GameStatus.DRAW
       game.next_turn += 1
       game.next_turn = game.next_turn%len(game.players)
        

    def check_winner(self, game:Game, cell):
        return any(ws.check_winner(cell, game.Board) for ws in game.winning_stg)


    def undo_move(self, game:Game):
        if not game.moves:
            print("No moves left to move")
            return

        cell = game.moves.pop()

        for ws in game.winning_stg:
            ws.undo_handle(cell, game.Board)
        cell.status = CellStatus.EMPTY
        cell.player = None

        game.next_turn -= 1
        game.next_turn %= len(game.players)