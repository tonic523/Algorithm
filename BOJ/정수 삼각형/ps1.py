import sys

input = sys.stdin.readline

N = int(input())
graph = [[int(input())]]

for i in range(1, N):
    nums = list(map(int, input().rstrip().split()))
    graph.append(nums)

def dfs(graph):
    answer = 0
    queue = [(0,0,graph[0][0])]
    while queue:
        r, c, now = queue.pop()
        if r == N-1:
            answer = answer if answer > now else now
        else:
            queue.append((r+1, c, graph[r+1][c] + now))
            queue.append((r+1, c+1, graph[r+1][c+1] + now))
    return answer

print(dfs(graph))