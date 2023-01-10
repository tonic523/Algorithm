import collections
import sys

input = sys.stdin.readline

'''
1 ~ 10 (11, 19) 20 21 (22, 29)
최대값: 9876543210 -> 총갯수: 1023
- Dfs 로 탐색
'''

N = int(input())
stack = collections.deque()
results = []

def dfs(before_number):
    global stack

    for i in range(10):
        if i >= before_number:
            break
        stack.append(i)
        results.append(int("".join(list(map(str, stack)))))
        dfs(i)
        stack.pop()


dfs(10)
l = sorted(results)

if N > len(l):
    print(-1)
else:
    print(l[N-1])
