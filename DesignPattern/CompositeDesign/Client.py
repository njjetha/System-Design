from Leaf import Leaf
from Composite import Composite


if __name__=="__main__":
    leaf1=Leaf('leaf1')
    leaf2=Leaf('leaf2')
    leaf3=Leaf('leaf3')

    c1=Composite('Composite1')
    c1.add(leaf1)
    c1.add(leaf2)

    c2=Composite('Composite2')
    c2.add(c1)
    # c2.add(leaf3)
    c2.operation()