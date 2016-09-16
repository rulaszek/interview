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

    def remove_duplicates(self):

        duplicates = {}

        n = self
        previous = None
        while n is not None:

            if n.data in duplicates:
                previous.next_node = n.next_node
            else:
                duplicates[n.data] = True
                previous = n

            n = n.next_node

    def print_kth_to_last(self, head, k):

        if head is None:
            return 0

        index = self.print_kth_to_last(head.next_node, k) + 1

        if index == k:
            print head.data

        return index

    def delete_node(self, n):

        if n is None or n.next_node is None:
            return False

        next_node = n.next_node

        n.data = next_node.data
        n.next_node = next_node.next_node

        return True

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
    node.append(5)
    print node.to_array()
    node.append(5)
    print node.to_array()
    node.remove_duplicates()
    print node.to_array()
    node.append(10)
    print node.to_array()
    node.append(15)
    print node.to_array()

    node.print_kth_to_last(node, 1)

    print node.to_array()
    node.delete_node(node)
    print node.to_array()
