from ConcreteMediator import ConcreteMediator
from Component import Component

class Client:
  mediator=ConcreteMediator()

  c1=Component(mediator,"participant1")
  c2=Component(mediator,"participant2")

  mediator.add_participants(c1)
  mediator.add_participants(c2)


  c1.send_message("Hello from participant1")
