from typing import List
from command import Command


class CommandManager:
    def __init__(self):
        self.history: List[Command] = []

    def execute_command(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if not self.history:
            return
        command = self.history.pop()
        command.undo()
