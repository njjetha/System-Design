from GamingComputer import GamingComputer
class Director:
    def __init__(self, gamingComputer:GamingComputer):
        self.computer = gamingComputer

    def construct(self, RAM, HardDisk, GPU, Processor):
        return self.computer.set_RAM(RAM).set_HardDisk(HardDisk).set_GPU(GPU).set_Processor(Processor).build()