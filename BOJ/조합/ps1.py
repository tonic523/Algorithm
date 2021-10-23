import sys

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

def factorial(num, last):
    if num <= last:
        return 1
    return num * factorial(num-1, last)

print(factorial(n, n-m) // factorial(m, 1))