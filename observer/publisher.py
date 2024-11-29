from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber) -> None:
        """
        Subscribe a subscriber to the publisher.
        """
        pass

    @abstractmethod
    def unsubscribe(self, subscriber) -> None:
        """
        Unsubscribe a subscriber from the publisher.
        """
        pass

    @abstractmethod
    def notify(self, message) -> None:
        """
        Notify all subscribers of the event.
        """
        pass

    @abstractmethod
    def set_state(self, state) -> None:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass
