from CharFlyWeight import CharFlyWeight

class CharFactory:
    char_flyweight={}

    @staticmethod
    def get_char(char):
        if char not in CharFactory.char_flyweight:
            CharFactory.char_flyweight[char]=CharFlyWeight(char)
        return CharFactory.char_flyweight[char]
    