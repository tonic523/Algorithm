import sys

input = sys.stdin.readline
A, B, C = map(int, input().strip().split())

def calculate(A, B):
    if B == 1:
        return A % C
    else:
        temp = calculate(A, B//2)
        if B % 2 == 0:
            return temp * temp % C
        else:
            return (temp * temp) * A % C

print(calculate(A, B) % C)