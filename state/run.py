"""
Run state pattern
"""
from concrete_context import VendingMachine

if __name__ == "__main__":
    vending_machine = VendingMachine()

    vending_machine.insert_coin()
    vending_machine.press_button()
    vending_machine.dispense()

    vending_machine.insert_coin()
    vending_machine.eject_coin()

    vending_machine.press_button()
    vending_machine.dispense()
