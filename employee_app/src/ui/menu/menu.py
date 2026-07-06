from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def open():
        ...
    
    @abstractmethod
    def _exit():
        ...