class QueueNode:

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data


class Queue:

    first = None
    last = None

    def __init__(self):
        pass

    def is_empty(self):
        return self.first is None

    def add(self, data):

        node = QueueNode(data)

        if self.last is not None:
            self.last.next_node = node

        self.last = node

        if self.first is None:
            self.first = self.last

        return node.data

    def remove(self):

        if self.first is None:
            raise Exception('No node to remove')

        data = self.first.data

        self.first = self.first.next_node

        if self.first is None:
            self.last = None

        return data

    def peek(self):
        return self.first.data

if __name__ == '__main__':
    queue = Queue()
    print queue.is_empty()
    print queue.add(5)
    print queue.peek()
    print queue.add(10)
    print queue.peek()
    print queue.remove()
    print queue.peek()
    print queue.remove()
    print queue.is_empty()
