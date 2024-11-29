from state import State
from context import Context


class NoCoinState(State):
    def __init__(self, machine: Context):
        self.machine = machine

    def insert_coin(self):
        print("Coin inserted.")
        self.machine.set_state(HasCoinState(self.machine))

    def eject_coin(self):
        print("No coin to eject.")

    def press_button(self):
        print("Insert a coin first.")

    def dispense(self):
        print("You need to pay first.")


class HasCoinState(State):
    def __init__(self, machine: Context):
        self.machine = machine

    def insert_coin(self):
        print("Coin already inserted.")

    def eject_coin(self):
        print("Coin ejected.")
        self.machine.set_state(NoCoinState(self.machine))

    def press_button(self):
        print("Button pressed. Dispensing item...")
        self.machine.set_state(DispensingState(self.machine))

    def dispense(self):
        print("Press the button to dispense.")


class DispensingState(State):
    def __init__(self, machine: Context):
        self.machine = machine

    def insert_coin(self):
        print("Please wait, dispensing in progress.")

    def eject_coin(self):
        print("Cannot eject coin while dispensing.")

    def press_button(self):
        print("Already dispensing.")

    def dispense(self):
        print("Item dispensed. Thank you!")
        self.machine.set_state(NoCoinState(self.machine))
