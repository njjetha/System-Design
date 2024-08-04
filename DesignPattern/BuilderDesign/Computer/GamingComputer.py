from BuilderComputer import BuilderComputer
from Computer import Computer

class GamingComputer(BuilderComputer):
    def __init__(self):
        self.RAM = None
        self.HardDisk = None
        self.GPU  = None
        self.Processor = None
        self.core = None
    
    def set_RAM(self, RAM):
        if RAM  < 16:
            raise ValueError("Insufficient RAM")
        self.RAM = RAM
        return self

    def set_HardDisk(self, HardDisk):
        if HardDisk < 1:
            raise ValueError("Insufficient HARDDISK")
        self.set_HardDisk = HardDisk
        return self
    
    def set_GPU(self, GPU):
        self.GPU = GPU
        return self
    
    def set_Processor(self, Processor):
        self.Processor = Processor
        return self

    def set_core(self, core):
        self.core = core


    def build(self):
        c =  Computer()
        c.set_HardDisk(self.HardDisk)
        c.set_GPU(self.GPU)
        c.set_Processor(self.Processor)
        c.set_RAM(self.RAM)
    