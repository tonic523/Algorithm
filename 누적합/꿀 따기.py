import sys

input = sys.stdin.readline

'''
이 문제의 핵심
아래의 3가지 조건 중 최대값의 점화식을 구하는 것이다.
1. 벌 벌 꿀통 순서일 때 - 가장 왼쪽에 벌이 있고 가장 오른쪽에 꿀통이 있는 형태에서 최대값이 나온다.
2. 벌 꿀통 벌 순서일 때 - 양 끝에 벌이 있는 형태에서 최대값이 나온다.
3. 꿀통 벌 벌 순서일 때 - 가장 왼쪽에 꿀통이 있고 가장 오른쪽에 벌이 있는 형태에서 최대값이 나온다.
'''

N = int(input())

honey = list(map(int, input().rstrip().split()))
prefix_sum = list(honey)

for i in range(1, N):
    prefix_sum[i] += prefix_sum[i-1]

answer = 0
for i in range(1, N-1):
    bbh = prefix_sum[N-1] * 2 - honey[0] - honey[i] - prefix_sum[i]
    bhb = prefix_sum[N-2] - honey[0] + honey[i]
    hbb = prefix_sum[N-2] + prefix_sum[i-1] - honey[i]
    answer = max(answer, bbh, bhb, hbb)

print(answer)
