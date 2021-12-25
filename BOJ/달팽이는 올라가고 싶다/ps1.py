import sys

input = sys.stdin.readline

A, B, V = map(int, input().rstrip().split())
quotient, remainder = divmod((V - A), (A - B))
print(quotient + 1 if remainder == 0 else quotient + 2)