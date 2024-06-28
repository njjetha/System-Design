from User import User, Customer, Servant
from Inventory import *
from HotelEnum import *
from Logic import Logic
class BookingRoom:
    def bookRoom(self, user:User, room:int, inv:Inventory):
        if isinstance(user, Customer):
            logic=Logic()
            isAvailable=logic.searchRoom(inv, room)
            print("# of Rooms Available ",isAvailable)
            if len(isAvailable)>=room:
                print(f"Room is Available")
                self.callInvoice(room,isAvailable)
            else:
                print(f"Room is not Available")

    def callInvoice(self, room, roomListAva):
        total_cost=0
        for idx in range(room):
            total_cost+=roomListAva[idx].getPriceOfRoom()
        
        payStatus=self.callPayement(total_cost)
        if payStatus:
            for idx in range(room):
                roomListAva[idx].f(RoomStatus.RESERVED)


    
    def callPayement(self, total_cost):
        print(f"Total Payement to be made {total_cost}")
        return True
            


        

            
