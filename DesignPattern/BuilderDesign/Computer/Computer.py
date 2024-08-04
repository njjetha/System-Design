class Computer:
    def __init__(self) -> None:
        self.RAM = None
        self.HardDisk = None
        self.GPU  = None
        self.Processor = None
        self.core = None
        self.GraphicCard =  None
    
    def set_RAM(self, RAM):
        self.RAM = RAM
    
    def set_HardDisk(self, HardDisk):
        self.HardDisk = HardDisk

    def set_GPU(self, GPU):
        self.GPU = GPU

    def set_Processor(self, Processor):
        self.Processor = Processor

    def set_core(self, core):
        self.core = core

    def set_GraphicCard(self, GraphicCard):
        self.GraphicCard = GraphicCard