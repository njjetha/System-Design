from Room import Room
from User import User
class Inventory:
    def __init__(self):
        self.roomList=[]
        self.userList=[]
    def addRoom(self, room:Room):
        self.roomList.append(room)
    def addUser(self, user:User):
        self.userList.append(user)
    def getAllRoom(self):
        for room in self.roomList:
            print("room Details", room.getStatusOfRoom())