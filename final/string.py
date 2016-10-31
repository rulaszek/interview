
def rev(s):

    r = ''

    for c in s:
        r = c + r

    return r

if __name__ == '__main__':
    print rev('foo')
