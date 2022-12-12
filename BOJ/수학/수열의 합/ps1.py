import sys

input = sys.stdin.readline


def solve(n, l):
    if l > 100:
        return [-1]
    q = n // l

    # 수열 합 구하기
    sum_of_sequences = 0
    for i in range(l):
        sum_of_sequences += q + i

    # 정답인 수열 찾기
    t = 0
    while sum_of_sequences >= n:
        if sum_of_sequences == n:
            # 정답인 수열을 응답
            q -= t
            sequence = []
            for i in range(l):
                sequence.append(q+i)
            return sequence
        sum_of_sequences -= l
        t += 1
        if q < t:
            return [-1]

    return solve(n, l + 1)


N, L = map(int, input().rstrip().split())

print(*solve(N, L))
