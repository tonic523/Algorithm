import collections
import sys

input = sys.stdin.readline

S = input().rstrip()
c_count = collections.Counter(S)
count = 0


def solve(before_c, len_s):
    global count

    if len_s == len(S):
        count += 1
        return

    for c in c_count.keys():
        if c == before_c or c_count[c] == 0:
            continue
        c_count[c] -= 1
        solve(c, len_s+1)
        c_count[c] += 1


solve("", 0)
print(count)
