from abc import ABC, abstractmethod
class IChannel(ABC):
    @abstractmethod
    def provide_broadcast(self):
        pass