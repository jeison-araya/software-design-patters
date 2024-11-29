from command import Command
from text_editor import TextEditor


class WriteCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.add_text(self.text)

    def undo(self):
        self.editor.remove_text(len(self.text))


class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, length: int):
        self.editor = editor
        self.length = length
        self.deleted_text = ''

    def execute(self):
        self.deleted_text = self.editor.remove_text(self.length)

    def undo(self):
        self.editor.add_text(self.deleted_text)
