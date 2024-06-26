
from Strategy.DriveStrategy import DriveStrategy
from Strategy.SportDriveStrategy import SportDriveStrategy
from Strategy.NormalDriveStrategy import NormalDriveStrategy
from Vehicle import Vehicle
class SportVehicle(Vehicle):
    def __init__(self,driveStrategy:DriveStrategy):
        super().__init__(driveStrategy)


if __name__=="__main__":
    c=SportVehicle(NormalDriveStrategy)
    c.drive()