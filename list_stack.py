class Stack:
    """A list-based stack"""

    def __init__(self):
        self.__values = []

    def peek(self):
        return self.__values[-1]

    def push(self, val):
        self.__values.append(val)

    def pop(self):
        return self.__values.pop()

    def size(self):
        return len(self.__values)

    def is_empty(self):
        return len(self.__values) == 0

    def __repr__(self):
        return str(self.__values) + " <="

    def __str__(self):
        return str(self.__values) + " <="

    def __len__(self):
        """Want to call len(Stack)? Implement the __len__() magic method!"""
        return self.size()


