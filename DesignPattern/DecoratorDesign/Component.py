from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_description(self):
        pass
    def get_damage(self):
        pass