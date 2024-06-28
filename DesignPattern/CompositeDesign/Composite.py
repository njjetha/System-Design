from Component import Component
from Leaf import Leaf

class Composite(Component):
    def __init__(self,name):
        self.name=name
        self.children=[]
    
    def add(self, component):
        self.children.append(component)
    
    def remove(self, component):
        self.children.remove(component)
    
    def operation(self):
        print(f"Composite: {self.name}")
        print(f"Children {self.name} length {len(self.children)}")
        for child in self.children:
            print (child.operation())
        return ""