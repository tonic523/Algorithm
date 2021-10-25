import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().rstrip().split()))
# 유클리드 호제법
def gcd(lst):
    def g(x, y):
        while y:
            x, y = y, x%y
        return x
    a = lst[0]
    for b in lst[1:]:
        a = g(a, b)
    return a

def BT(array):
    mid = len(array) // 2
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return array[0] + array[1]

    return max(BT(array[:mid])+gcd(array[mid:]), BT(array[mid:])+gcd(array[:mid]))

mid = N // 2
if N == 1:
    print(numbers[0])
else:
    print(max(BT(numbers[:mid])+gcd(numbers[mid:]), BT(numbers[mid:])+gcd(numbers[:mid])))