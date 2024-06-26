from abc import ABC,abstractmethod
class Device(ABC):
    @abstractmethod
    def toggle_power(self):
        pass
    @abstractmethod
    def volume_up(self):
        pass
    @abstractmethod
    def volume_dwon(self):
        pass