from Channel import Channel
from IChannel import IChannel
from Customer import Customer

class ProxyChannel(IChannel):

    def __init__(self,customer:Customer):
        self.customer=customer
        self.channel=Channel()

    def provide_broadcast(self):
        customer_age=self.customer.get_age()
        if customer_age > 18:
            self.channel.provide_broadcast()
            print("The service is registered for servicing")
        else:
            print("Sorry, this service is not allowed for the customer under the age of 18")

proxyChannel=ProxyChannel(Customer(25   ))
proxyChannel.provide_broadcast()