from concrete_states import NoCoinState
from context import Context


class VendingMachine(Context):
    def __init__(self):
        self.state = NoCoinState(self)

    def set_state(self, state: Context):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def press_button(self):
        self.state.press_button()

    def dispense(self):
        self.state.dispense()
