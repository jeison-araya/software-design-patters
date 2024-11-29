"""
Run command pattern
"""
from command import Command
from concrete_commands import WriteCommand, DeleteCommand
from invoker import CommandManager
from text_editor import TextEditor


if __name__ == "__main__":
    text_editor = TextEditor()
    command_manager = CommandManager()

    write_command = WriteCommand(text_editor, "Hello ")
    command_manager.execute_command(write_command)

    assert text_editor.text == "Hello "

    write_command = WriteCommand(text_editor, "World!")
    command_manager.execute_command(write_command)

    assert text_editor.text == "Hello World!"

    delete_command = DeleteCommand(text_editor, 6)
    command_manager.execute_command(delete_command)

    assert text_editor.text == "Hello "

    write_command = WriteCommand(text_editor, "Python!")
    command_manager.execute_command(write_command)

    assert text_editor.text == "Hello Python!"

    command_manager.undo_last_command()

    assert text_editor.text == "Hello "
