from datetime import datetime
from flight import *
from User.passenger import *
from enum_class import *
from booking import *
from seats import *

class AircraftManagement:
    def __init__(self):
        self.booking = {}
        self.counter = 0
        self.flights:List[Flight] = []
        self.passangers = []
    
    def add_flight(self, flight:Flight):
        self.flights.append(flight)
        print(f"Flight added {flight.flightId}")

    def add_passanger(self, passenger:Passenger):
        self.passangers.append(passenger)
        print(f"Passanger added {passenger.name}")

    def bookFlight(self, passenger:Passenger, flight:Flight, seat):
        self.counter+=1
        book_tckt = Booking(self.counter, flight, passenger, seat)
        self.booking[passenger.name]=book_tckt
    
    def searchFligh(self, src, dest, date) -> List[Flight]:
        res = []
        for flight in self.flights:
            if flight.source == src and flight.destination == dest and flight.date.date() == date.date():
                res.append(flight)
        return res
    

if __name__ == "__main__":
    am = AircraftManagement()
    fligh1= Flight(123, "BOM", "IDR", datetime(2024,8,1,5,10), 1, 100)
    pass1= Passenger("Neeraj", "8435503268", "njetha@gmail.com", Proof.ADHARCARD, 15)
    am.add_flight(fligh1)
    am.add_passanger(pass1)
    flightDetails = am.searchFligh("BOM", "IDR", datetime(2024,8,1))
    for fl in flightDetails:
        print("List of FlightId",fl.flightId)
    if len(flightDetails):
        am.bookFlight(pass1, flightDetails[0], 10)
    



