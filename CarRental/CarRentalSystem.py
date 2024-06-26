from abc import ABC
import datetime
from EnumClass import *
class CarRentalSystem():
    
    def __init__(self,name):
        self.__name=name
        self.__location=list()
        
    def add_new_location(self,location):
        carRentalLocation=CarRentalLocation(self.__name,location)
        self.__location.append(carRentalLocation)
    
    def view_all_location(self):
        for carRent in self.__location:
            print(carRent.get_location())


class CarRentalLocation():
    def __init__(self,name,location):
        self.__name=name
        self.__location=location
    def get_location(self):
        return self.__location
    # def list_vehicle(self)


class Vehicle(ABC):
    def __init__(self,licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage) :
        self.__licenceNumber=licenceNumber
        self.__vehicleId=vehicleId
        self.__passangerCapacity=passangerCapacity
        self.__status=status
        self.__manfacturingYear=manfacturingYear
        self.__mileage=mileage
    def getStatus(self):
        return self.__status
    def reserve_vehicle(self):
        self.__status=VehicleStatus.RESERVED
    def return_vehicle(self):
        self.__status=VehicleStatus.AVAILABLE
    def getVehicleId(self):
        return self.__vehicleId

class Car(Vehicle):
    def __init__(self, licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage):
        super().__init__(licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage)
        
class Van(Vehicle):
    def __init__(self, licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage):
        super().__init__(licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage)

class Truck(Vehicle):
    def __init__(self, licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage):
        super().__init__(licenceNumber, vehicleId, passangerCapacity, status, manfacturingYear, mileage)

class User:
    def __init__(self, name, age, licenceNo):
        self.name=name
        self.age=age
        self.licenceNo=licenceNo
    


class VeicleReservation:
    def __init__(self):
        self.status=ReservationStatus.ACTIVE
        self.creation=datetime.date.today()
    
    def reserveVehicle(self,user:User, vehicle:Vehicle):
        status=vehicle.getStatus()
        print(status)
        if status == VehicleStatus.AVAILABLE:
            vehicle.reserve_vehicle()
            print(f"{user.name} has reserved vehicle {vehicle.getVehicleId()}")
            return True
        return False
    

class VehicleInventory:
    
    def __init__(self):
        self.vehicleList=[]

    def addNewVehicle(self, vehicle:Vehicle):
        self.vehicleList.append(vehicle)


if __name__=="__main__":
    car1=Car("BDXX09TYLA","MP09CG5548",4,VehicleStatus.AVAILABLE,"2022","45km")
    user1=User("Neeraj",26,"ABC395YYXK")
    vehicleInventory=VehicleInventory()
    vehicleInventory.addNewVehicle(car1)
    reserve=VeicleReservation()
    reserve.reserveVehicle(user1,car1)

            

        


        


