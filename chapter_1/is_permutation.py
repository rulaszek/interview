def is_permutation(s1, s2):

    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    return s1_sorted == s2_sorted

if __name__ == '__main__':
    print is_permutation('foo', 'oof')
