import sys

input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def sol1676():
    N = int(input())
    result = 0
    number = str(factorial(N))
    for n in reversed(number):
        if n == '0':
            result += 1
        else:
            break
    print(result)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    sol1676()