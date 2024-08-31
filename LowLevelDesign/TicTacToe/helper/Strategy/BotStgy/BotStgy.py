from abc import ABC, abstractmethod


class BotStgy(ABC):
    @abstractmethod
    def decide_move(self, board):
        raise NotImplementedError
    
