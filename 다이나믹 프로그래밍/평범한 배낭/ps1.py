import sys

input = sys.stdin.readline

# N = 물품의 수, K = 버틸 수 있는 무게
N, K = map(int, input().rstrip().split())

# 물건 리스트 (무게, 가치)
products = [0]
for _ in range(N):
    products.append(tuple(map(int, input().rstrip().split())))

# N개의 물품의 수를 고려했을 때 K 무게에서 가장 높은 가치를 저장하는 2차원 배열
d = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1):
    weight, value = products[n] # 현재 순회하는 물품의 무게와 가치
    for k in range(1, K+1):
        if weight <= k:
            # (현재 물품의 무게를 뺏을 때 최대 가치 + 현재 물품의 가치, 현재 물품을 포함하지 않았을 때 최대 가치)
            d[n][k] = max(d[n-1][k-weight] + value, d[n-1][k])
        else:
            # 현재 물품을 포함하지 않았을 때 최대 가치
            d[n][k] = d[n-1][k]

print(d[N][K])
