def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Wizard:
    def __init__(self, name):
        self.name = name

instance1=Wizard("Jhon")
instance2=Wizard("Jeff")

print(instance1.name, instance2.name)