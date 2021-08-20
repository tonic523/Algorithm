import sys
input = sys.stdin.readline
K, N = map(int, input().rstrip().split())
k_list = [int(input()) for _ in range(K)]

left, right = 1, max(k_list)
result = 0
while left <= right:
    mid = (left + right) // 2
    n_cnt = 0
    for k in k_list:
        n_cnt += k // mid

    if n_cnt == N:
        result = mid

    if n_cnt < N:
        right = mid - 1
    else:
        left = mid + 1
print(result)