from Queue import Queue


class TreeNode:

    data = None
    left = None
    right = None

    marked = False

    def __init__(self, data):
        self.data = data


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        # visit
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node is not None:
        # visit
        in_order_traversal(node.left)
        in_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        # visit


def dfs(node):
    if node is None:
        return

    # visit

    node.visited = True

    if node.left and not node.left.visited:
        dfs(node.left)
    if node.right and not node.right.visited:
        dfs(node.right)


def bfs(root, target):

    q = Queue()

    root.marked = True
    q.put(root)

    while not q.empty():
        n = q.get()
        n.marked = True

        print n.data

        if n.left and not n.left.marked:
            if n.data == target:
                break
            else:
                q.put(n.left)
        if n.right and not n.right.marked:
            if n.data == target:
                break
            else:
                q.put(n.right)


def create_minimal_bst(array, start, end):

    if end < start:
        return None

    mid = (start + end) / 2
    n = TreeNode(array[mid])
    n.left = create_minimal_bst(array, start, mid - 1)
    n.right = create_minimal_bst(array, mid + 1, end)

    return n


def binary_search(a, x, low, high):
    if low < high:
        return -1

    mid = (low + high) / 2

    if a[mid] < x:
        return binary_search(a, x, mid + 1, high)
    elif a[mid] > x:
        return binary_search(a, x, low, mid - 1)
    else:
        return mid
