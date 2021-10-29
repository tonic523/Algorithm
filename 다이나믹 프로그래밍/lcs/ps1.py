import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

def lcs(s1, s2):
    answer = 0
    idx = 0
    for c1 in s1:
        now =get_idx_exist(c1, s2, idx)
        if idx != now:
            answer += 1
            idx = now
    return answer


def get_idx_exist(v, s, from_idx):
    for i in range(from_idx, len(s)):
        if s[i] == v:
            return i+1
    return from_idx

print(lcs(s1, s2))