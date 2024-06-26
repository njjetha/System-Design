class User:
    def __init__(self, name, address):
        self.name=name
        self.address=address
        self.order=[]

class Item:
    def __init__(self, cost, type, vno):
        self.cost=cost
        self.paymentstatus=False
        self.vehicle=Vehicle(type, vno)

class Vehicle:
    def __init__(self, type, vno):
        self.type=type
        self.vno=vno

class Order:
    def __init__(self):
        self.users={}
    
    def add_item(self, name, address,cost, type, vno):
        user=self.users[name]
        if not user:
            self.users[name]=User(name, address)
        self.users[name].order.append(Item(cost, type, vno))
    
    
    

