from typing import List
from publisher import Publisher
from observer import Observer


class ConcretePublisher(Publisher):
    _state: str = None
    _observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        """
        Subscribe an observer to the publisher.
        """
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        """
        Unsubscribe an observer from the publisher.
        """
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Notify all observers of the event.
        """
        for observer in self._observers:
            observer.update(self)

    def set_state(self, state) -> None:
        print(f'Publisher: Setting state to {state}')
        self._state = state
        self.notify()

    def get_state(self) -> str:
        return self._state
