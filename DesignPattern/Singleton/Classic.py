class Singleton:
    instance=None
    def __new__(cls):
        if cls.instance is None:
            cls.instance=super(Singleton, cls).__new__(cls)
        return cls.instance
    

# Doesn't suport MultiThreading
# Lazy intialization , even though class is imported or accessed it immediately create a instance
# Inheritance not possible
instance1=Singleton()
print(type(instance1))
instance2=Singleton()
if instance1 is instance2:
    print("True")
else:
    print("False")
