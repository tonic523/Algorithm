import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
in_o = list(map(int, input().rstrip().split()))
post_o = list(map(int, input().rstrip().split()))

# 리스트의 값과 인덱스 switch 방법
index = [0] * (N+1)
for i in range(N):
    index[in_o[i]] = i

def solve(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return

    parent = post_o[r_post]
    print(parent, end = " ")

    p_idx = index[parent]
    left = p_idx - l_in

    solve(l_in, p_idx - 1, l_post, (l_post + left) - 1)
    solve(p_idx + 1, r_in, l_post + left, r_post - 1)

solve(0, N-1, 0, N-1)