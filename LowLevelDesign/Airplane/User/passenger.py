from User.user import User
from flight import Flight
class Passenger(User):
    def __init__(self, name, phone, email, proof, luggage:int):
        super().__init__(name, phone, email, proof)
        self.luggage = luggage
        self.flight = None
        self.seat = None
    
    def seat_alloted(self,seatNo):
        self.seat = seatNo
    
    def flightDetails(self, flight:Flight):
        self.flight = flight
