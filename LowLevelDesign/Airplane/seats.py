from enum_class import SeatStatus
from threading import *
class Seats:
    
    
    def __init__(self,seatId) -> None:
        self.seatId = seatId
        self.status =  SeatStatus.AVAILABLE
        self.seatType = None

