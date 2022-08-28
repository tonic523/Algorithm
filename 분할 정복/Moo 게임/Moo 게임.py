import sys

input = sys.stdin.readline

N = int(input())


def moo_game(a, b, n):
    if n <= a:
        return moo_game((a - (b-1)) // 2, b-1, n)
    if a < n <= a + b:
        if n - a == 1:
            return 'm'
        return 'o'
    if a + b < n <= 2 * a + b:
        n -= a + b
        return moo_game((a - (b-1)) // 2, b-1, n)
    return moo_game(2*a+b, b+1, n)


result = moo_game(0, 3, N)
print(result)
