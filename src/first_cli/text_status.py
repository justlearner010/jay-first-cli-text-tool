from dataclasses import dataclass
@dataclass(init=True)


class TextStats:
    
    def __init__(self,text):
        self.text = text

    
    def space_check(self):
        return sum(char.isspace() for char in self.text)

    def line_check(self):
        return len(self.text.splitlines())
    

    def word_check(self):
        return len(self.text.split())
    

    def digit_check(self):
        return sum(char.isdigit() for char in self.text)

    =
