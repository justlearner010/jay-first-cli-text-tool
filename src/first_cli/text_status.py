from dataclasses import dataclass
@dataclass(init=True)


class TextStats:
    fname:str


    def space_check(self):
        space_cnt = 0
        with open(self.fname,"r") as f:
            for line in f:
                for word in line:
                    if(word.isspace()):
                        space_cnt += 1
        return space_cnt

    def line_check(self):
        lines = 0
        with open(self.fname,"r") as file:
            for line in file:
                lines = lines+1

        return lines



    def word_check(self):
        word_cnt = 0
        with open(self.fname,"r") as file:
            for line in file:
                words = line.split()
                word_cnt +=len(words)
        return word_cnt

    def digit_check(self):
        digit_cnt = 0
        with open(self.fname,"r") as f:
            for line in f:
                for word in line:
                    if(word.isdigit()):
                        digit_cnt += 1
        return digit_cnt
