from Queue import Queue


class TreeNode:

    data = None
    left = None
    right = None

    visited = False
    marked = False

    def __init__(self, data):
        self.data = data

    def print_data(self):
        left_data = self.left.data if self.left else None
        right_data = self.right.data if self.right else None
        print 'node: {0}, left: {1}, right: {2}'.format(self.data, left_data, right_data)


def visit(node):
    node.print_data()


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node is not None:
        visit(node)
        in_order_traversal(node.left)
        in_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        visit(node)


def dfs(node):
    if node is None:
        return

    visit(node)

    node.visited = True

    if node.left and not node.left.visited:
        dfs(node.left)
    if node.right and not node.right.visited:
        dfs(node.right)


def bfs(node):

    q = Queue()

    node.marked = True
    q.put(node)

    while not q.empty():
        n = q.get()
        visit(n)

        if n.left:
            n.left.marked = True
            q.put(n.left)

        if n.right:
            n.right.marked = True
            q.put(n.right)


def create_minimal_bst(array, start, end):

    if end < start:
        return None

    mid = (start + end) / 2
    n = TreeNode(array[mid])
    n.left = create_minimal_bst(array, start, mid - 1)
    n.right = create_minimal_bst(array, mid + 1, end)

    return n


if __name__ == '__main__':
    tree = create_minimal_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9)
    #in_order_traversal(tree)
    #pre_order_traversal(tree)
    #post_order_traversal(tree)

    #dfs(tree)
    bfs(tree)
