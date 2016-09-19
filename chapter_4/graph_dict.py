def find_path(graph, start, end, path=[]):
    path = path + [start]
    print path

    if start == end:
        return path

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)

            if new_path:
                return new_path

    return None


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    print path

    if start == end:
        return path

    if start not in graph:
        return None

    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)

            if new_path:
                if not shortest or (len(new_path) < len(shortest)):
                    shortest = new_path

    return shortest


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    print path

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)

            for new_path in new_paths:
                paths.append(new_path)

    return paths

if __name__ == '__main__':
    g = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']
    }

    print find_shortest_path(g, 'A', 'D')
