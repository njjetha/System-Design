from Strategy.DriveStrategy import DriveStrategy
class Vehicle():
    def __init__(self, driveStrategy:DriveStrategy):
        self.driveStrategy=driveStrategy
    
    def drive(self):
        self.driveStrategy.drive()
    