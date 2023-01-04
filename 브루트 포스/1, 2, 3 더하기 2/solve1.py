import sys
from itertools import permutations

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
answer = []

# 합이 11이 되는 모든 경우의 수 구하기
sum_case = set()
for one_value in range(0, n+1, 1):
    for two_value in range(0, n+1-one_value, 2):
        for three_value in range(0, n+1-two_value, 3):
            sum_value = one_value + two_value + three_value
            if sum_value == n:
                sum_case = sum_case | set(permutations([1] * one_value + [2] * (two_value // 2) + [3] * (three_value // 3)))

# k 번째 값 출력 양식에 맞게 출력
sorted_case = sorted(sum_case)
print("+".join(list(map(str,sorted_case[k-1]))) if k <= len(sorted_case) else -1)
