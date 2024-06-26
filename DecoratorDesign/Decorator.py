from abc import ABC, abstractmethod

class CharacterDecorator(ABC):
    def __init__(self,character):
        self._character=character
    @abstractmethod
    def get_description(self):
        pass
    def get_damage(self):
        pass
