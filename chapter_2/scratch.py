class Node(object):

    node_data = None
    node_next = None

    def __init__(self, data):
        self.node_data = data


class LinkedList(object):

    head = None

    def append(self, data):

        node = Node(data)

        if not self.head:
            self.head = node
            return

        if not self.head.node_next:
            self.head.node_next = node
            return

        current = self.head
        while current.node_next:
            current = current.node_next

        current.node_next = node

    def to_array(self):
        arr = []

        if not self.head:
            return []

        if not self.head.node_next:
            return [self.head.node_data]

        current = self.head
        while current:
            arr.append(current.node_data)
            current = current.node_next

        return arr

    def de_dupe(self):

        freq = {}

        current = self.head
        previous = None
        while current:
            if current.node_data in freq:
                previous.node_next = current.node_next
            else:
                freq[current.node_data] = True
                previous = current

            current = current.node_next


def remove_duplicates():
    pass

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append('5')
    linked_list.append('6')
    linked_list.append('7')
    linked_list.append('7')
    linked_list.append('8')

    print linked_list.to_array()

    linked_list.de_dupe()

    print linked_list.to_array()
