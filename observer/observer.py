from abc import ABC, abstractmethod
from publisher import Publisher

class Observer(ABC):
    @abstractmethod
    def update(self, publisher: Publisher) -> None:
        """
        Update the observer with a publisher.
        """
        pass
