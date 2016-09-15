def build_frequency_table(phrase):
    table = [0]*(ord('z')-ord('a')+1)

    for c in phrase:
        if ord('a') <= ord(c) <= ord('z'):
            table[ord(c) - ord('a')] += 1

    print table
    return table


def is_max_one_odd(table):
    found_odd = False

    for i in table:
        if i % 2 == 1:
            if found_odd:
                return False
            found_odd = True

    return True


def is_permutation_palindrome(phrase):
    table = build_frequency_table(phrase)
    return is_max_one_odd(table)

if __name__ == '__main__':
    print is_permutation_palindrome('fooxoof')
