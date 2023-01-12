import collections
import sys

input = sys.stdin.readline

'''
aabbbaa -> abababa
ab -> ab, ba
aaab -> none
abcdefghij -> 3628800 (최대 횟수) (10!)

python의 변수 scope가 어떻게 되지? java는??
'''

S = input().rstrip()
s_index = set([i for i in range(len(S))])
stack = collections.deque()
count = 0
visited = set()


def solve(before_c, s_index):
    global stack
    global count

    if len(stack) == len(S) and "".join(stack) not in visited:
        count += 1
        visited.add("".join(stack))
        return
    for i in s_index:
        c = S[i]
        if before_c == c:
            continue
        stack.append(c)
        next_index = s_index.copy()
        next_index.remove(i)
        solve(c, next_index)
        stack.pop()


solve("", s_index)
print(count)
