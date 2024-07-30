from typing import List
from seats import *

class Flight:
    def __init__(self, flightId, source, destination, date, duration, seats):
        self.flightId = flightId
        self.source = source
        self.destination =destination
        self.date = date
        self.duration =duration
        self.seats = [Seats(seatId) for seatId in range(1,seats)]



