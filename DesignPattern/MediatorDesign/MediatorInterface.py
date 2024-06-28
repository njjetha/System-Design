from abc import abstractmethod, ABC

class MediatorInterface(ABC):
    @abstractmethod
    def send_message(self,message,participants):
        pass