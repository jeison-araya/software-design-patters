"""
Run Observer pattern example.
"""

from concrete_observer import ConcreteObserverA, ConcreteObserverB, ConcreteObserverC
from concrete_publisher import ConcretePublisher

if __name__ == '__main__':
    publisher = ConcretePublisher()

    observer_a = ConcreteObserverA('Observer A')
    observer_b = ConcreteObserverB('Observer B')
    observer_c = ConcreteObserverC('Observer C')

    publisher.subscribe(observer_a)
    publisher.subscribe(observer_b)
    publisher.subscribe(observer_c)

    publisher.set_state('New State')
    publisher.set_state('Another State')

    publisher.unsubscribe(observer_b)

    publisher.set_state('Final State')
