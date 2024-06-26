from Inventory import Inventory
from HotelEnum import *
class Logic:
    def __init__(self) -> None:
        pass
    def searchRoom(self, inv:Inventory, rooms:int) -> []:
        # cnt=0
        availRoomList=[]
        for room in inv.roomList:
            # print(room.getStatusOfRoom())
            if room.getStatusOfRoom() == RoomStatus.AVAILABLE:

                availRoomList.append(room)  
        return availRoomList
    

        
