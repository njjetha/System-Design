"""
Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.
"""

"""
The function animal_sound does not conform to the open-closed principle because it cannot be closed against new kinds of animals.
If we add a new animal, Snake, We have to modify the animal_sound function.
You see, for every new animal, a new logic is added to the animal_sound function. 
This is quite a simple example. When your application grows and becomes complex, 
you will see that the if statement would be repeated over and over again 
in the animal_sound function each time a new animal is added, all over the application.

"""


class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

if __name__=='__main__':
    animals=[
        Snake('snake')
    ]
    animal_sound(animals)