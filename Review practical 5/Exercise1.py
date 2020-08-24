def naive_fib(n):
    if n <= 2:
        return 1
    else:
        return naive_fib(n-1) + naive_fib(n-2)


def fib_count(n):
    count = [0] * n

    def fib(num):
        count[num-1] += 1
        if num <= 2:
            return 1
        else:
            return fib(num-1) + fib(num-2)
    fib(n)
    return count


def dp_fib(n):
    memo = [None] * n
    memo[0] = 1
    if n >= 2:
        memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1]


def test_naive_fib():
    assert naive_fib(7) == 13, "naive_fib test 1 failed"
    assert naive_fib(3) == 2, "naive_fib test 2 failed"


def test_fib_count():
    assert fib_count(4) == [1, 2, 1, 1], "fib_count test 1 failed"
    assert fib_count(5) == [2, 3, 2, 1, 1],"fib_count test 2 failed"


def test_dp_fib():
    assert dp_fib(8) == 21, "dp_fib test 1 failed"
    assert dp_fib(1) == 1, "dp_fib test 2 failed"


test_naive_fib()
test_fib_count()
test_dp_fib()
