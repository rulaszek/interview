class Node(object):

    def __init__(self):
        self._data = None
        self._next = None

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_next(self, n):
        self._next = n

    def get_next(self):
        return self._next


class LinkedList(object):

    def __init__(self):
        self._head = None
        self._length = 0

    def count(self):
        current = self._head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def insert_at_head(self, data):

        node = Node()
        node._data = data

        if self._head is None:
            self._head = node
        else:
            node.set_next(self._head)
            self._head.set_next(node)

        self._length += 1

    def insert_at_end(self, data):

        node = Node()
        node.set_data(data)

        current = self._head

        while current is not None:
            current = current.get_next()

        current.set_next(node)

        self._length += 1

    def insert_at_pos(self, pos, data):

        if pos > self._length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_head(data)
            else:
                if pos == self._length:
                    self.insert_at_end(data)
                else:
                    node = Node()
                    node.set_data(data)

                    current = self._head
                    count = 1

                    while count < pos - 1:
                        count += 1
                        current = current.get_next()

                    node.set_next(current.get_next())
                    current.set_next(node)

                    self._length += 1

    def nth_node_from_end(self, n):

        if n <= 0:
            return None

        temp = self._head
        count = 0

        while count < n and temp is not None:
            temp = temp.get_next()
            count += 1

        if count < n or temp is None:
            return None

        nth = self._head

        while temp is not None:
            temp = temp.get_next()
            nth = nth.get_next()

        return nth

    def detect_cycle(self):

        fast_ptr = self._head
        slow_ptr = self._head

        while fast_ptr and slow_ptr:
            fast_ptr = fast_ptr.get_next()

            if fast_ptr == slow_ptr:
                return True

            if fast_ptr is None:
                return False

            fast_ptr = fast_ptr.get_next()

            if fast_ptr == slow_ptr:
                return True

            slow_ptr = slow_ptr.get_next()

        return False



