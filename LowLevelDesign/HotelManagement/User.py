from Room import Room
from HotelEnum import *
class User:
    def __init__(self, name:str, age:int, phone:str, email):
        self.__name=name
        self.__age=age
        self.__phone=phone
        self.__email=email
    

class Customer(User):
    def __init__(self, name, age, phone, email, familyMembers:int, rooms:int):
        super().__init__(name, age, phone, email)
        self.familyMembers=familyMembers
        self.rooms=rooms
    

    
class Receptionist(User):
    def isUserExist(user:User):
        pass
    def roomBooking(user:Customer):
        pass


class Servant(User):
    def cleaningRoom(room:Room):
        room.setStatus=RoomStatus.CLEANING
        print(f"Cleaning Room")
        room.setStatusOfRoom=RoomStatus.AVAILABLE
