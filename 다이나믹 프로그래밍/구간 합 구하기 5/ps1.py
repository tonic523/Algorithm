import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[0] * (N+1)]
for i in range(N):
    temp = [0]
    temp += list(map(int, input().rstrip().split()))
    for j in range(1, N+1):
        temp[j] += temp[j-1]
    graph.append(temp)

for i in range(1, N):
    for j in range(N):
        graph[i][j] += graph[i-1][j]

print(graph)

def graph_sum(x1, y1, x2, y2):
    answer = graph[x2][y2]
    answer -= graph[x1-1][y2]
    answer -= graph[x2][y1-1]
    answer += graph[x1-1][y1-1]
    return answer

for j in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    answer = graph_sum(x1, y1, x2, y2)
    print(answer)