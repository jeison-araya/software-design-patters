from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def eject_coin(self):
        pass

    @abstractmethod
    def press_button(self):
        pass

    @abstractmethod
    def dispense(self):
        pass