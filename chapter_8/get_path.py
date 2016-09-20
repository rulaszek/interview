def _get_path(matrix, r, c, path):

    if r < 0 or c < 0:
        return False

    is_origin = r == 0 and c == 0

    if is_origin or _get_path(matrix, r, c - 1, path) or _get_path(matrix, r - 1, c, path):
        path.append([r, c])
        return True

    return False


def get_path(matrix):
    if not matrix or len(matrix) == 0:
        return None

    path = []
    if _get_path(matrix, len(matrix) - 1, len(matrix[0]) - 1, path):
        return path

    return None

if __name__ == '__main__':
    r, c = 10, 10
    m = [[0 for x in range(r)] for y in range(c)]
    print get_path(m)
