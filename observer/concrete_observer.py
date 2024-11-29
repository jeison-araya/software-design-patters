from observer import Observer
from publisher import Publisher

class ConcreteObserverA(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, publisher: Publisher):
        print(f'{self.name} received message: {publisher.get_state()}')


class ConcreteObserverB(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, publisher: Publisher):
        print(f'{self.name} received message: {publisher.get_state()}')


class ConcreteObserverC(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, publisher: Publisher):
        print(f'{self.name} received message: {publisher.get_state()}')
