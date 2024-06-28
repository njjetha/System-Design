class Component:
    def __init__(self,mediator,name):
        self.mediator=mediator
        self.name=name
    
    def send_message(self,message):
        self.mediator.send_message(message,self)
    
    def recieve_message(self,message):
        print(f"{self.name} recieved message: {message}")