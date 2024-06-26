from typing import Any


class Singelton(type):
    instance={}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls.instance:
            cls.instance[cls]=super(Singelton,cls).__call__(*args, **kwds)
        return cls.instance[cls]
    
class Wizard(metaclass=Singelton):
    def __init__(self,name):
        self.name=name

instance1=Wizard("Jhon")
instance2=Wizard("Jeff")

print(instance1.name, instance2.name)