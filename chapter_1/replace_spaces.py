def replace_spaces(phrase, true_length):

    spaces = 0
    for c in phrase:
        if c.isspace():
            spaces += 1

    index = true_length + spaces * 2

    for i in range(true_length - 1, -1, -1):
        if phrase[i].isspace():
            phrase[index - 1] = '0'
            phrase[index - 2] = '2'
            phrase[index - 3] = '%'
            index -= 3
        else:
            phrase[index - 1] = phrase[i]
            index -= 1

    return phrase

if __name__ == '__main__':
    l = list('f oo ')
    l.extend(['']*5)
    print l
    print replace_spaces(l, 5)
