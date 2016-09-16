class Node:

    next_node = None
    data = None

    def __init__(self, d):
        self.data = d

    def append(self, d):
        end = Node(d)

        n = self
        while n.next_node is not None:
            n = n.next_node

        n.next_node = end

    def delete(self, d):
        return self.delete_node(self, d)

    def delete_node(self, head, d):
        n = head

        if n.data == d:
            return head.next_node

        while n.next_node is not None:
            if n.next_node.data == d:
                n.next_node = n.next_node.next_node
                return head

            n = n.next_node

        return head

    def to_array(self):
        lst = [self.data]

        n = self
        while n.next_node is not None:
            n = n.next_node
            lst.append(n.data)

        return lst


if __name__ == '__main__':
    node = Node(5)
    print node.to_array()
    node.append(10)
    print node.to_array()
    node.append(15)
    print node.to_array()
    node = node.delete(5)
    print node.to_array()
    node = node.delete(15)
    print node.to_array()
