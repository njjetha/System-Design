# from CharFactory import CharFactory
from Character import Character
character=[]
character.append(Character('A',12))
character.append(Character('B',20))

for ch in character:
    ch.render()