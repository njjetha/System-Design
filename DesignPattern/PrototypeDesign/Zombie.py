from Monster import Monster
import copy

class Zombie(Monster):

    def __init__(self, health):
        self.health = health

    def attack(self):
        print("Attacking .........")
    
    def clone(self):
        return copy.deepcopy(self)
    