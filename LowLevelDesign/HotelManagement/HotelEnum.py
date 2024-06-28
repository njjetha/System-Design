from enum import Enum

class RoomStatus(Enum):
    AVAILABLE, OCCUPIED, RESERVED, CLEANING = 1, 2, 3,4

class RoomType(Enum):
    STANDARD, DELUX, FAMILY = 1,2,3