from enum import Enum

class Proof(Enum):
    ADHARCARD, DRIVING_LICENCE, PASSPORT, VOTERID =1,2,3,4

class SeatStatus(Enum):
    AVAILABLE, UNAVAILABLE = 1,2

class SeatSide(Enum):
    WINDOW, MIDDLE, CORNER =1,2,3