import sys

input = sys.stdin.readline

R, C, Q = map(int, input().rstrip().split())

graph = []

# 일반 for문보다 메모리에서 약간의 이득이 있고 시간에서 약간의 손해가 있다. 결론적으로 큰 차이 없음
graph = [[0] * (C+1)] + [[0] + list(map(int, input().rstrip().split())) for _ in range(R)]

for i in range(1, R+1):
    for j in range(1, C+1):
        graph[i][j] += graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1]

result = []
for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().rstrip().split())
    answer = graph[y2][x2] - graph[y1-1][x2] - graph[y2][x1-1] + graph[y1-1][x1-1]
    result.append(str(answer // ((x2-x1+1) * (y2-y1+1))))

print("\n".join(result))
