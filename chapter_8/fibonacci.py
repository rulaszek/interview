def fibonacci_recursive(i, memo):
    if i == 0 or i == 1:
        return i

    if memo[i] == 0:
        memo[i] = fibonacci_recursive(i - 1, memo) + fibonacci_recursive(i - 2, memo)

    return memo[i]


def fibonacci_iterative1(i):
    if i == 0 or i == 1:
        return i

    memo = [0]*i

    memo[0] = 0
    memo[1] = 1

    for j in range(2, i):
        memo[j] = memo[j-1] + memo[j-2]

    return memo[i-1] + memo[i-2]


def fibonacci_iterative2(i):
    if i == 0 or i == 1:
        return i

    a = 0
    b = 1

    for j in range(2, i):
        c = a + b
        a = b
        b = c

    return a + b

if __name__ == '__main__':
    #print fibonacci_recursive(35, [0]*36)
    #print fibonacci_iterative1(34)
    print fibonacci_iterative2(34)
