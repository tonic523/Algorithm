import sys

input = sys.stdin.readline

def sol1676():
    N = int(input())
    result = 0
    number = 1
    if N != 0:
        for n in range(1, N+1):
            number *= n
    number = str(number)
    for n in reversed(number):
        if n == '0':
            result += 1
        else:
            break
    print(result)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    sol1676()