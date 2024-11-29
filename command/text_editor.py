class TextEditor:
    def __init__(self):
        self.text = ""

    def add_text(self, new_text):
        self.text += new_text
        print(f"Current Text: {self.text}")

    def remove_text(self, length):
        removed_text = self.text[-length:]
        self.text = self.text[:-length]
        print(f"Current Text: {self.text}")
        return removed_text
