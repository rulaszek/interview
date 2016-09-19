from Queue import Queue


class Graph:

    children = {}

    def __init__(self):
        pass

    def create(self, data):
        self.children[data] = GraphNode(data)
        return self.children[data]

    def search(self, start, end):

        if start == end:
            return True

        q = Queue()

        for k in self.children:
            self.children[k].state = 'Unvisted'

        start.state = 'Visiting'
        q.put(start)

        while not q.empty():
            u = q.get()

            if u:
                for child in u.children:
                    if child.state == 'Unvisted':
                        if child == end:
                            return True
                        else:
                            child.state = 'Visiting'
                            q.put(child)

            u.state = 'Visited'

        return False


class GraphNode:

    state = None
    data = None
    children = []

    def __init__(self, data):
        self.data = data

    def add(self, nodes):
        for node in nodes:
            self.children.append(node)

    def __eq__(self, other):
        return self.data == other.data

if __name__ == '__main__':
    g = Graph()

    a = g.create('A')
    b = g.create('B')
    c = g.create('C')
    d = g.create('D')
    e = g.create('E')
    f = g.create('F')

    a.add([b, c])
    b.add([c, d])
    c.add([d])
    d.add([c])
    e.add([f])
    f.add([c])

    print g.search(a, d)
