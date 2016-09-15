def compress(s):

    compressed = []

    count_consequtive = 0
    for i in range(len(s)):
        count_consequtive += 1

        if i + 1 >= len(s) or s[i] != s[i+1]:
            compressed.append(s[i])
            compressed.append(str(count_consequtive))
            count_consequtive = 0

    return ''.join(compressed) if len(compressed) < len(s) else s


if __name__ == '__main__':
    print compress('aaaabbcccddddd')
