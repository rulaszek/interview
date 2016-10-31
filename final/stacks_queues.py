class Stack(object):

    def __init__(self):
        self.__storage = []

    def is_empty(self):
        return len(self.__storage) == 0

    def push(self, data):
        self.__storage.append(data)

    def pop(self):
        return self.__storage.pop()


def is_palindrome(str):

    str_stack = Stack()

    for c in str:
        str_stack.push(c)

    for c in str:
        if c != str_stack.pop():
            return False


class Queue(object):

    def __init__(self):
        self.S1 = []
        self.S2 = []

    def enqueue(self, element):
        self.S2.append(element)

    def dequeue(self):

        if not self.S1:
            while self.S2:
                self.S1.append(self.S2.pop())

        return self.S2.pop()
