from MediatorInterface import MediatorInterface
from Component import Component
class ConcreteMediator(MediatorInterface):
    def __init__(self):
      self.participants=[]

    def add_participants(self,participant):
      self.participants.append(participant)
    
    def send_message(self, message, participant):
       for par in self.participants:
          if(par!=participant):
             par.recieve_message(message)
             