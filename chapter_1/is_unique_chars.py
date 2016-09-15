def is_unique_chars(phrase):

    if len(phrase) > 128:
        return False

    char_set = [False]*128

    for c in phrase:
        if char_set[ord(c)]:
            return False

        char_set[ord(c)] = True

    return True

if __name__ == "__main__":
    print is_unique_chars('phrase')
