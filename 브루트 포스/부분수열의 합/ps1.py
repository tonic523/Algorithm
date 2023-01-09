import itertools
import sys

'''
모든 조합의 수: O(2^n)
따라서 최대 2^20이므로 1048576이다.
'''

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())

li = list(map(int, input().rstrip().split()))
answer = 0
for i in range(1, len(li)+1):
    cases = itertools.combinations(li, i)
    for case in cases:
        if sum(case) == S:
            print(case)
            answer += 1
print(answer)
