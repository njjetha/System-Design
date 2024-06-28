from HotelEnum import *
class Room:
    def __init__(self, ac, type, price, isSmoking, roomStatus=RoomStatus.AVAILABLE):
        self.__ac=ac
        self.__type=type
        self.__roomStatus=roomStatus
        self.__price=price
        self.__isSmoking=isSmoking
    
    def getStatusOfRoom(self):
        return self.__roomStatus
    
    def getPriceOfRoom(self):
        return self.__price
    
    def getSmokingStatus(self):
        return self.__isSmoking

    def setStatusOfRoom(self,roomStatus):
        self.__roomStatus=roomStatus



    

        