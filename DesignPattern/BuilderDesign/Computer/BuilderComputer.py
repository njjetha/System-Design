from abc import ABC, abstractmethod
class BuilderComputer(ABC):
    @abstractmethod
    def set_RAM(self, RAM):
        pass
    @abstractmethod
    def set_HardDisk(self, HardDisk):
        pass
    @abstractmethod
    def set_GPU(self, GPU):
        pass
    @abstractmethod
    def set_Processor(self, Processor):
        pass
    @abstractmethod
    def set_core(self, core):
        pass