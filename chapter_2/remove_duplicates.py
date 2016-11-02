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

    def k_to_the_nth(self, head, k):

        slow = head
        fast = head
        pos = 0

        while fast.next_node and pos < k:
            fast = fast.next_node
            pos += 1

        if pos < k:
            return None

        while fast.next_node:
            slow = slow.next_node
            fast = fast.next_node

        return slow.data

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


class LinkedList(object):

    head = None

    def append(self, data):

        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = Node(data)


def sum_nodes(le, ri):

    re = LinkedList()
    rem = 0

    while le and ri:
        w = (rem + le.data + ri.data) % 10
        rem = (rem + le.data + ri.data) / 10
        re.append(w)
        le = le.next_node
        ri = ri.next_node

    return re.head


if __name__ == '__main__':
    left = Node(7)
    left.append(1)
    left.append(6)

    right = Node(5)
    right.append(9)
    right.append(2)

    result = sum_nodes(left, right)

    print result.to_array()
