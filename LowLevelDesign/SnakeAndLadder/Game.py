import random
from Board import Snake, Ladder, Board, Cell
from collections import deque

class Player:
    def __init__(self,number,name):
        self.number=int(number)
        self.name=name


class Game:
    def initialize(self, snake, ladder, players):
       b=Board()
    
       for obj in range(snake):
           while True:
               start=random.randint(1,100)
               end=random.randint(1,100)
               if(start<end):
                   snakeObj=Snake(start,end)
                   print(start)
                   b.board[start].set_snake(snakeObj)
                   break
                   
       for obj in range(ladder):
           while True:
               start=random.randint(1,100)
               end=random.randint(1,100)
               if(start>end):
                   ladderObj=Ladder(start,end)
                   b.board[start].set_ladder(ladderObj)
                   break
       self.startGame(players, b)
        
    def startGame(self, players, board:Board):
        winner=False
        
        playerTurn=deque()
        for player in range(players):
            playerTurn.append(Player(1,player+1))
        while not winner:
            player=playerTurn.popleft()
            dice=random.randint(1,6)
            # print(dice)
            # print(f"Player Name {player.name}, {player.number+dice}")
            if player.number+dice>=100:
                winner=True
                print("Winner of Snake and Ladder Game is ",player.name)
                break
            elif board.board[player.number+dice].snake:
                player.number=board.board[player.number+dice].snake.end
            elif board.board[player.number+dice].ladder:
                player.number=board.board[player.number+dice].ladder.end
            else:
                player.number=player.number+dice
            playerTurn.append(player)

if __name__=='__main__':
    game=Game()
    game.initialize(4,4,2)

