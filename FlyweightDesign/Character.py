# from Character import Character
from CharFactory import  CharFactory

class Character:
    def __init__(self, char, font_Size):
        self.char_flyweight=CharFactory.get_char(char)
        self.font_Size=font_Size
    
    def render(self):
        print(f"Character: {self.char_flyweight.char}, Font_Size:{self.font_Size}")