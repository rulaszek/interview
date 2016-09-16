class StackNode:

    data = None
    next_node = None

    def __init__(self, d):
        self.data = d


class Stack:

    top = None

    def __init__(self):
        pass

    def is_empty(self):
        return self.top is None

    def push(self, item):
        node = StackNode(item)

        if self.top is None:
            self.top = node
        else:
            node.next_node = self.top
            self.top = node

        return self.top.data

    def peek(self):
        if self.top is None:
            raise Exception('No item in list')

        return self.top.data

    def pop(self):
        if self.top is None:
            raise Exception('No item in list')

        data = self.top.data

        self.top = self.top.next_node

        return data

if __name__ == '__main__':
    stack = Stack()
    print stack.is_empty()
    print stack.push(5)
    print stack.peek()
    print stack.pop()
    print stack.is_empty()
