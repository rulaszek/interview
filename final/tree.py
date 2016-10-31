import Queue

class Node:

    def __init__(self):
        self._data = None
        self._left = None
        self._right = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self, node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self, node):
        self._right = node

    def get_right(self):
        return self._right


def pre_order_traversal(root, results):

    if not root:
        return

    results.append(root.get_data())
    pre_order_traversal(root.get_left(), results)
    pre_order_traversal(root.get_right(), results)


def in_order_traversal(root, results):

    if not root:
        return

    in_order_traversal(root.get_left(), results)
    results.append(root)
    in_order_traversal(root.get_right(), results)


def post_order_traversal(root, results):

    if not root:
        return

    post_order_traversal(root.get_left(), results)
    post_order_traversal(root.get_right(), results)

    results.append(root.data())


def level_order(root, results):

    q = Queue.Queue()
    q.enqueue(root)

    while not q.empty():
        node = q.dequeue()
        results.append(node.data())

        if node.get_left():
            q.enqueue(node.get_left())
        if node.get_right():
            q.enqueue(node.get_right())

max_data = float("-infinity")


def get_max_data(root):
    global max_data

    if not root:
        return max_data

    if root.get_data() > max_data:
        max_data = root.get_data()

    get_max_data(root.get_left())
    get_max_data(root.get_right())

    return max_data
