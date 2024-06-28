from Iterator import Iterator
from ConcreteCollection import ConcreteCollection

if __name__=='__main__':
    cc=ConcreteCollection()
    cc.add(1)
    cc.add(2)
    cc.add(3)

    iterator=cc.create_iterator()
    for element in iterator:
        print(element)
