import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

li = list(set(map(int, input().rstrip().split())))
li.sort()

def bt(sequence):
    if len(sequence) == M:
        print(*sequence)
        return

    for i in li:
        if len(sequence) == 0 or sequence[-1] <= i:
            sequence.append(i)
            bt(sequence)
            sequence.pop()

bt(list())