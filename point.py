class Point:
    def __init__(self, line: int, column: int, object: str = '.'):
        self.line = line
        self.column = column
        self.object = object

    def __eq__(self, other) -> bool:
        if isinstance(other, tuple):
            return (self.line, self.column) == other

        if isinstance(other, self.__class__):
            return (self.line, self.column) == (other.line, other.column)

        return False
