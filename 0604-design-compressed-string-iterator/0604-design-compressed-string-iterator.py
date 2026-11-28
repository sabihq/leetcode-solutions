class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.index = 0
        self.char = ""
        self.count = 0

    def next(self) -> str:
        if not self.hasNext():
            return " "

        if self.count == 0:
            self.char = self.s[self.index]
            self.index += 1

            while self.index < len(self.s) and self.s[self.index].isdigit():
                self.count = self.count * 10 + int(self.s[self.index])
                self.index += 1

        self.count -= 1
        return self.char

    def hasNext(self) -> bool:
        return self.count > 0 or self.index < len(self.s)