from Queue import Queue


class Node(object):

    data = None
    next_node = None

    left = None
    right = None

    marked = False
    level = 0

    def __init__(self, data):
        self.data = data


def build_graph(arr, start, end):

    if end < start:
        return None

    mid = (start + end) / 2
    node = Node(arr[mid])
    node.left = build_graph(arr, start, mid - 1)
    node.right = build_graph(arr, mid + 1, end)

    return node


def dfs(root, target, s):

    q = Queue()

    root.marked = True
    q.put(root)
    s.append([root])

    while not q.empty():
        n = q.get()
        n.marked = True

        print n.data

        level = []
        if n.left and not n.left.marked:
            if n.data == target:
                break
            else:
                q.put(n.left)
                level.append(n)
        if n.right and not n.right.marked:
            if n.data == target:
                break
            else:
                q.put(n.right)
                level.append(n)

        s.append(level)


def in_order_traversal(root):

    if not root:
        return

    in_order_traversal(root.left)
    print root.data
    in_order_traversal(root.right)

if __name__ == '__main__':
    root = build_graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9)
#    in_order_traversal(root)
    print dfs(root, 8)
