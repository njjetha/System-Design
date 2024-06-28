class Observable:
    def __init__(self):
        self.observers=[]

    def add(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
    