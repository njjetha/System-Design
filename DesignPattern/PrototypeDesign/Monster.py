from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def clone(self):
        pass