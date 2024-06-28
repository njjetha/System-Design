from Room import Room
from User import *
from Inventory import Inventory
from HotelEnum import *
from BookingRoom import BookingRoom
if __name__=="__main__":
    invObj=Inventory()
    room1=Room(True,RoomType.DELUX, 3000, True)
    room2=Room(False, RoomType.FAMILY, 2000, False)
    invObj.addRoom(room1)
    invObj.addRoom(room2)
    user1=Customer("Neeraj", 25, "8435503268", "njjetha123@gmail.com",4,2)
    invObj.getAllRoom()
    invObj.addUser(user1)
    br=BookingRoom()
    br.bookRoom(user1, user1.rooms, invObj)