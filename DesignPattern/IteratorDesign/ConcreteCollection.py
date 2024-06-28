from IteratorCollection import IteratorCollection
from ConcreteIterator import ConcreteIterator
class ConcreteCollection(IteratorCollection):
    def __init__(self):
        self.data=[]
    def add(self,value):
        self.data.append(value)
    def create_iterator(self):
        return ConcreteIterator(self.data)
    