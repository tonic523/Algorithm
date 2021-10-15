import sys

input = sys.stdin.readline

def bf(start):
    distance = [1e9] * len(graph)
    distance[start] = 0
    for i in range(1, N+1):
        for s in range(1, N+1):
            for end, cost in graph[s]:
                cost += distance[s]
                if cost < distance[end]:
                    distance[end] = cost
                    if i == N:
                        return True
    return False

answer = []

for _ in range(int(input())):
    N, M, W = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    for _ in range(W):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, -c))

    answer.append("YES" if bf(1) else "NO")

print("\n".join(answer))