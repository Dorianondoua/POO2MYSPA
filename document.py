from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def __str__(self):
        pass

