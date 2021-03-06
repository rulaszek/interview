def check_for_duplicates(A):
    A.sort()

    for i in range(0, len(A)):

        if A[abs(A[i])] < 0:
            return True
        else:
            A[A[i]] = - A[A[i]]

    return False


def max_repetitions(A):
    freq = {}

    for el in A:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1

    max_count = 0
    max_el = None

    for el in A:
        if freq[el] > max_count:
            max_count = freq[el]
            max_el = el

    return max_el


def two_elements_with_sum(A, k):
    freq = {}

    for el in A:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1

    for el in A:
        if k - el in freq:
            return True

    return False


def binary_search(array, item):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2
        if array[midpoint] == item:
            return True
        else:
            if item < array[midpoint]:
                return binary_search(array[:midpoint], item)
            else:
                return binary_search(array[midpoint + 1:], item)


if __name__ == '__main__':
    print binary_search([1, 2, 3, 4, 5], 5)
