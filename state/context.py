from abc import ABC, abstractmethod
from state import State


class Context(ABC):

    @abstractmethod
    def set_state(self, state: State):
        pass

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
