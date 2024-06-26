from Component import Character
from ConcreteComponent import BasicCharacter
from Decorator import CharacterDecorator
from ConcreteDecorator import DoubleDamageDecorator, FireballDecorator, InvisibilityDecorator

if __name__=="__main__":
    char=BasicCharacter()
    print(char.get_description())

    ddd=DoubleDamageDecorator(char)
    print(ddd.get_description()," ", ddd.get_damage())


    xyc=DoubleDamageDecorator(FireballDecorator(InvisibilityDecorator(BasicCharacter())))
    print(xyc.get_description()," ", xyc.get_damage())