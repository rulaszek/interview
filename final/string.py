
def reverse(s):

    r = ''

    for c in s:
        r = c + r

    return r


def reverse_long(s):

    sl = list(s)

    start = 0
    end = len(sl) - 1

    while start < end:
        temp = sl[start]
        sl[start] = sl[end]
        sl[end] = temp

        start += 1
        end -= 1

    return ''.join(sl)
