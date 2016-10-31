def is_palindrome(phrase):

    l = len(phrase)
    mid = l/2
    left = mid - 1
    right = mid if l % 2 == 0 else mid + 1

    print left, right

    while left >= 0 and right < l:
        if phrase[left] != phrase[right]:
            return False

        left -= 1
        right += 1

    return True


if __name__ == '__main__':
    print is_palindrome('racecar')
    print is_palindrome('hannah')
    print is_palindrome('hannah2')
    print is_palindrome('racecarr')
