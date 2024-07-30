from User.passenger import *
from flight import *
from enum_class import *
class Booking:
    def __init__(self, bookingId, flight: Flight, passenger:Passenger, seatNo) -> None:
        self.bookingId = bookingId
        self.flight = flight
        self.passenger = passenger
        self.selectSeat(flight, passenger, seatNo)
    
    def selectSeat(self,flight:Flight, passenger:Passenger, seatNo):
        if flight.seats[seatNo].status == SeatStatus.AVAILABLE:
            flight.seats[seatNo].status = SeatStatus.UNAVAILABLE
            passenger.seat_alloted(seatNo)
            passenger.flightDetails(flight)
            print(f"Booking Successful for Passenger {passenger.name} for flightNo. {flight.flightId} src {flight.source} to dest {flight.destination} on seatNo. {seatNo}")
            return seatNo
        print(f"Booking unsuccessful due to seat not available selected")
        return None
    