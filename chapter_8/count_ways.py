def count_ways(i, n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    next = i + 1
    result = count_ways(next, n - 1) + count_ways(next, n - 2) + count_ways(next, n - 3)
    print '{0} = cw({1}) + cw({2}) + cw({3}), {4}'.format(result, n-1, n-2, n-3, i)
    return result


if __name__ == '__main__':
    result = count_ways(3, 1)
    # print count_ways(2)
    # print count_ways(3)
    # print count_ways(4)
    # print count_ways(5)
